from collections import defaultdict, Counter, deque
H,W=map(int, input().split())
S=[input() for i in range(H)]

dir = [(0, 1), (0, -1), (1, 0), (-1, 0)]


parent = [[None]*W for _ in range(H)]
memo = [[-1]*W for _ in range(H)]
q = deque()

# 始点をキューに全て入れる
for i in range(H):
    for j in range(W):
        if S[i][j] == 'E':
            memo[i][j] = 0
            q.append((i, j))

# BFS
while q:
    y, x = q.popleft()
    for dy, dx in dir:
        ny, nx = y + dy, x + dx
        if 0 <= ny < H and 0 <= nx < W:
            if S[ny][nx] == '.' and memo[ny][nx] == -1:
                memo[ny][nx] = memo[y][x] + 1
                parent[ny][nx] = (y, x)
                q.append((ny, nx))

# 経路復元
ans = [['']*W for _ in range(H)]
for i in range(H):
    for j in range(W):
        if S[i][j] == '#':
            ans[i][j] = '#'
        elif S[i][j] == 'E':
            ans[i][j] = 'E'
        elif parent[i][j] is not None:
            py, px = parent[i][j]
            dy, dx = py - i, px - j
            if dy == -1 and dx == 0:
                ans[i][j] = '^'
            elif dy == 1 and dx == 0:
                ans[i][j] = 'v'
            elif dy == 0 and dx == -1:
                ans[i][j] = '<'
            elif dy == 0 and dx == 1:
                ans[i][j] = '>'
# 出力
for row in ans:
    print(''.join(row))