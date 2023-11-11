from typing import List

def solve(heights: List[int]) -> int:
    return max(heights) - min(heights)


n = int(input())
heights = list(map(int, input().split()))
ans = solve(heights)
print(ans)