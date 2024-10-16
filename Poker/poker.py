import random
import matplotlib.pyplot
import unittest

cards = list(range(0, 52))
possibilities = {
    "high_card": 0, "pair": 0, "two_pair": 0, "three_of_a_kind": 0,
    "straight": 0, "flush": 0, "full_house": 0, "four_of_a_kind": 0,
    "straight_flush": 0, "royal_flush": 0
}


def get_card(card):
    """
    Returns:
    tuple: A tuple (suit, value), where suit is 0-3 (for 4 suits) and value is 0-12.
    """
    return card // 13, card % 13


def count_values(cards):
    """
    Counts the frequency of each card value in a given hand.

    Args:
    cards (list): List of cards, where each card is an integer from 0 to 51.

    Returns:
    dict: A dictionary where the keys are card values (0-12) and the values are their counts.
    """
    values = [get_card(card)[1] for card in cards]
    return {v: values.count(v) for v in set(values)}


def count_suits(cards):
    """
    Counts the frequency of each suit in a given hand.

    Args:
    cards (list): List of cards, where each card is an integer from 0 to 51.

    Returns:
    dict: A dictionary where the keys are suits (0-3) and the values are their counts.
    """
    suits = [get_card(card)[0] for card in cards]
    return {s: suits.count(s) for s in set(suits)}


def check_pair(cards):
    """
    Checks if the hand contains a pair.
    """
    return 2 in count_values(cards).values()


def check_two_pair(cards):
    """
    Checks if the hand contains two pairs.
    """
    return list(count_values(cards).values()).count(2) == 2


def check_three_of_a_kind(cards):
    """
    Checks if the hand contains three of a kind.
    """
    return 3 in count_values(cards).values()


def check_four_of_a_kind(cards):
    """
    Checks if the hand contains four of a kind.
    """
    return 4 in count_values(cards).values()


def check_flush(cards):
    """
    Checks if the hand is a flush (all cards are of the same suit).
    """
    return 5 in count_suits(cards).values()


def check_full_house(cards):
    """
    Checks if the hand is a full house (three of a kind and a pair).
    """
    values = count_values(cards).values()
    return 3 in values and 2 in values


def check_straight(cards):
    """
    Checks if the hand is a straight (five cards in sequential rank).
    """
    values = sorted(get_card(card)[1] for card in cards)
    if values == [0, 9, 10, 11, 12]:  # Royal straight (A, 10, J, Q, K)
        return True
    return all(values[i] + 1 == values[i + 1] for i in range(4))


# Draw cards and evaluate hands
def draw(card_list, hand_size):
    """
    Draws a random hand of cards and updates the count of possible poker hands.

    Args:
    card_list (list): The full deck of cards (0-51).
    hand_size (int): The number of cards to draw.
    """
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


def main():
    unittest.main(exit=False)
    draws = 1000000
    for _ in range(draws):
        draw(cards, 5)

    fig, ax = matplotlib.pyplot.subplots()
    total = 0
    for key, value in possibilities.items():
        percent = 100 * value / draws
        p = ax.bar(key, percent)
        ax.bar_label(p, label_type="edge")
        print(f"{key}: {percent:.2f}% ({value})")
        total += value
    print("Total hands evaluated:", total)
    matplotlib.pyplot.show()


if __name__ == "__main__":
    main()
