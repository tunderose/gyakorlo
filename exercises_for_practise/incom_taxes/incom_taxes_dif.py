# In a certain tax system, people who earn more have to pay a higher percentage of taxes. For example:
# People earning under €67000 have to pay 24% of all of their earnings to the government in taxes.
# People earning under €97000 have to pay 31% of all of their earnings to the government in taxes.
# People earning more than €97000 have to pay 34% of all of their earnings to the government in taxes.
# Write a program that calculates how much money someone has left after taxes, given their income.
# Example 1: income = 58200 Output: Your income after taxes is 44232 euros
# Example 2: income = 101000 Output: Your income after taxes is 66660 euros
# tax counting formula: tax amount = income * tax rate/100

income = float(input("type the income: "))
tax_boarder_1 = 67000
tax_boarder_2 = 97000

if bool(tax_boarder_1 >= income):
    print("Your income after taxes is " + str(income - (income * 24 / 100)) + "euros")
elif bool(tax_boarder_1 >= income <= tax_boarder_2):
    print("Your income after taxes is " + str(incom     e - (income * 31 / 100)) + "euros")
else:
    print("Your income after taxes is " + str(income - (income * 34 / 100)) + "euros")