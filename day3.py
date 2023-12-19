f = open("day3.txt", "r")

# make it a matrix
matrix = []
lines = f.readlines()
for line in lines:
    matrix.append(list(line.strip()))


sum = 0
num = ""
start = end = None
gear_positions = {}
# num, gear_pos
directions = [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (-1, -1), (1, -1), (-1, 1)]
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if matrix[i][j].isdigit():
            if not num:
                start = (i, j)
            num += matrix[i][j]
            end = (i, j)
        else:
            if num != "":
                possible_gear = False
                for dx, dy in directions:
                    for pos in [start, end]:
                        nx, ny = pos[0] + dx, pos[1] + dy
                        if 0 <= nx < len(matrix) and 0 <= ny < len(matrix[nx]):
                            if matrix[nx][ny] == "*":
                                possible_gear = True
                                gear_pos = (nx, ny)
                                if gear_pos in gear_positions:
                                    if int(num) not in gear_positions[gear_pos]:
                                        gear_positions[gear_pos].append(int(num))
                                else:
                                    gear_positions[gear_pos] = [int(num)]

                num = ""

for gear, nums in gear_positions.items():
    if len(nums) == 2:
        print(gear, nums)
        sum += nums[0] * nums[1]

print(sum)
