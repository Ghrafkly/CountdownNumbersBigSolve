package main

import (
	"fmt"
	"strings"

	"github.com/ernestosuarez/itertools"
)

func main() {
	// var ops = [4]string{"+", "-", "*", "/"}
	// var number = []int{1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 25, 50, 75, 100}
	var number = []string{"1", "1", "2", "2", "3", "3", "4", "4", "5", "5", "6", "6", "7", "7", "8", "8", "9", "9", "10", "10", "25", "50", "75", "100"}
	var s [][]string

	allKeys := make(map[string]bool)

	list := itertools.CombinationsStr(number, 4)
	for item := range list {
		var strSlc string = strings.Join(item[:], " ")

		if _, value := allKeys[strSlc]; !value {
			allKeys[strSlc] = true
			s = append(s, []string{strSlc})
		}

	}
	fmt.Printf("S: %v", s)
	
	// fmt.Printf("I: %v, J: %v", i, j)
	// var dupe = duplicate(s)
	// fmt.Printf("S: %v\n", len(s))
	// fmt.Printf("D: %v\n", len(dupe))

}
