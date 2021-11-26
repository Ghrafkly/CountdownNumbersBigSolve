import numpy as np
from itertools import permutations

tileSetSize = 3
ops = ['+', '-', '*', '/']
equations = []
eqCalc = list()

class StoreNumber:
    def __init__(self):
        self.setOf = set()

    def tiles(self):
        numbers = [1,1,2,2,3,3,4,4,5,5,6,6,7,7,8,8,9,9,10,10,25,50,75,100] # All the numbers in the Countdown rules
        numbers_6 = list(np.random.choice(numbers, size=tileSetSize, replace = False)) # Generate how many numbers per tile/numberset
        self.setOf.add(tuple(sorted(numbers_6))) # Sort the generated list then add to set. This avoids numbersets that have the same numbers but different order.

    def printSet(self):
        return self.setOf

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
    
    def calculate(self, equation):
        stack = []
        dupeIntEq = set()
        dupeSum = set()
 
        for aqua in equation:
            for term in aqua:
                if term.isdigit():
                    stack.insert(0, int(term))
                else:
                    eq = (f'{stack.pop(1)} {term} {stack.pop(0)}') # Generates an equation based on the stack i.e. 1 + 2 (where stack is 1 2 +)
                    a = eq.split()

                    if (term == '/' and a[2] == 1) or (term == '*' and a[2] == 1): # x / 1 and x * 1
                        stack.insert(0, a[0])
                    elif (term == '/' and a[0] == 1) or (term == '*' and a[0] == 1): # 1 * x and 1 / x
                        stack.insert(0, a[2])
                    else:
                        exp = eval(eq)

                        if exp > 0 and float(exp).is_integer(): # Checks if the equation is greater than 0 and is a whole number
                            if (str(a) in dupeIntEq):
                                stack.insert(0, int(exp)) # Inserts result back into the stack
                            else:
                                if (term == '+') or (term == '*'): # Deals with commutative equations
                                    a.sort()
                                dupeIntEq.add(str(a)) # Add intermidiate equation to set
                                
                                if exp in dupeSum:
                                    pass
                                else:
                                    if 100 < exp < 999:
                                        eqCalc.append(int(exp))
                                        
                                        # deal with partial summs


                                    dupeSum.add(exp)

                                stack.insert(0, exp)
                        else:
                            break
                        
                        # if exp > 0 and float(exp).is_integer(): # Checks if the equation is greater than 0 and is a whole number                          
                        #     if exp in dupeSum:
                        #         pass
                        #     else:
                        #         if 100 < exp < 999:
                        #             eqCalc.append(int(exp))
                        #         dupeSum.add(exp)
                        #         # print(dupeSum)
                        #     stack.insert(0, exp)
                        # else:
                        #     break
        equation.clear()
        return(eqCalc)

class NumSolutions:
    def __init__(self):
        pass

    def counter(self, sums):
        print(sums)
                       
def main():
    sn = StoreNumber()
    ns = NumSolutions()
    i = 0
    k = 0

    while i < 1: # Determines the number of tilesets
        sn.tiles()
        i += 1

    while k < len(sn.printSet()):
        calculations = Calculations()
        # variables = [str(x) for x in list(sn.printSet())[k]]
        # print(variables)
        variables = ['25', '100', '75', '50']
        for variable_permutation in permutations(variables):
            calculations.rpn(equations, list(variable_permutation), set(ops), [])
        result = calculations.calculate(equations)
        k += 1
    ns.counter(sorted(result))
   
if __name__ == "__main__":
    main()