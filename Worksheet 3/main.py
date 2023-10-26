# Q1)
print(" ".join([x.capitalize() for x in input("Enter a string: ").split(" ")]))

# Q2)
stringInput = input("Enter a string: ")
charCount = {}
for char in stringInput:
    charCount[char] = charCount.get(char, 0) + 1

print(charCount)


# Q4)

stringInput = input("Enter a string: ")
n = len(stringInput)
k = -1
while k > n or k < 0:
    k = int(input("Enter k: "))

t = [stringInput[i:i + k] for i in range(0, n, k)]

for single_t in t:
    t_chars = {}
    for char in single_t:
        if char not in t_chars:
            print(char, end="")
            t_chars[char] = True
    print("")

