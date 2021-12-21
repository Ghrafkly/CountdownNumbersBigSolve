package main

import (
	"fmt"
	"strings"
	"sync"

	// https://pkg.go.dev/github.com/karrick/gorpn#ErrBadBindingType
	// https://github.com/karrick/gorpn
	"github.com/ernestosuarez/itertools"
)

// var equations = NewEmptyStack()
var equations []*Stack

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
			pStack := NewEmptyStack()
			for _, v := range item {
				pStack.Push(v)
			}

			current := NewEmptyStack()
			fmt.Printf("Numbers: %v\n", pStack)
			rpn(pStack, operators, current, ops_needed)
		}
	}
}

func rpn(nums *Stack, ops []string, current *Stack, ops_needed int) {

	if ops_needed == 0 && nums.Size() == 0 {
		for i := 0; i < 5; i++ {
			fmt.Printf("Current Length: %v\n", current.Size())
			current.Pop()
		}
	}

	if ops_needed > 0 {
		for _, op := range ops {
			current.Push(op)
			rpn(nums, ops, current, ops_needed-1)
			current.Pop()
		}
	}

	if nums.Size() != 0 {
		v := nums.Pop()
		current.Push(v)
		rpn(nums, ops, current, ops_needed+1)
		current.Pop()
		nums.Push(v)
	}
}

// Item interface to store any data type in stack
type Item interface{}

// Stack struct which contains a list of Items
type Stack struct {
	items []Item
	mutex sync.Mutex
}

// NewEmptyStack() returns a new instance of Stack with zero elements
func NewEmptyStack() *Stack {
	return &Stack{
		items: nil,
	}
}

// NewStack() returns a new instance of Stack with list of specified elements
func NewStack(items []Item) *Stack {
	return &Stack{
		items: items,
	}
}

// Push() adds new item to top of existing/empty stack
func (stack *Stack) Push(item Item) {
	stack.mutex.Lock()
	defer stack.mutex.Unlock()

	stack.items = append(stack.items, item)
}

// Pop() removes most recent item(top) from stack
func (stack *Stack) Pop() Item {
	stack.mutex.Lock()
	defer stack.mutex.Unlock()

	if len(stack.items) == 0 {
		return nil
	}

	lastItem := stack.items[len(stack.items)-1]
	stack.items = stack.items[:len(stack.items)-1]

	return lastItem
}

// Size() returns the number of items currently in the stack
func (stack *Stack) Size() int {
	stack.mutex.Lock()
	defer stack.mutex.Unlock()

	return len(stack.items)
}

// Top() returns the last inserted item in stack without removing it.
func (stack *Stack) Top() Item {
	stack.mutex.Lock()
	defer stack.mutex.Unlock()

	if len(stack.items) == 0 {
		return nil
	}

	return stack.items[len(stack.items)-1]
}

// IsEmpty() returns whether the stack is empty or not (boolean result)
func (stack *Stack) IsEmpty() bool {
	stack.mutex.Lock()
	defer stack.mutex.Unlock()

	return len(stack.items) == 0
}
