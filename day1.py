nums = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

f = open("day1.txt", "r")
sum = 0
for line in f:
    numbers = ""

    for i in range(len(line)):
        if line[i].isdigit():
            numbers += line[i]
        else:
            for n in nums:
                if line.startswith(n, i):
                    numbers += str(nums.index(n))
                    i += len(n)

        #print(numbers)
        if len(numbers) == 1:
            numbers = numbers + numbers

    sum += int(numbers[0] + numbers[-1])
    numbers = ""

print(sum)
