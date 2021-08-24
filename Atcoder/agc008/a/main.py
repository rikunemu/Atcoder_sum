x,y = map(int, input().split())
ans = 0
if abs(x) == abs(y):
    if x != y:
        ans += 1
    print(ans)
    exit()
if abs(x) < abs(y):
    if x < 0:
        ans += 1
    if y < 0:
        ans += 1
    ans += abs(abs(x)-abs(y))
else:
    if x > 0:
        ans += 1
    if y > 0:
        ans += 1
    ans += abs(abs(x)-abs(y))
print(ans)