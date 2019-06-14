import random

suits = ["H", "S", "D", "C"]
faces = ["A", "J", "Q", "K"]
deck = []

for num in range(2, 11):
    faces.append(str(num))

for suit in range(4):
    for face in range(13):
        card = (faces[face] + suits[suit])
        deck.append(card)

random.shuffle(deck)

print(deck)
