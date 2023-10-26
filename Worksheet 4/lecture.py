import sys


def f1():
    f2()


def f2():
    f3()


def f3():
    try:
        raise Exception("x")
        print("a")
    except ArithmeticError:  # if the exception is not caught then it is passed on to stack.
        print("y")
    else:  # Else only runs when there is no exception.
        print("z")
    finally:  # Finally run always, exception or no exception.
        print(".")


try:
    f1()
except Exception as e:
    print(e)

# Command line arguments: import sys

print(sys.argv)
print(len(sys.argv))
print(sys.argv[0])

# Run in cmd by: python3 "location" arg1 "arg 2" 232



# Files


try:
    file = open("clients.txt", "w")
except IOError:
    print("File no open")
    exit(1)

print("Enter the account, name, and balance: ")
for i in range(3):
    accountLine = input("? ")
    file.write(accountLine + "\n")

file.close()



try:
    file = open("clients.txt", "r")
except IOError:
    print("File no open")
    exit(1)

records = file.readlines()                                      # A list of items but with \n at end
records2 = [x.replace("\n", "") for x in records]   # A list of items without \n at end
records3 = file.read().split("\n")          # A list of items without \n at end but with empty element at end
records4 = file.read().split("\n")[:-1]     # A list of items without \n at end and without empty element at end
print(records)
print(records2)
print(records3)
print(records4)

file.close()


# OS stuff

import os

os.mkdir(path)


