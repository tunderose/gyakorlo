# Exercise 4.1: Someone called Frank has a list containing how many days he was sick each quarter of a year.
# So the first element of the list dictates how many days he was sick in the first quarter of the year.
# Frank usually has dance lessons every day, but when he is sick he doesn't go.
# Write a program that shows how many days Frank went dancing last year.
# Example 1: sick_days = [10, 4, 5, 19]
# Output: Frank was sick for 38 days.
# Example 2: sick_days = [0, 4, 1, -11
# Output: Frank can't be sick for -1 days!
# He went dancing for 327 days

sick_day = [10, 4, 5, 19]
total_sick_day = sum(sick_day)
dancing_days = int(365 - total_sick_day)
print(f"Frank went dancing for " +str(dancing_days) +" days")