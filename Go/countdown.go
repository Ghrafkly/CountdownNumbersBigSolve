package main

import (
	"fmt"
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
	comb := itertools.CombinationsStr(number, 3)

	for item := range comb {
		var strSlc string = strings.Join(item[:], ",") // Turns slice into string to create unique key
		if _, value := allKeys[strSlc]; !value {
			allKeys[strSlc] = true
			cNums = append(cNums, [][]string{item}...)
		}
	}

	// Deals with duplicates for Permutations
	for _, item := range cNums {
		if multiply(item) { // If all the numbers multiplied > 101 use the numberset
			var pNums [][]string
			permKeys := make(map[string]bool)
			perm := itertools.PermutationsStr(item, len(item))
			for x := range perm {
				var permSlc string = strings.Join(x[:], ",") // Turns slice into string to create unique key
				if _, value := permKeys[permSlc]; !value {
					permKeys[permSlc] = true
					pNums = append(pNums, [][]string{x}...)
				}
			}
			for _, item := range pNums {
				var current []string
				rpn(item, operators, current, ops_needed)
			}
			sol = append(sol, []string(equate(equations))...)
			for _, v := range sol {
				i, _ := strconv.Atoi(v)
				threeDigits[i] += 1
			}
			sol = nil
			equations = nil
		}
	}

	var keys []int
	for k := range threeDigits {
		keys = append(keys, k)
	}
	sort.Ints(keys)
	for _, k := range keys {
		fmt.Printf("Key: %v, Value: %v\n", k, threeDigits[k])
	}

	elapsed := time.Since(start)
	fmt.Printf("Elapsed: %v\n", elapsed)

	// file, err := os.Open("GoNumbers.csv")
	// if err != nil {
	// 	panic(err)
	// }
	// defer file.Close()
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

	if len(nums) > 0 {
		v := nums[len(nums)-1]       // Save pop value
		nums = nums[:len(nums)-1]    // Pop last element
		current = append(current, v) // Push element
		rpn(nums, ops, current, ops_needed+1)
		current = current[:len(current)-1] // These are reached
		nums = append(nums, v)
	}
}

func equate(equations [][]string) []string {
	var listResult []string
	var eqString string
	for _, item := range equations {
		var eq []string
		var temp []string
		for _, term := range item {
			_, err := strconv.Atoi(term)
			if err == nil {
				eq = append(eq, term)
			} else {
				temp = append(temp, eq[len(eq)-2], eq[len(eq)-1], term)
				eq = eq[:len(eq)-2]

				tempCopy := make([]string, len(temp))
				copy(tempCopy, temp)

				if term == "+" || term == "*" {
					eqString = SortString(tempCopy)
				} else {
					eqString = strings.Join(temp, "")
				}

				////// Comment the below block in to see the changes //////
				// if val, ok := sub[eqString]; ok {
				// 	v := fmt.Sprint(val)
				// 	if isIntegral(val) && val > 0 {
				// 		if val > 100 && val < 1000 {
				// 			listResult = append(listResult, []string{v}...)
				// 		}
				// 		eq = append(eq, v)
				// 	} else {
				// 		break
				// 	}
				// 	temp = nil
				// 	continue
				// }
				///////////////////////////////////////////////////////////

				var calc string = strings.Join(temp, ",")
				expression, err := gorpn.New(calc)
				if err != nil {
					panic(err)
				}

				result, err := expression.Evaluate(nil)
				if err != nil {
					panic(err)
				} else {
					sub[eqString] = result
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
				temp = nil
			}
		}
	}
	return listResult
}

func isIntegral(val float64) bool {
	return val == float64(int(val))
}

func multiply(array []string) bool {
	var k []int
	for _, i := range array {
		j, _ := strconv.Atoi(i)
		k = append(k, j)
	}

	result := 1
	for _, v := range k {
		result *= v
	}

	if result > 101 {
		return true
	} else {
		return false
	}
}

func SortString(w []string) string {
	sort.Strings(w)
	return strings.Join(w, "")
}
