from itertools import permutations, combinations
import copy
import time

def rpn(nums: list, ops: list, current: list, ops_needed: int = -1):
    if ops_needed == 0 and len(nums) == 0:
        c = copy.deepcopy(current)
        equations.append(c)
    
    if ops_needed > 0:
        for op in ops:
            current.append(op)
            rpn(nums, ops, current, ops_needed-1)
            current.pop()
    
    if len(nums) > 0:
        var = nums.pop()
        current.append(var)
        rpn(nums, ops, current, ops_needed+1)
        current.pop()
        nums.append(var)

def calculate(equa: list):
    stack, eqString, test = [], '', {}
    for item in equa:
        for term in item:
            if type(term) == int:
                stack.append(term)
            else:
                temp = [stack.pop(-1), stack.pop(-1), term]
                c = [str(int) for int in temp]

                if term == '+' or term == '*':
                    c.sort()
                    eqString = ','.join(c)
                else:
                    eqString = ','.join(c)
                
                match temp:
                    case [1, _, '*']:
                        stack.append(temp[1])
                        continue
                    case [_, 1, '/'|'*']:
                        stack.append(temp[0])
                        continue

                if eqString in test.keys():
                    v = test[eqString]
                    if v:
                        stack.append(v)
                        continue
                    else:
                        break
                
                if eqString in sub.keys():
                    v = sub[eqString]
                    test[eqString] = v
                    if v:
                        if 100 < v < 1000:
                            dict[v] += 1
                        stack.append(v)
                    else:
                        break
                else:
                    exp = equate(temp[1],temp[0], term)
                    sub[eqString] = exp
                    test[eqString] = exp
                    if exp:
                        if 100 < exp < 1000:
                            dict[exp] += 1
                        stack.append(exp)
                    else:
                        break
                
        stack.clear()

def equate(a: int, b: int, term: str):
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

    if (c%1) == 0 and c > 0:
        return int(c)
    else:
        return 0

def main():
    numbers = [1,1,2,2,3,3,4,4,5,5,6,6,7,7,8,8,9,9,10,10,25,50,75,100] # All the numbers in the Countdown rules
    operators = ['+', '-', '*', '/']
    cDupe = set()

    # Deals with duplicates for Combinations
    cNums = sorted(combinations(numbers, 4))
    for item in cNums:
        cDupe.add(item)
    cNums.clear()

    # Deals with duplicates for Permutations
    for item in cDupe:
        pNums = permutations(item)
        perm = set()
        for item in pNums:
            perm.add(item)
        
        for item in perm:
            rpn(list(item), operators, [])
        
        calculate(equations) # Equations gets filled in the rpn function

        equations.clear()

    with open('Python/numbers.csv', 'w') as file:
        for key in dict.keys():
            file.write(str(key) + "," + str(dict[key]) + '\n')

if __name__ == '__main__':
    equations = []
    dict = {}
    sub = {}

    # Creates a dict of all 3 digit numbers. Values set to 0
    keys = range(101, 1000, 1)
    for i in keys:
        dict[i] = 0

    start = time.perf_counter()
    main()
    finish = time.perf_counter()
    print(f'Elapsed: {round(finish-start,2)}s')