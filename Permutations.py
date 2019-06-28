import math

word = input("Enter a word: ")

word_to_list = list(word)

answer = math.factorial(len(set(word_to_list)))

print("There are " + str(answer) + " combinations of the " + str(len(set(word_to_list))) +
      " unique letters in the word " + word)
