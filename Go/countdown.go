package main

import (
	"fmt"
	"strings"

	"github.com/ernestosuarez/itertools"
)

func main() {
	var number = []string{"1", "1", "2", "2", "3", "3", "4", "4", "5", "5", "6", "6", "7", "7", "8", "8", "9", "9", "10", "10", "25", "50", "75", "100"}
	// var ops = [4]string{"+", "-", "*", "/"}

	// Creates a dict of all 3 digit nums
	threeDigits := make(map[int]int)
	for i := 101; i < 1000; i++ {
		threeDigits[i] = 0
	}

	// Deals with duplicates
	var s [][]string
	allKeys := make(map[string]bool)
	list := itertools.CombinationsStr(number, 3)
	for item := range list {
		var strSlc string = strings.Join(item[:], " ")
		if _, value := allKeys[strSlc]; !value {
			allKeys[strSlc] = true
			s = append(s, []string{strSlc})
		}
	}
	fmt.Printf("S: %T\n", s)
}
