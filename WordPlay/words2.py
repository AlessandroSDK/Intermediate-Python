import scrabble

#First example on how to find the longest palindrome work in sowpos.txt

longest = ""

for word in scrabble.wordlist:
    is_palindrome = True
    for index in range(len(word)):
        if word[index] != word[-(index + 1)]:
            is_palindrome = False
    if is_palindrome and len(word) > len(longest):
        longest = word
print("First example")
print(longest)
print()
#Sencond example on how to find the longest palindrome work in sowpos.txt

longest = ""

for word in scrabble.wordlist:
    if list(word) == list(reversed(word)) and len(word) > len(longest):
        longest = word
print("Second example")
print(longest)
print()

#Third example on how to find the longest palindrome work in sowpos.txt

import scrabble

longest = ""

for word in scrabble.wordlist:
    if word == word[::-1] and len(word) > len(longest):
        longest = word
print("Third example")
print(longest)
print()