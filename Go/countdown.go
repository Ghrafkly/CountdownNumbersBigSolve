package main

import (
	"fmt"
	"strings"

	// https://pkg.go.dev/github.com/karrick/gorpn#ErrBadBindingType
	// https://github.com/karrick/gorpn
	"github.com/ernestosuarez/itertools"
)

func main() {
	var number = []string{"1", "1", "2", "2", "3", "3", "4", "4", "5", "5", "6", "6", "7", "7", "8", "8", "9", "9", "10", "10", "25", "50", "75", "100"}

	// Creates a dict of all 3 digit numbers
	threeDigits := make(map[int]int)
	for i := 101; i < 1000; i++ {
		threeDigits[i] = 0
	}

	// Deals with duplicates
	var s [][]string
	var nums [][]string
	allKeys := make(map[string]bool)
	list := itertools.CombinationsStr(number, 3)

	for item := range list {
		var strSlc string = strings.Join(item[:], " ")
		if _, value := allKeys[strSlc]; !value {
			allKeys[strSlc] = true
			s = append(s, []string{strSlc})
			nums = append(nums, [][]string{item}...)
		}
	}

	for _, item := range nums {
		var t [][]string
		permKeys := make(map[string]bool)
		perm := itertools.PermutationsStr(item, len(item))
		for x := range perm {
			var permSlc string = strings.Join(x[:], " ")
			if _, value := permKeys[permSlc]; !value {
				permKeys[permSlc] = true
				t = append(t, []string{permSlc})
			}
		}
		equations := rpn(t)
		fmt.Println(equations)
	}
}

func rpn(nums [][]string) int {
	// var ops = [4]string{"+", "-", "*", "/"}
	var j int
	for x := range nums {
		fmt.Println(x)
		j++

	}
	return j
}
