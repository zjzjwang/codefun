

def count(s: str) -> int:
  l, r = 0, len(s) - 1
  pos = []
  while l < r:
    if s[l] != s[r]:
      pos.append((l, r))
    l += 1
    r -= 1
  return pos


def solve(s: str) -> str:
  pos = count(s)
  cnt = len(pos)
  c = list(s)
  if cnt == 0:
    l, r = 0, len(c) - 1
    while l < r and s[l] == 'a':
      l += 1
      r -= 1
    if l <= r:
      c[l] = c[r] = 'a'
  elif cnt == 1:
    l, r = pos[0]
    if c[l] != 'a' and c[r] != 'a':
      c[l] = c[r] = 'a'
    elif c[l] == 'a' or c[r] == 'a':
      c[l] = c[r] = 'a'
      if len(c) % 2 == 1:
        c[len(c) // 2] = 'a'
  elif cnt == 2:
    for l, r in pos:
      c[l] = c[r] = min(c[l], c[r])
  else:
    raise ValueError("Invalid input")
  
  return "".join(c)


# assert solve("acca") == "aaaa"
# assert solve("baccab") == "aaccaa"
# assert solve("ccbcc") == "acbca"
# assert solve("aabaa") == "aaaaa"

# assert solve("abcea") == "aacaa"
# assert solve("abccea") == "aaccaa"

# assert solve("abcde") == "abcba"
print(solve(input()))
