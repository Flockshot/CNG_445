import math
import random
import re # Regular expression
from math import exp
from math import sqrt as root


a = math.sqrt(9.8)
print(a)

b = random.randrange(1, 7)
print(b)

a = exp(3)
print(a)

a = root(9.8)
print(a)

# Make it a module

def printHi():
    print("Hi")

# re.match() - checks if the string starts with the specified pattern
# re.search() - checks if the string contains the specified pattern

def matching():
    if re.match("hello", "hello hi"):
        print("Matched")
        print(re.match("hello", "hello hi")) # Gives info about start and end index (end not included)
    else:
        print("Not matched")


# Will only run if it is called a main program, and wont run if it is imported into another file.
# If you don't add this then when you import this module into other, then the main function/statements will run
if __name__ == "__main__"
    printHi()