# Write a program that gives the user a basic test with three questions.
# If they have a question wrong stop the quiz,
# if they have it right give them the next question.
# Example 1: What is 2 * 2? That is correct!
# What is 6 / 3? 2 That is also correct!
# What is 9 * 9? 18 Correct! You passed the test!
# Example 2: What is 2 * 2? That is correct!
# What is 6 / 3? That is false, you failed the test
import sys

question_1 = int(input("Answer the following question: What is 2 * 2? : "))
question_2 = int(input("Answer the following question: What is 6 / 3? : "))
question_3 = int(input("Answer the following question: What is 9 * 9? : "))

if question_1 == 4 and question_2 == 2 and question_3 == 81:
     print("Correct! You passed the test!")

if question_1 != 4 and question_2 != 2 and question_3 != 81:
    sys.exit("That is false, you failed the test.")