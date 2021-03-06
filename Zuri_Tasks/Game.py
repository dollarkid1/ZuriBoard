import random


def game():
    while True:

        print("\"R\" for rock \n"
              "\"P\" for paper \n"
              "\"S\" for scissors ")
        user_action = input("Enter a choice: ")

        possible_actions = ["R", "P", "S"]

        computer_action = random.choice(possible_actions)

        print(f"\nYou chose {user_action}, computer chose {computer_action}.\n")

        if user_action == computer_action:
            print(f"Both players selected {user_action}. It's a tie!")

        elif user_action.lower() == "r":
            if computer_action == "s":
                print("Rock smashes scissors! You win!")
            else:
                print("Paper covers rock! You lose.")

        elif user_action == "p":
            if computer_action == "r":
                print("Paper covers rock! You win!")
            else:
                print("Scissors cuts paper! You lose.")

        elif user_action == "s":
            if computer_action == "p":
                print("Scissors cuts paper! You win!")
            else:
                print("Rock smashes scissors! You lose.")

        play_again = input("Play again? (y/n): ")
        if play_again.lower() != "y":
            break


if __name__ == '__main__':
    print(game())
