import numpy as np
from itertools import permutations, product, combinations_with_replacement
import re

tileSetSize = 4 # Specifies the size of the tileset

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

    def rpn(self, variables):
        ops = ['+', '-', '*', '/']
        opnumber = tileSetSize-2
        equations = []
        i = 0
        valid = 0
        invalid = 0

        for n1, n2, *nums in permutations(variables):
            nums += ["%s"] * opnumber
            for p in {*permutations(nums)}:
                for operators in product(ops, repeat = opnumber):
                    for last in ops:
                        equations.append((" ".join((n1, n2, *p, last)) % operators))

        print("Total Equations: " + str(len(equations)))

        #### Stack is in the wrong order ####
        while i < 2:
            eq = (equations[i]).split()
            stack = []
            sm = 0

            for term in eq:
                if term.isdigit():
                    stack.insert(0, int(term))
                else:
                    sm = (f'{stack.pop(-1)} {term} {stack.pop(-1)}')
                    if eval(sm) > 0 and float(eval(sm)).is_integer():
                    # if sm >= 0 and float(sm).is_integer():
                        stack.insert(0, sm)
                    else:
                        invalid += 1
                        break
            i += 1
            stack.clear()
        
        print("Invalid Equations: " + str(invalid))

def main():
    sn = StoreNumber()
    i = 0
    k = 0
    while i < 1: # Determines the number of tilesets
        sn.tiles()
        i += 1

    print("Final equations:")

    while k < len(sn.printSet()):
        calculations = Calculations()
        calculations.rpn(map(str, list(sn.printSet())[k]))
        k += 1
    
    print("Tilesets: " + str(list(sn.printSet())))
    print("Number of tilesets: " + str(i))
    
if __name__ == "__main__":
    main()