# Write a program that takes a string with a maximum size of 5. Do something different
# #depending on the size of the string:
# 1 Letter: Print the letter 6 times (a = aaaaaa)
# 2 Letters: Switch the position of the letters (at = ta)
# 3 Letters: Move the last letter from the back to the front (Dog = gDo)
# 4 Letters: Print the reverse of the word (Wait = taiW)
# 5 Letters: Print the word divided by t (Brain = Btrtatitn)


letter: str = input("Type any 5 letters: ")

if letter != str and len(letter) <= 5:

     if len(letter) == 1:
        print(str(letter * 6))

     if len(letter) == 2 or 4 and len(letter) != 5:
        reversed_string = letter[::-1]
        print(reversed_string)

     if len(letter) == 3:
        last_letter_move = letter[::-3]
        print(last_letter_move)

     if len(letter) == 5:
        print(letter[0] + 't', letter[1] + 't', letter[2] + 't', letter[3] + 't', letter[4] + 't')

else:
   print("try it again: ")

# why I have the extra line in the 1rst and 3rd sample
