from itertools import permutations, product

variables = ['100', '50', '10']
ops = ['+', '-', '*', '/']
# opnumber = len(variables)-2 # Pre
opnumber = len(variables)-1 # Post
equations = []
invalid = 0
coun = 0

for nums in permutations(variables):
    for operators in product(ops, repeat = opnumber):
        nums += operators
        print(nums)
        nums = tuple
        # for p in permutations(nums):
        #     eqCheck = (" ".join(p)).split()
        #     if (eqCheck[0].isdigit() and eqCheck[1].isdigit() and (eqCheck[-1].isdigit() != True)):
        #         for x in eqCheck:
        #             if x.isdigit():
        #                     coun += 1
        #             else:
        #                 coun -= 1
        #                 if coun == 0:
        #                     break
        #         if coun == 1:
        #             equations.append(eqCheck)
        #             coun = 0

print(len(equations))




# for nums in permutations(variables):
#     nums += tuple(("%s",)) * opnumber

# for p in permutations(nums):
#     for operators in product(ops, repeat = opnumber):
#         eqCheck = (" ".join(p) % operators).split()
#         if (eqCheck[0].isdigit() and eqCheck[1].isdigit() and (eqCheck[-1].isdigit() != True)):
#             for x in eqCheck:
#                 if x.isdigit():
#                         coun += 1
#                 else:
#                     coun -= 1
#                     if coun == 0:
#                         break
#             if coun == 1:
#                 equations.append(eqCheck)
#                 coun = 0

# print(len(equations))

# for n1, n2, *nums in permutations(variables):
#     nums += ["%s"] * opnumber
#     for p in {*permutations(nums)}:
#         for operators in product(ops, repeat = opnumber):
#             for last in ops:
#                 eqCheck = (" ".join((n1, n2, *p, last)) % operators).split()
#                 for x in eqCheck:
#                     if x.isdigit():
#                         coun += 1
#                     else:
#                         coun -= 1
#                         if coun == 0:
#                             break
#                 if coun == 1:
#                     equations.append(eqCheck)
#                     coun = 0

# print("Total Equations: " + str(len(equations)))

#### Postfix must be n numbers in a row then up to n-1 ops in a row ####
# for eq in equations:
#     stack = []
#     sm = 0
#     for term in eq:
#         if term.isdigit():
#             stack.insert(0, int(term))
#         else:
#             sm = (f'{stack.pop(1)} {term} {stack.pop(0)}') # Generates an equation based on the stack i.e. 1 + 2 (where stack is 1 2 +)
        
#             divide_multiply = sm.split()
            
#             # If the equation is divided/multiplied by one, skip evaluating i.e. 2*1 = 2 or 2/1 = 2
#             if (divide_multiply[1] == '/' and divide_multiply[2] == 1) or (divide_multiply[1] == '*' and divide_multiply[2] == 1):
#                 stack.insert(0, divide_multiply[0])
#                 break
#             exp = eval(sm)                   
                
#             if exp > 0 and float(exp).is_integer(): # Checks if the equation is greater than 0 and is a whole number
#                 stack.insert(0, exp) # Inserts result back into the stack
#             else:
#                 invalid += 1
#                 break
#     stack.clear() # Wipes the stack so the next RPN can be done

# print("Valid Equations: " + str((len(equations)) - (invalid)))
# print("Invalid Equations: " + str(invalid))