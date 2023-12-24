# First sol
# f = open("day4.txt", "r")
# lines = f.readlines()

# t_points = 0
# for l in lines:
#     points = 0
#     firstl, secondl = [set(s.split()) for s in l.split(":")[1].split("|")]
#     matches = len(firstl & secondl)

#     if matches > 0:
#         points = 2 ** (matches - 1)

#     t_points += points


# print(t_points)

# Second sol
f = open("day4.txt", "r")
lines = f.readlines()

t_points = 0
cards = [1 for _ in lines]

i = 0
while i < len(cards):
    firstl, secondl = [set(s.split()) for s in lines[i].split(":")[1].split("|")]
    matches = len(firstl & secondl)

    # 1 has 1, 2 has 2 copies, 3 has 4 copies ...
    for j in range(1, matches + 1):
        if i + j < len(cards):
            cards[i + j] += cards[i]

    i += 1

print(cards)
total_scratchcards = sum(cards)

print(total_scratchcards)
