import random
import time

player_health = 100
computer_health = 100

while (player_health > 0) or (computer_health > 0):
    print("\nPlayer HP: " + str(player_health) + "               CPU HP: " + str(computer_health))
    if player_health <= 0:
        print("You Lose!")
        break
    print("\n Your turn!")
    player_move = input("Enter Move: ")
    if player_move.lower().strip() == "punch":
        damage = random.randint(18, 26)
        computer_health = computer_health - damage
        print("\nYou punched the CPU for " + str(damage) + " HP!")
    elif player_move.lower().strip() == "kick":
        damage = random.randint(5, 51)
        computer_health = computer_health - damage
        print("\nYou kicked the CPU for " + str(damage) + " HP!")
    elif player_move.lower().strip() == "heal":
        hpgain = random.randint(15, 31)
        player_health = player_health + hpgain
        healeq = (100 + hpgain) - player_health
        print("\nYou healed for " + str(healeq) + " HP!")
        if player_health > 100:
            player_health = 100
    print("\nPlayer HP: " + str(player_health) + "               CPU HP: " + str(computer_health))
    if computer_health <= 0:
        print("You Win!")
        break
    print("\nCPU's Turn!")
    time.sleep(1)
    computer_move = random.randint(1, 4)
    if computer_move == 1:
        damage = random.randint(18, 26)
        player_health = player_health - damage
        print("CPU used punch! You lost " + str(damage) + " HP!")
    elif computer_move == 2:
        damage = random.randint(5, 51)
        player_health = player_health - damage
        print("CPU used kick! You lost " + str(damage) + " HP!")
    elif computer_move == 3:
        hpgain = random.randint(15, 31)
        computer_health = computer_health + hpgain
        healeq = (100 + hpgain) - computer_health
        print("CPU used heal! It gained " + str(healeq) + " HP!")
        if computer_health > 100:
            computer_health = 100

