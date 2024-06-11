# I would like to create a game of rock, paper, scissors that can be played via the CLI
# The player will play against the computer
# The player can choose one of the three options rock, paper, or scissors and should be warned if they enter an invalid option.
# At each round, the player must enter one of the options in the list and be informed if they won, lost, or tied with the opponent.
# By the end of each round, the player can choose whether to play again.
# Display the player's score at the end of the game.
# The minigame must handle user inputs, putting them in lowercase and informing the user if the option is invalid.

import random

def game():
    player_score = 0
    computer_score = 0
    rounds = 0

    while True:
        player_choice = input("Enter rock, paper, or scissors: ").lower()
        computer_choice = random.choice(["rock", "paper", "scissors"])

        if player_choice not in ["rock", "paper", "scissors"]:
            print("Invalid choice. Please enter rock, paper, or scissors.")
            continue

        print(f"Player: {player_choice}")
        print(f"Computer: {computer_choice}")

        if player_choice == computer_choice:
            print("It's a tie!")
        elif player_choice == "rock":
            if computer_choice == "paper":
                print("You lose!")
                computer_score += 1
            else:
                print("You win!")
                player_score += 1
        elif player_choice == "paper":
            if computer_choice == "scissors":
                print("You lose!")
                computer_score += 1
            else:
                print("You win!")
                player_score += 1
        elif player_choice == "scissors":
            if computer_choice == "rock":
                print("You lose!")
                computer_score += 1
            else:
                print("You win!")
                player_score += 1

        rounds += 1
        print(f"Round {rounds} - Player: {player_score} Computer: {computer_score}")

        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            break

    print(f"Final score - Player: {player_score} Computer: {computer_score}")


if __name__ == "__main__":
    game()