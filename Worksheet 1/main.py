a_str = "acd"
print(a_str[1])

# a_str[1] = 'b'
print(a_str)
# a_str is an immutable object, so it cannot be changed element by element

a_list = [1, 3, 2, 4]
a_list[1] = 2
print(a_list)
# a_list is a mutable object, so it can be changed element by element

row1 = ["H", "He"]
row2 = ["Li", "Be", "F", "Ar"]
row3 = ["Na", "Mg", "Cl", "Ne"]

ptable = row1
ptable.extend(row2)
ptable.extend(row3)

print(ptable)
print(row1)

# 2a) What is the value of ptable now?
# ['H', 'He', 'Li', 'Be', 'F', 'Ar', 'Na', 'Mg', 'Cl', 'Ne']

# What is the value of row1 now? Is this what you expected?
# ['H', 'He', 'Li', 'Be', 'F', 'Ar', 'Na', 'Mg', 'Cl', 'Ne']
# Yes, this is what I expected

# Correct the error in row2 (Ar should be Ne) by executing a command of the form row2[?] = ?.
# What happens to ptable as a result of this assignment?
row2[3] = "Ne"
print(ptable)
# ptable is not affected by this assignment

# Correct the error in row3 (Ne should be Ar) by executing a command of the form ptable[?] = ?.
# What happens to row3 as a result of this assignment?
ptable[9] = "Ar"
print(row3)
print(ptable)
# row3 is not affected by this assignment





