

n = int(input())
nums = list(map(int, input().split()))
k = int(input())
ops = input().split()

res = sum(nums)

for i in range(0, len(ops), 2):
    idx, op = int(ops[i]), ops[i + 1]
    if op == '+':
        print(f"{res:.1f}", end=" ")
    elif op == '-':
        print(f"{res - 2 * nums[idx]:.1f}", end=" ")
    elif op == '*':
        print(f"{res - nums[idx - 1] - nums[idx] + nums[idx - 1] * nums[idx]:.1f}", end=" ")
    else:
        print(f"{res - nums[idx - 1] - nums[idx] + nums[idx - 1] / nums[idx]:.1f}", end=" ")

