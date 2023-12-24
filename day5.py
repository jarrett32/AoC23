# Solution One
f = open("day5.txt", "r")
lines = f.readlines()


def line_to_map(lines):
    array = []
    for line in lines:
        array.append(line.strip().split(" "))

    return array


def find_mapping(n, ranges):
    for r in ranges:
        dest, src, l = r
        if int(src) <= n < int(src) + int(l):
            n = int(dest) + (n - int(src))
            break

    return n


# seeds = lines[0].split(":")[1].strip().split(" ")
stss = line_to_map(lines[3:43])
sstf = line_to_map(lines[45:70])
ftw = line_to_map(lines[72:114])
wtl = line_to_map(lines[116:163])
ltt = line_to_map(lines[165:181])
tth = line_to_map(lines[183:199])
htl = line_to_map(lines[201:213])

# lowest = float("inf")
# for seed in seeds:
#     seed_num = int(seed)

#     soil = find_mapping(seed_num, stss)
#     fertilizer = find_mapping(soil, sstf)
#     water = find_mapping(fertilizer, ftw)
#     light = find_mapping(water, wtl)
#     temperature = find_mapping(light, ltt)
#     humidity = find_mapping(temperature, tth)
#     location = find_mapping(humidity, htl)

#     lowest = min(lowest, location)

# print(lowest)

# Solution Two
all_seeds = lines[0].split(":")[1].strip().split(" ")
seeds = []
for i in range(0, len(all_seeds), 2):
    seeds.append([all_seeds[i], all_seeds[i + 1]])

lowest = float("inf")

for tup in seeds:
    star, rg = tup
    star = int(star)
    rg = int(rg)
    print("seed: ", star, "range: ", rg, "to: ", star + rg - 1)
    for i in range(rg):
        seed_num = int(star) + i

        soil = find_mapping(seed_num, stss)
        fertilizer = find_mapping(soil, sstf)
        water = find_mapping(fertilizer, ftw)
        light = find_mapping(water, wtl)
        temperature = find_mapping(light, ltt)
        humidity = find_mapping(temperature, tth)
        location = find_mapping(humidity, htl)

        lowest = min(lowest, location)

print(lowest)
