"""
https://codefun2000.com/p/P1077
meituan 2023.3.11-第一题-字符串修改

2023年10月30日 16点28分
"""

def solve(s: str):
    s = list(s)
    n = len(s)
    res = 0
    for i in range(1, n):
        if s[i] == s[i - 1]:
            s[i] = '*'
            res += 1
    return res

print(solve(input()))