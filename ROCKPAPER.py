import random
print("Welcome to the Game of rock, paper, scissors, lizard, spock !!!")
print("Game Rules: There are two players (player1 and player2), each will get their turn to enter a weapon.")
print("A player can choose a weapon by choosing a number between 1 and 5.")
print(" 1 represents rock")
print(" 2 represents paper")
print(" 3 represents scissors")
print(" 4 represents lizard")
print(" 5 represents spock")

weapon_1 = 1
weapon_2 = 2
weapon_3 = 3
weapon_4 = 4
weapon_5 = 5
print("Player1's turn")
weapon_number = int(input("Enter the weapon number :"))
if weapon_number == 1:
    print("Player1 picks rock")
elif weapon_number == 2:
    print("Player1 picks paper")
elif weapon_number == 3:
    print("Player1 picks scissors")
elif weapon_number == 4:
    print("Player1 picks lizard")
else:
    print("Player1 picks spock")
print("Computer's turn")
player2 = int(random.randrange(1, 5, 1))
if player2 == 1:
    print("Computer picks rock")
elif player2 == 2:
    print("Computer picks paper")
elif player2 == 3:
    print("Computer picks scissors")
elif player2 == 4:
    print("Computer picks lizard")
else:
    print("Computer picks spock")
player1 = weapon_number
if player1 == weapon_1 and (player2 == weapon_3 or player2 == weapon_4):
    print("Player1 wins!!")
elif player1 == weapon_1 and (player2 == weapon_2 or player2 == weapon_5):
    print("Computer wins!!")
elif player1 == weapon_2 and (player2 == weapon_1 or player2 == weapon_5):
    print("Player1 wins!!")
elif player1 == weapon_2 and (player2 == weapon_3 or player2 == weapon_4):
    print("Computer wins!!")
elif player1 == weapon_3 and (player2 == weapon_2 or player2 == weapon_4):
    print("Player1 wins!!")
elif player1 == weapon_3 and (player2 == weapon_1 or player2 == weapon_5):
    print("Computer wins!!")
elif player1 == weapon_4 and (player2 == weapon_2 or player2 == weapon_5):
    print("Player1 wins!!")
elif player1 == weapon_4 and (player2 == weapon_1 or player2 == weapon_3):
    print("Computer wins!!")
elif player1 == weapon_5 and (player2 == weapon_1 or player2 == weapon_3):
    print("Player1 wins!!")
elif player1 == weapon_5 and (player2 == weapon_2 or player2 == weapon_4):
    print("Computer wins!!")
else:
    print("Player1 & Computer are tied")