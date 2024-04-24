# Write a program that finds the largest of 4 numbers.
# Example 1: first_number: 10 second_number: 12 third_number: fourth_number: 24
# Output: The largest number is 24
# Example 2: first_number: 10 second_number: 10 third_number: 10 fourth_number: 4
# Output: The largest number is 10

szam_1 = float(input("Type a number: "))
szam_2 = float(input("Type a number: "))
szam_3 = float(input("Type a number: "))
szam_4 = float(input("Type a number: "))

if szam_3 < szam_1 > szam_2 and szam_1 > szam_4:
    print("The biggest number is: " + str(szam_1))
if szam_1 < szam_2 > szam_3 and szam_2 > szam_4:
    print("The biggest number is: " + str(szam_2))
if szam_1 < szam_3 > szam_2 and szam_3 > szam_4:
    print("The biggest number is: " + str(szam_3))
else:
    print("The biggest number is: " + str(szam_4))
