# Exercise 4.2: Frank now has danced for another year, making another list.
# He wants to check in which quarter of the last two years he got sick the most.
# Write a program that turns the two lists into one list of length & and then check which quarter he was sick the most
# Example 1:sick_days_1 = [10, 4, 5, 19] sick_days_2 = [7, 8, 2, 12]
# Example 2:sick_days 1 = [0, 4, 1, 2] sick_days_2 = [3, 4, 0, 0]
# Output:The full list of frank's sick days is: [10, 4, 5, 19, 7, 8, 2, 12].
# Output: The full list of frank's sick days is: [0, 4, 1, 2, 3, 4, 0, 01.
# Frank was sick the most in quarter 4 of the first year.
# Frank was sick the most in quarter 6 of the second year.
# OR Output:
# The full list of frank's sick days is: [0, 4, 1, 2, 3,4, 0,01.]
# Frank was sick the most in quarter 2 of the first year.


sick_days_1 = [10, 4, 5, 19]
sick_days_2 = [7, 8, 2, 12]
total_sick_days = (sick_days_1 + sick_days_2)
the_longest_sickness = max(total_sick_days)
print(total_sick_days)

if the_longest_sickness == sick_days_1[0]:
    print("Frank was sick the most in quarter 1st of the first year.")
elif the_longest_sickness == sick_days_1[1]:
    print("Frank was sick the most in quarter 2nd of the first year.")
elif the_longest_sickness == sick_days_1[2]:
    print("Frank was sick the most in quarter 3rd of the first year.")
elif the_longest_sickness == sick_days_1[3]:
    print("Frank was sick the most in quarter 4th of the first year.")
elif the_longest_sickness == sick_days_2[0]:
    print("Frank was sick the most in quarter 1st of the second year.")
elif the_longest_sickness == sick_days_2[1]:
    print("Frank was sick the most in quarter 2nd of the second year.")
elif the_longest_sickness == sick_days_2[2]:
    print("Frank was sick the most in quarter 3rd of the second year.")
else:
    print("Frank was sick the most in quarter 4th of the second year.")