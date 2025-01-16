import random

POSSIBLE_VALUES = ["rock", "paper", "scissors", "spock", "lizard"]

symbol_counts = {value: 0 for value in POSSIBLE_VALUES}
win_counts = {"player": 0, "computer": 0}


def main():
    while True:
        show_menu()
        try:
            choice = int(input(">>> "))
            if choice == 1:
                play_game()
            elif choice == 2:
                show_stats()
            elif choice == 3:
                print("Game ended. Goodbye!")
                break
            else:
                print("Invalid input. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")


def show_stats():
    print("\nNumber of symbols played:")
    for symbol, count in symbol_counts.items():
        print(f"{symbol}: {count}")

    print("\nGame results:")
    for participant, wins in win_counts.items():
        print(f"{participant}: {wins}")


def play_game():
    computer_choice = random.choice(POSSIBLE_VALUES)
    computer_index = parse_choice(computer_choice)

    user_input = input("Choose between rock, paper, scissors, spock, lizard >>> ").lower()
    if user_input not in POSSIBLE_VALUES:
        print("Invalid choice. Please choose a valid option!")
        return

    user_index = parse_choice(user_input)

    symbol_counts[user_input] += 1
    symbol_counts[computer_choice] += 1

    print(f"The computer chose {computer_choice}, and the player chose {user_input}.")
    if computer_index == user_index:
        print("It's a draw!")
    elif ((computer_index - user_index) % 5) % 2 == 1:
        print("The computer wins!")
        win_counts["computer"] += 1
    else:
        print("The player wins!")
        win_counts["player"] += 1


def show_menu():
    print("\n\nRock Paper Scissors Spock Lizard")
    print("================================")
    print("1) Play a game of RPSSL")
    print("2) Show statistics")
    print("3) Quit the game")


def parse_choice(choice):
    return POSSIBLE_VALUES.index(choice)


if __name__ == "__main__":
    main()
