import numpy as np
from itertools import permutations, product, combinations_with_replacement
import re

tileSetSize = 3 # Specifies the size of the tileset

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
        equations = set()
        remove = set()

        for n1, n2, *nums in permutations(variables):
            nums += ["%s"]*opnumber
            for p in {*permutations(nums)}:
                for operators in product(ops, repeat=opnumber):
                    for last in ops:
                        equations.add("".join((n1,n2,*p,last)) % operators)

        print("Before clean: " + str(len(equations)))                

        # Reduce commutative equivalents: ca*a-b/ same as ac*a-b/
        for equation in equations:
            if equation not in remove:
                for match in re.finditer(r"(?=(.+)(\w)[+*])", equation):
                    a, _ = match.span(1)
                    _, d = match.span(2)
                    equivalent = equation[:a] + match[2] + match[1] + equation[d:]
                    if equivalent != equation and equivalent in equations:
                        remove.add(equivalent)
        equations -= remove

        print("After clean: " + str(len(equations)))

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