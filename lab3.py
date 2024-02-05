import random

print("Welcome to rock, paper, scissors, lizard, spock!")
print("Choose your weapon by typing its assigned number:")
print("1. Rock")
print("2. Paper")
print("3. Scissors")
print("4. Lizard")
print("5. Spock")

weapon_1 = 1
weapon_2 = 2
weapon_3 = 3
weapon_4 = 4
weapon_5 = 5

print("Take your pick.")
weapon_number = int(input("Enter a weapon number:"))

if weapon_number == 1:
    print("You picked rock")
elif weapon_number == 2:
    print("You picked paper")
elif weapon_number == 3:
    print("You picked scissors")
elif weapon_number == 4:
    print("You picked lizard")
elif weapon_number == 5:
    print("You picked spock")

computer_choice = random.randint(1, 5)

if computer_choice == 1:
    print("I choose rock!")
elif computer_choice == 2:
    print("I choose paper!")
elif computer_choice == 3:
    print("I choose scissors!")
elif computer_choice == 4:
    print("I choose lizard!")
elif computer_choice == 5:
    print("I choose spock!")

if weapon_number == computer_choice:
    print("It's a tie!")
elif (
    (weapon_number == 1 and computer_choice == 4) or
    (weapon_number == 1 and computer_choice == 3) or
    (weapon_number == 2 and computer_choice == 1) or
    (weapon_number == 2 and computer_choice == 5) or
    (weapon_number == 3 and computer_choice == 4) or
    (weapon_number == 3 and computer_choice == 2) or
    (weapon_number == 4 and computer_choice == 2) or
    (weapon_number == 4 and computer_choice == 5) or
    (weapon_number == 5 and computer_choice == 1) or
    (weapon_number == 5 and computer_choice == 3)
):
    print("You win!")
elif (
    (computer_choice == 1 and weapon_number == 4) or
    (computer_choice == 1 and weapon_number == 3) or
    (computer_choice == 2 and weapon_number == 1) or
    (computer_choice == 2 and weapon_number == 5) or
    (computer_choice == 3 and weapon_number == 4) or
    (computer_choice == 3 and weapon_number == 2) or
    (computer_choice == 4 and weapon_number == 2) or
    (computer_choice == 4 and weapon_number == 5) or
    (computer_choice == 5 and weapon_number == 1) or
    (computer_choice == 5 and weapon_number == 3)
):
    print("You lose!")