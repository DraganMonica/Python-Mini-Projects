import random
import art

game_images = [art.rock, art.paper, art.scissors]
user_choice = int(input("What do you choose?\n Type 0 for Rock, 1 for Paper, 2 for Scissors\n"))

# verificare daca nr este valid
if user_choice < 0 or user_choice > 2:
    print("You typed an invalid number.\nYou lose!")
else:
    print(f"You chose:\n{game_images[user_choice]}")
    #
    computer_choice = random.randint(0, 2)
    print(f"Computer chose: {game_images[computer_choice]}")

    # determinarea castigatorului
    if user_choice == computer_choice:
        print("It's a draw!")
    elif (user_choice == 0 and computer_choice == 2) or \
         (user_choice == 1 and computer_choice == 0) or \
         (user_choice == 2 and computer_choice == 1):
        print("You win!")
    else:
        print("You lose...")
