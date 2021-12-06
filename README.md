# CountdownNumbersBigSolve
 
*Aim to create a graph of all the solutions for numbers between 101-999 using the Countdown/Letters and Numbers rules*

## Rules
1. 24 numbers are available to use: [1,1,2,2,3,3,4,4,5,5,6,6,7,7,8,8,9,9,10,10,25,50,75,100]
2. 6 numbers are selected (without replacement) 24C6.
3. Using the 6 selected numbers reach a 3-digit number using basic arithmetic [+, *, -, /]
5. Not all digits need to be used
6. Cocatenation is not allowed (2 + 2 = 22)
7. At no intermidate step in the process can the current running total negative or invlove decimal places
8. Each numbered tile can only be used once

**Duplicates are handled throughout the process to reduce redudant and duplicate equations**

The variable `tileSetSize` is used to determine how many numbers are 'selected' i.e. when it is set to 4 it will select 4 numbers. 

*Recommended to use no more than 4 to test the code*

---
## Current code process
1. Generate all possible 24Cn (where n = `tileSetSize`) then,
2. Generate all possible permutations for each selected set of numbers i.e. 1,2,3 and 3,2,1 and 1,3,2 etc.
3. For each permutation generated create all possible postfix notation equations using basic arithmetic
4. Once all the postfix has been generated for all possible permutations of one set of numbers, calculate.
5. For each valid 3 digit answer iterate a counter in a dictionary with the appropiate key (101-999)
6. Return to Step 2. and repeat until all possible selection of numbers are exhausted.
---
## Postfix Notation (Reverse Polish Notation)
Postfix Notation is a method of calculating equations that removes the ambiguity of brackets.

For valid postfix notation the number of operators should never equal or greater than the number of numbers preceding.

i.e. 
1. (2 10 + 75 -) ✔ 
2. (2 + 10 75 -) ❌