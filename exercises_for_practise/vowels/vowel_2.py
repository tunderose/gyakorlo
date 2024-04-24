def is_vowel(char):

    all_vowels = 'a,e,i,o,u'
    return char in all_vowels

print(is_vowel(input('type a letter: ')))