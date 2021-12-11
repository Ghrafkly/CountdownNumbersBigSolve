from itertools import permutations, combinations
import numpy as np

def rpn(eqList: list, varStack: list, avOps: set, currEq: list, neededOps: int = -1):
    if not neededOps and not varStack: # if neededOps != 0 and len(varStack) > 0
        eqList.append(tuple(currEq))

    if neededOps > 0:
        for op in avOps:
            currEq.append(op)
            rpn(eqList, varStack, avOps, currEq, neededOps - 1)
            currEq.pop()

    if varStack:
        var = varStack.pop()
        currEq.append(var)
        rpn(eqList, varStack, avOps, currEq, neededOps + 1)
        currEq.pop()
        varStack.append(var)

def calculate(equation: list):
    stack = []
    dupeParEq = set()

    for aqua in equation:
        for term in aqua:
            if type(term) == int:
                stack.insert(0, int(term))
            else:
                sm = [stack.pop(-1), stack.pop(-1), term]
                smList = [str(int) for int in sm]

                match sm:
                    case [1, _, '/'|'*']: # 1 / or * x
                        stack.insert(0, sm[1])
                    case [_, 1, '/'|'*']: # x / or * 1
                        stack.insert(0, sm[0])
                    case _:
                        exp = equate(sm[0], sm[1], term)
                        match exp:
                            case 'skip':
                                break
                            case _:
                                if 100 < exp < 1000:
                                    dict[exp] += 1
                                stack.insert(0, exp)
                                # a = tuple(sorted(smList))
                                # print(a)
                                # if a not in dupeParEq:
                                #     if 100 < exp < 1000:
                                #         dict[exp] += 1
                                #     dupeParEq.add(a)
                                # stack.insert(0, exp)

        stack.clear() # Reset stack for next intermediate equation

def equate(a: int, b: int, term: str): # Faster than eval() ¯\_(ツ)_/¯
    c = 0
    match term:
        case '+':
            c = a+b
        case '*':
            c = a*b
        case '-':
            c = a-b
        case '/':
            c = a/b

    if ((c%1) == 0) and (c > 0): # At all stages the sum needs to be greater than 0 and an integer
        return(int(c))
    else:
        return('skip')

def main():
    n = permutations(numbers, 3) # Generate 24C4
    for item in n:
        dupeNumSet.add(item) # Eliminate duplicates
    
    for item in dupeNumSet:
        rpn(equations, list(item), set(ops), [])

    calculate(equations)

    with open('numbers2.csv', 'w') as file:
        for key in dict.keys():
            file.write(str(key) + "," + str(dict[key]) + '\n')

if __name__ == "__main__":
    numbers = [1,1,2,2,3,3,4,4,5,5,6,6,7,7,8,8,9,9,10,10,25,50,75,100] # All the numbers in the Countdown rules
    ops = ['+', '-', '*', '/']
    equations = []
    dupeNumSet = set()

    dict = {}
    keys = range(101, 1000, 1)

    for i in keys:
        dict[i] = 0
    main()