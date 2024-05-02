# Exercise one: write a program that reorders smallest and removes the largest and smallest
# Example 1: my_Ist = [6,2,7,4,3]
# Output: The new list is: [3,4,6]
# Example 2: my _Ist = [6,6,3,2,4,5,5]
# Output: The new list is: [3,4,5,5,6]



my_lst = [6, 2, 7, 4, 3]
reorder= sorted(my_lst)
print(reorder)

del reorder[0]
del reorder[-1]
print(reorder)









