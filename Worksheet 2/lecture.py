import copy

a = [1, 2, 3, 4, 5]
a.insert(2, 10)
print(a)
print(a.count(4))

# last index not included
print(a[1:3])

# first and last index optional.
print(a[:3])
print(a[1:])
print(a[:])

# with step size
print(a[::2])
print(a[::-1])

a = [2, 4, 3, [5, 6]]
# shallow copy, if [5,6] list is changed in b, it will also change in a
b = a[1:]
print(b)

# deep copy, if [5,6] list is changed in b, it will not change in a
b = copy.deepcopy(a)
print(b)

# example of shallow copy
a = [1, 2, 3, [4, 5]]
b = list(a)

a[-1].append(6)

print(a)
print(b)

c = ["Y", "Z", "x", "z", "D", "A"]
c.sort(key=lambda x: ord(x) if x.islower() else ord(x) + 100)
print(c)

d = [(4, 5), (1, 2), (3, 4), (2, 3)]
# sort by first element, if first element is same then sort by second element
# the syntax is below, use () to define what to sort by and which to look in case of tie
d.sort(key=lambda x: (x[1], x[0]))
print(d)
