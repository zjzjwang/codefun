"""
https://codefun2000.com/p/P1078
16点32分
"""

from collections import OrderedDict


def solve(begs, ends, n):
    """
    离散差分
    time: O(nlogn), space: O(n)
    """
    mp = OrderedDict()
    for i in range(n):
        a, b = begs[i], ends[i]
        mp[a] = mp.get(a, 0) + 1
        mp[b + 1] = mp.get(b + 1, 0) - 1
            

    cnts = {}
    _sum, pre = 0, min(begs)
    for k in sorted(mp.keys()):
        v = mp[k]
        cnts[_sum] = cnts.get(_sum, 0) + k - pre
        _sum += v
        pre = k
    
    x, y = 0, 0
    for k, v in cnts.items():
        if k > x:
            x = k
            y = v
    return x, y


def solve1(begs, ends, n):
    """
    普通差分
    
    time: O(k) space: O(k) k = max(ends)
    """
    arr = [0] * 100010
    l, r = min(begs), max(ends)
    for i in range(n):
        b, e = begs[i], ends[i]
        arr[b] += 1
        arr[e + 1] -= 1
    
    for i in range(l + 1, r + 1):
        arr[i] += arr[i - 1]
    
    x = max(arr)
    y = 0
    for i in range(l, r + 1):
        if arr[i] == x:
            y += 1
    return x, y


n = int(input())
begs = list(map(int, input().split()))
ends = list(map(int, input().split()))
x, y = solve(begs, ends, n)
print(f"{x} {y}")
