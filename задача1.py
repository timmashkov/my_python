numbers = [int(i) for i in input().split()]
count = 0
for num in range(len(numbers)):
    if num % 2 != 0:
        count += numbers[num]
print(count)
