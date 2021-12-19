package main

import (
	"fmt"
	// "sort"
	"github.com/ernestosuarez/itertools"
)

func main() {
	// var ops = [4]string{"+", "-", "*", "/"}
	var number = []int{1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 25, 50, 75, 100}
	var s [][]int
	allKeys := make(map[[2]int]bool)

	list := itertools.CombinationsInt(number, 6)
	for item := range list {
		fmt.Printf("%v\n", item)
		if _, value := allKeys[item]; !value {
			allKeys[item] = true
			s = append(s, [][]int{item}...)
		}
	}

	// var dupe = duplicate(s)
	// fmt.Printf("S: %v\n", len(s))
	// fmt.Printf("D: %v\n", len(dupe))

}
