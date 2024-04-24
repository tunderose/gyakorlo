# Write a program that prints whether an integer is in between 1000 and 2000. If it is not, print
# whether it is lower than 1000 or higher than 2000.
# Example 1:
# number = 1420
# Output:
# This number is in between 1000 and 2000
# Example 2:
# number = 12
# Output:
# This number is lower than 1000

valtozo = int(input("Please type an integer number between 1000 and 2000: "))

if 1000 <= int(valtozo) <= 2000:
    print("This number is in between 1000 and 2000")
elif 2000 < int(valtozo):
    print("this number bigger than 2000")
else:
    print("This number is lower than 1000")

