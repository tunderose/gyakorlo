# Exercise 3: Write a program that converts a list (size of 5) of characters into a string.
# Example 1: my_Ist = ['h', 'e', "', l', 'o']
# Example 2: my_Ist=I'h', 'e', 'Y]
# Output1: The string is: hello
# Output2: This list doesn't have the right size

import numpy as np

my_list =['h', 'e', 'l', 'l', 'o']
word = np.array(my_list)
if len(my_list) == 5:
   print(*(word))
else:
    print("This list doesn't have the right size")