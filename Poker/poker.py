import random
import matplotlib.pyplot as plt


def get_card(card):
    return card // 13, card % 13


def count_values(cards):
    values = [get_card(card)[1] for card in cards]
    return {v: values.count(v) for v in set(values)}


def count_suits(cards):
    suits = [get_card(card)[0] for card in cards]
    return {s: suits.count(s) for s in set(suits)}


def check_pair(cards):
    return 2 in count_values(cards).values()


def check_two_pair(cards):
    return list(count_values(cards).values()).count(2) == 2


def check_three_of_a_kind(cards):
    return 3 in count_values(cards).values()


def check_four_of_a_kind(cards):
    return 4 in count_values(cards).values()


def check_flush(cards):
    return 5 in count_suits(cards).values()


def check_full_house(cards):
    values = count_values(cards).values()
    return 3 in values and 2 in values


def check_straight(cards):
    values = sorted(get_card(card)[1] for card in cards)
    if values == [0, 9, 10, 11, 12]:
        return True
    return all(values[i] + 1 == values[i + 1] for i in range(4))


def draw(card_list, hand_size, possibilities):
    try:
        if hand_size > len(card_list):
            raise ValueError("Hand size cannot be larger than the number of available cards.")

        cards = random.sample(card_list, hand_size)
        values = sorted(get_card(card)[1] for card in cards)

        if check_flush(cards):
            if values == [0, 9, 10, 11, 12]:
                possibilities["royal_flush"] += 1
            elif check_straight(cards):
                possibilities["straight_flush"] += 1
            else:
                possibilities["flush"] += 1
        elif check_straight(cards):
            possibilities["straight"] += 1
        elif check_four_of_a_kind(cards):
            possibilities["four_of_a_kind"] += 1
        elif check_full_house(cards):
            possibilities["full_house"] += 1
        elif check_three_of_a_kind(cards):
            possibilities["three_of_a_kind"] += 1
        elif check_two_pair(cards):
            possibilities["two_pair"] += 1
        elif check_pair(cards):
            possibilities["pair"] += 1
        else:
            possibilities["high_card"] += 1

    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


def main():
    while True:
        try:
            draws = int(input("Wie oft soll das Ziehen wiederholt werden? "))
            if draws < 0:
                print("Bitte geben Sie eine positive Zahl ein.")
            else:
                break
        except ValueError:
            print("Ungültige Eingabe! Bitte geben Sie eine ganze Zahl ein.")

    cards = list(range(0, 52))
    possibilities = {
        "high_card": 0, "pair": 0, "two_pair": 0, "three_of_a_kind": 0,
        "straight": 0, "flush": 0, "full_house": 0, "four_of_a_kind": 0,
        "straight_flush": 0, "royal_flush": 0
    }

    for _ in range(draws):
        draw(cards, 5, possibilities)

    fig, ax = plt.subplots()
    fig.set_size_inches(17, 7)
    total = 0
    for key, value in possibilities.items():
        percent = 100 * value / draws
        p = ax.bar(key, percent)
        ax.bar_label(p, label_type="edge")
        print(f"{key}: {percent:.2f}% ({value})")
        total += value
    print("Total hands evaluated:", total)
    plt.show()


if __name__ == "__main__":
    main()
