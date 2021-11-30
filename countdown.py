from itertools import permutations, combinations

numbers = [1,1,2,2,3,3,4,4,5,5,6,6,7,7,8,8,9,9,10,10,25,50,75,100] # All the numbers in the Countdown rules
ops = ['+', '-', '*', '/']
tileSetSize = 4 # Change this unless you have a v. powerful computer
equations = []
dupeNumSet = set()

dict = {}
keys = range(101, 1000, 1)

for i in keys:
    dict[i] = 0

class StoreNumber:
    def __init__(self):
        pass

    def tiles(self): # Sort the generated list then add to set. This avoids numbersets that have the same numbers but different order.
        n = sorted(combinations(numbers, tileSetSize)) # sorted() and .sort() work just as fast here as it is early in the code
        for item in n:
            dupeNumSet.add(item)

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

        for aqua in equation:
            eq = [str(int) for int in aqua]
            for term in eq:
                if term.isdigit():
                    stack.insert(0, int(term))
                else:
                    sm = stack.pop(-1), stack.pop(-1), term
                    smList = [str(int) for int in sm]
                    if (term == '/' and sm[1] == 1) or (term == '*' and sm[1] == 1): # x / 1 and x * 1
                        stack.insert(0, sm[0])
                    elif (term == '/' and sm[0] == 1) or (term == '*' and sm[0] == 1): # 1 * x and 1 / x
                        stack.insert(0, sm[1])
                    else:
                        exp = self.equate(sm[0], sm[1], term)
                        if exp != 'skip':
                            a = tuple(sorted(smList))
                            if a not in dupeParEq:
                                if 100 < exp < 1000:
                                    dict[exp] += 1
                                dupeParEq.add(a)
                            stack.insert(0, exp)
                        else:
                            break
            stack.clear() # Reset stack for next intermediate equation
        equation.clear() # Reset equation for next equation set
    
    def equate(self, a: int, b: int, term: str): # Faster than eval() ¯\_(ツ)_/¯
        c = 0
        if term == '+':
            c = a+b
        elif term == '*':
            c = a*b
        elif term == '-':
            c = a-b
        elif term == '/':
            c = a/b

        if (float(c).is_integer()) and (c > 0): # At all stages the sum needs to be greater than 0 and an integer
            return(int(c))
        else:
            return('skip')
                       
def main():
    sn = StoreNumber()
    ds = set()
    sn.tiles() # Generates master list of equations. Stored in dupeNumSet


    for item in dupeNumSet:
        calculations = Calculations()
        for variable_permutation in permutations(item):
            if variable_permutation not in ds:
                calculations.rpn(equations, list(variable_permutation), set(ops), [])
                ds.add(variable_permutation)
        calculations.calculate(equations)
    
    with open('numbers.csv', 'w') as file:
        for key in dict.keys():
            file.write(str(key) + "," + str(dict[key]) + '\n')
    
if __name__ == "__main__":
    main()