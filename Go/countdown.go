package main

import (
	"fmt"

	"github.com/ernestosuarez/itertools"
)

func main() {
	// var ops = [4]string{"+", "-", "*", "/"}
	var number = []int{1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 25, 50, 75, 100}
	var s [][]int
	allKeys := make(map[[2]int]bool)

	list := itertools.CombinationsInt(number, 2)
	for item := range list {
		if _, value := allKeys[item]; !value {
			allKeys[item] = true
			s = append(s, [][]int{item}...)
		}
	}

	// var dupe = duplicate(s)
	fmt.Printf("S: %v\n", len(s))
	// fmt.Printf("D: %v\n", len(dupe))

}

// func duplicate(arr [][]int) [][]int {
// 	var result [][]int

// 	for _, e := range arr {
// 		fmt.Println(e)
// 		result = append(result, [][]int{e}...)
// 	}

// 	return result
// }
