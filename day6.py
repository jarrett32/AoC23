# Solution 1
# times = [40, 70, 98, 79]
# distance = [215, 1051, 2147, 1005]

times = [40709879]
distance = [215105121471005]

sum = []
for i in range(1):
    ways = 0
    for j in range(times[i]):  # button hold = 0
        speed = j
        travel_time = times[i] - j
        dist = speed * travel_time
        if dist >= distance[i]:
            ways += 1

    sum.append(ways)

total = 1
for i in sum:
    total *= i

print(total)
