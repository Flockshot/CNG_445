# Q1)
print(" ".join([x.capitalize() for x in input("Enter a string: ").split(" ")]))

# Q2)
stringInput = input("Enter a string: ")
charCount = {}
for char in stringInput:
    charCount[char] = charCount.get(char, 0) + 1

print(charCount)

