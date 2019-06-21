import math

word = input("Enter a word: ")

word_to_list = list(word)

answer = math.factorial(len(set(word_to_list)))

print(answer)
