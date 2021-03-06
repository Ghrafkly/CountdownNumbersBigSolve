package main

import (
	"encoding/csv"
	"fmt"
	"os"
	"sort"
	"strconv"
	"strings"
	"time"

	"github.com/ernestosuarez/itertools"
	"github.com/karrick/gorpn"
)

var equations [][]string
var sub = make(map[string]float64)

func main() {
	start := time.Now()
	var operators = []string{"+", "-", "*", "/"}
	var number = []string{"1", "1", "2", "2", "3", "3", "4", "4", "5", "5", "6", "6", "7", "7", "8", "8", "9", "9", "10", "10", "25", "50", "75", "100"}
	var ops_needed int = -1
	var sol []string

	// Creates a dict of all 3 digit numbers. Values set to 0
	threeDigits := make(map[int]int)
	for i := 101; i < 1000; i++ {
		threeDigits[i] = 0
	}

	// Deals with duplicates for Combinations
	var cNums [][]string
	allKeys := make(map[string]bool)
	comb := itertools.CombinationsStr(number, 4)
	for item := range comb {
		var strSlc string = strings.Join(item[:], ",") // Turns slice into string to create unique key
		if _, value := allKeys[strSlc]; !value {
			allKeys[strSlc] = true
			cNums = append(cNums, [][]string{item}...)
		}
	}

	// Deals with duplicates for Permutations
	permKeys := make(map[string]bool)
	for _, item := range cNums {
		var pNums [][]string
		perm := itertools.PermutationsStr(item, len(item))
		for x := range perm {
			var permSlc string = strings.Join(x[:], ",") // Turns slice into string to create unique key
			if _, value := permKeys[permSlc]; !value {
				pNums = append(pNums, [][]string{x}...)
				permKeys[permSlc] = true
			}
		}

		for _, item := range pNums {
			// fmt.Println(item)
			var current []string
			rpn(item, operators, current, ops_needed)
		}

		sol = append(sol, []string(equate(equations))...) // Add all (valid) solutions to a slice

		for _, v := range sol {
			i, _ := strconv.Atoi(v) // Convert solutions into ints
			threeDigits[i] += 1     // Increment the dict by one where a solution exists
		}
		sol = nil       // Reset sol so it doesn't kill the memory
		equations = nil // Reset equations for next round
	}

	cNums = nil

	// Write the key, value to a csv file
	writeToCsv("GoNumbers.csv", threeDigits)

	elapsed := time.Since(start)
	fmt.Printf("Elapsed: %v\n", elapsed)
}

func writeToCsv(fileName string, dict map[int]int) {
	file, _ := os.Create(fileName)
	w := csv.NewWriter(file)
	defer w.Flush()

	var keys []int
	for k := range dict {
		keys = append(keys, k)
	}
	sort.Ints(keys)
	for _, k := range keys {
		row := []string{strconv.Itoa(k), strconv.Itoa(dict[k])}
		w.Write(row)
	}
}

func rpn(nums []string, ops []string, current []string, ops_needed int) {
	if ops_needed == 0 && len(nums) == 0 {
		c := make([]string, len(current))
		copy(c, current)
		equations = append(equations, [][]string{c}...)
	}

	if ops_needed > 0 {
		for _, op := range ops {
			current = append(current, op)
			rpn(nums, ops, current, ops_needed-1)
			current = current[:len(current)-1]
		}
	}

	if size := len(nums); size > 0 {
		v := nums[size-1]            // Save pop value
		nums = nums[:size-1]         // Pop last element
		current = append(current, v) // Push element
		rpn(nums, ops, current, ops_needed+1)
	}
}

func equate(equa [][]string) []string {
	var listResult []string
	var eqString string
	var test = make(map[string]float64) // Test is a temporary lookup table for each set of numbers
	for _, item := range equa {         // equa = [[1,2,+,3,+] [1,2,+,3-] etc.]
		var eq []string
		for _, term := range item { // item = [1,2,+,3,+]
			var temp []string
			_, err := strconv.Atoi(term) // Attempt to convert term to int
			if err == nil {
				eq = append(eq, term) // Append term to eq if int i.e. [1,2]
			} else {
				temp = append(temp, eq[len(eq)-2], eq[len(eq)-1], term) // Create postfix equation [1,2,+]
				eq = eq[:len(eq)-2]                                     // Remove last two elements from eq. Setting to nil will break everything

				if term == "+" || term == "*" { // Turn postfix equation into standardised string for key
					eqString = SortString(temp)
				} else {
					eqString = strings.Join(temp, ",")
				}

				if (temp[2] == "/" || temp[2] == "*") && (temp[1] == "1") { // Ignores equations that x/1 or x*1
					eq = append(eq, temp[0])
					continue
				}

				if temp[2] == "*" && temp[0] == "1" { // Ignores equations that 1*x
					eq = append(eq, temp[1])
					continue
				}

				// if val, ok := test[eqString]; ok { // IF a set of numbers has already done an equation, don't add to solution list
				// 	if isIntegral(val) && val > 0 { // i.e. 100 + 1 might be done if other different equations
				// 		v := fmt.Sprint(val)
				// 		eq = append(eq, v)
				// 		continue
				// 	} else {
				// 		break
				// 	}
				// }

				if val, ok := sub[eqString]; ok { // If value for key exists, use the value. Huge save on comp. time
					v := fmt.Sprint(val)
					test[eqString] = val
					if isIntegral(val) && val > 0 {
						if val > 100 && val < 1000 {
							listResult = append(listResult, []string{v}...)
						}
						eq = append(eq, v)
					} else {
						break
					}
				} else { // If value doesn't exist, compute it and add it to dict.
					expression, _ := gorpn.New(eqString)
					result, _ := expression.Evaluate(nil)
					sub[eqString] = result
					test[eqString] = result
					rs := fmt.Sprint(result)
					if isIntegral(result) && result > 0 {
						if result > 100 && result < 1000 {
							listResult = append(listResult, []string{rs}...)
						}
						eq = append(eq, rs)
					} else {
						break
					}
				}
			}
		}
	}
	return listResult
}

func isIntegral(val float64) bool {
	return val == float64(int(val))
}

func SortString(w []string) string {
	sort.Sort(sort.Reverse(sort.StringSlice(w))) // Reversed so the RPN import can be used
	return strings.Join(w, ",")
}
