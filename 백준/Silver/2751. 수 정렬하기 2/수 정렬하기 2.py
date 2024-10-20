N = int(input())

nums = []
for i in range(N):
    nums.append(int(input()))

sorted_nums = sorted(nums)

for num in sorted_nums:
    print(num)
