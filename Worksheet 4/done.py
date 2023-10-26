import os
import re
import random



# 1a)
s = "/home/eraslan/445/2018/prj/project.py"
path = re.split("/", s)
print(path[-1])

# 1b)
pathWithoutFile = path[1:-1]
print(pathWithoutFile)

# 1c)
s = "I doon't waaaant to haaave aannny eeexxaaam"
withoutRepetition = re.sub("a+", "a", s)
print(withoutRepetition)


# 2)
ssn = input("Enter SSN: ")
while not re.match("^\d{9}$|^\d{3}-\d{2}-\d{4}$", ssn):
    ssn = input("Enter SSN: ")


# 3)
numList100 = []

for x in range(100):
    numList100.append(random.randrange(1, 101))

toFind = int(input("Enter the number to find index of: "))
try:
    print(numList100.index(toFind))
except ValueError:
    print("Not found")


# 4)
filePath = input("Enter the file path: ")
file = open(filePath, "r")
counter = {}
wordsInFile = file.read().lower().replace("\n", " ").split(" ")

for word in wordsInFile:
    counter[word] = counter.get(word, 0) + 1

print(counter)


# 5)
folderPath = input("Enter the folder path: ")

for file in os.listdir(folderPath):
    extension = file.split(".")[-1]

    try:
        os.mkdir(folderPath + extension)
    except FileNotFoundError:
        print("Error in parent dir")
    except FileExistsError:
        os.rename(folderPath + file, folderPath + extension + "/" + file)
    else:
        os.rename(folderPath+file, folderPath+extension+"/"+file)
