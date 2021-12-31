package main

import (
	"fmt"
	"strings"

	// https://pkg.go.dev/github.com/karrick/gorpn#ErrBadBindingType
	// https://github.com/karrick/gorpn
	"github.com/ernestosuarez/itertools"
)

var equations [][]string

func main() {
	var operators = []string{"+", "-", "*", "/"}
	// var number = []string{"1", "1", "2", "2", "3", "3", "4", "4", "5", "5", "6", "6", "7", "7", "8", "8", "9", "9", "10", "10", "25", "50", "75", "100"}
	var number = []string{"5", "10", "25"}
	var ops_needed int = -1

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
			fmt.Printf("Equations: %v\n", equations)
		}
	}
}

func rpn(nums []string, ops []string, current []string, ops_needed int) {
	if ops_needed == 0 && len(nums) == 0 {
		fmt.Printf("Current: %v\n", current)
		equations = append(equations, [][]string{current}...)
	}

	if ops_needed > 0 {
		for _, op := range ops {
			current = append(current, op)
			rpn(nums, ops, current, ops_needed-1)
			current = current[:len(current)-1]
		}
	}

	if len(nums) > 0 {
		v := nums[len(nums)-1]
		nums = nums[:len(nums)-1]
		current = append(current, v)
		rpn(nums, ops, current, ops_needed+1)
		current = current[:len(current)-1]
		nums = append(nums, v)
	}
}

// a := nums[len(nums)-1]  // Save pop value
// b := nums[:len(nums)-1] // Pop last element
// b = append(b, a) // Push element
