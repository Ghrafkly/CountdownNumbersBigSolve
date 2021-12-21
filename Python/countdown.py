from itertools import permutations, combinations

class Calculations:
    def __init__(self):
        pass

    def rpn(self, equation_list: list, var_stack: list, available_ops: set, current_eq_stack: list, ops_needed: int = -1):
        if not ops_needed and not var_stack: # if ops_needed != 0 and len(var_stack) > 0
            equation_list.append(tuple(current_eq_stack))

        if ops_needed > 0:
            for op in available_ops:
                current_eq_stack.append(op)
                self.rpn(equation_list, var_stack, available_ops, current_eq_stack, ops_needed - 1)
                current_eq_stack.pop()

        if var_stack:
            var = var_stack.pop()
            current_eq_stack.append(var)
            self.rpn(equation_list, var_stack, available_ops, current_eq_stack, ops_needed + 1)
            current_eq_stack.pop()
            var_stack.append(var)
    
    def calculate(self, equation: list):
        stack = []
        dupeParEq = set()
        for aqua in equation: # equation = [(75, 10, '+', 7, '+'), (75, 10, '+', 7, '-'), (75, 10, '+', 7, '*')...]
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
                            exp = self.equate(sm[0], sm[1], term)
 
                            match exp:
                                case 'skip':
                                    break
                                case _:
                                    a = tuple(sorted(smList))
                                    if a not in dupeParEq:
                                        if 100 < exp < 1000:
                                            dict[exp] += 1
                                        dupeParEq.add(a)
                                    stack.insert(0, exp)

            stack.clear() # Reset stack for next intermediate equation
        equation.clear() # Reset equation for next equation set
    
    def equate(self, a: int, b: int, term: str):
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
    ds = set()
    n = sorted(combinations(numbers, tileSetSize)) # sorted() and .sort() work just as fast here as it is early in the code
    
    for item in n:
        dupeNumSet.add(item)

    for item in dupeNumSet:
        calculations = Calculations()
        for variable_permutation in permutations(item):
            if variable_permutation not in ds: # 1,1,2 and 1,1,2 are valid. This stops that.           
                calculations.rpn(equations, list(variable_permutation), set(ops), []) # 0.02s @ 6 numbers
                ds.add(variable_permutation)
        # calculations.calculate(equations)

    print(len(equations))
        
    with open('numbers.csv', 'w') as file:
        for key in dict.keys():
            file.write(str(key) + "," + str(dict[key]) + '\n')
    
if __name__ == "__main__":
    # numbers = [1,1,2,2,3,3,4,4,5,5,6,6,7,7,8,8,9,9,10,10,25,50,75,100] # All the numbers in the Countdown rules
    numbers = [5,10,25] # All the numbers in the Countdown rules
    ops = ['+', '-', '*', '/']
    tileSetSize = 3 # Change this unless you have a v. powerful computer
    equations = []
    dupeNumSet = set()

    dict = {}
    keys = range(101, 1000, 1)

    for i in keys:
        dict[i] = 0
    main()