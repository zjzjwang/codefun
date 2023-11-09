# https://codefun2000.com/p/P1087

N = 1010
def solve(a, b, coords):
    diff = [[0] * N for _ in range(N)]
    for i in range(N - 1):
        for j in range(N - 1):
            diff[i + 1][j + 1] = diff[i + 1][j] + diff[i][j + 1] - diff[i][j] + coords[i][j]

    ans = 0
    for i in range(a, N - 1):
        for j in range(b, N - 1):
            cnt = diff[i + 1][j + 1] - diff[i + 1][j - b] - diff[i - a][j + 1] + diff[i - a][j - b]
            ans = max(cnt, ans)

    return ans

n, a, b = map(int, input().split())
coords = [[0] * N for _ in range(N)]
for _ in range(n):
    x, y = map(int, input().split())
    coords[x][y] += 1

ans = solve(a, b, coords)
print(ans)
    