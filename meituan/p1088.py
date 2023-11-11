from typing import List


def solve(colors: List[int], k: int) -> int:
  n = len(colors)
  ans = 0
  cnt = {}

  left, right = 0, 0
  while right < n:
    cr = colors[right]
    right += 1
    cnt[cr] = cnt.get(cr, 0) + 1 

    while len(cnt) > k:
      cl = colors[left]
      left += 1
      cnt[cl] -= 1
      if cnt[cl] == 0:
        del cnt[cl]
    
    ans = max(ans, right - left)
  return ans

n, k = map(int, input().split())
colors = list(map(int, input().split()))

ans = solve(colors, k)
print(ans)