package main

import (
	"fmt"

	"github.com/veryfunny/generator"
)

func main() {
	var numbers = [24]int8{1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 25, 50, 75, 100}
	var ops = [4]string{"+", "-", "*", "/"}

	generator.Generator()
	fmt.Println("hello world")
}
