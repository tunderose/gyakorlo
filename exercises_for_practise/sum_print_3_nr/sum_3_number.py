# Write a program that prints the sum of 3 given numbers, but if all 3 numbers are the same it
# should print 4 times the sum of the 3 numbers
# Example 1: first_number: 10 second_number: 12 third_number: 8
# Output: The sum of these numbers is 30
# Example 2: first_number: 10 second_number: 10 third_number: 10
# Output:(These numbers are the same.) The sum of these numbers is: 30
# Multiplied by 4 this becomes 120

szam_1 = float(input("Type a number: "))
szam_2 = float(input("Type a number: "))
szam_3 = float(input("Type a number: "))

if bool(szam_1 != szam_2 or szam_1 != szam_3 or szam_2 != szam_3):
    print(float((szam_1 + szam_2 + szam_3)))
else:
    print(f"This number are the same. " + str((float(szam_1 + szam_2 + szam_3) * 104)))