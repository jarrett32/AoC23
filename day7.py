# Solution One
f = open("day7.txt", "r")
lines = f.readlines()

# rank = ["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"]

# Solution Two
rank = ["A", "K", "Q", "T", "9", "8", "7", "6", "5", "4", "3", "2", "J"]
hands = [line.strip().split(" ") for line in lines]


# def get_rank(h):
#     hand = h[0]
#     count = {r: hand.count(r) for r in hand}
#     sorted_hand = sorted(hand, key=lambda x: (count[x], rank.index(x)), reverse=True)
#     unique = len(set(hand))

#     if unique == 1:
#         return (8, sorted_hand)
#     elif unique == 2:
#         if 4 in count.values():
#             return (7, sorted_hand)
#         else:
#             return (6, sorted_hand)
#     elif unique == 3:
#         if 3 in count.values():
#             return (5, sorted_hand)
#         else:
#             return (4, sorted_hand)  # Two pair
#     elif unique == 4:
#         return (3, sorted_hand)  # One Pair
#     else:
#         return (2, sorted_hand)


def get_rank(h):
    hand = h[0]
    jacks_count = hand.count("J")

    count = {r: hand.count(r) + (jacks_count if r != "J" else 0) for r in hand}
    sorted_hand = sorted(hand, key=lambda x: (count[x], rank.index(x)), reverse=True)
    unique = len(set(hand))

    if unique == 1:
        return (8, sorted_hand)
    elif unique == 2:
        if 4 in count.values():
            return (7, sorted_hand)
        else:
            return (6, sorted_hand)
    elif unique == 3:
        if 3 in count.values():
            return (5, sorted_hand)
        else:
            return (4, sorted_hand)  # Two pair
    elif unique == 4:
        return (3, sorted_hand)  # One Pair
    else:
        return (2, sorted_hand)


def compare_hands(hand1, hand2):
    r1, sorted_hand1 = get_rank(hand1)
    r2, sorted_hand2 = get_rank(hand2)
    if r1 != r2:
        return r1 - r2

    for card1, card2 in zip(hand1[0], hand2[0]):
        if rank.index(card1) != rank.index(card2):
            return rank.index(card2) - rank.index(card1)
    return 0


def bubble_sort_hands(hands):
    n = len(hands)
    for i in range(n):
        for j in range(0, n - i - 1):
            if compare_hands(hands[j], hands[j + 1]) < 0:
                hands[j], hands[j + 1] = hands[j + 1], hands[j]
    return hands


sorted_hands = bubble_sort_hands(hands.copy())[::-1]
print(sorted_hands[:5])
print(sorted_hands[-5:])

total_sum = sum(i * int(hand[1]) for i, hand in enumerate(sorted_hands, start=1))
print(total_sum)
