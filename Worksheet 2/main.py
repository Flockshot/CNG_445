# 4)
character = input("Enter a character: ").lower()
rotation = int(input("Enter a rotation: "))
rotation = rotation % 26
newASCII = ord(character)+rotation
print(chr(newASCII if newASCII <= 122 else newASCII-26))


# 5)
words = input("Enter 2 words: ").split(" ")
newWord = [words[0][i]+words[1][i] for i in range(len(words[0]))]
print("".join(newWord))


# 6)
firstIndexes = input("Enter first index of the list: ").split(" ")
secondIndexes = input("Enter second index of the list: ").split(" ")
subList = [(firstIndexes[i], secondIndexes[i]) for i in range(len(firstIndexes))]
print(subList)

subList.sort(key=lambda x: (x[1], x[0]), reverse=True)
print(subList)


# 7)
postal = input("Enter your postal code: ")

isValid = 100000 <= int(postal) <= 999999
isAlternating = [postal[i] == postal[i+2] for i in range(len(postal) - 2)]

print(isValid and not any(isAlternating))

# alternative solution

digits = []
temp = 1
while temp !=0:
    digits.append(temp % 10)
    temp = temp//10
print(digits)

check = []

for j in range(0, len(digits)-2):
    check.append(digits[j] == digits[j+2])

print(check.count(True) <= 1 and 100000 <= int(postal) <= 999999)








