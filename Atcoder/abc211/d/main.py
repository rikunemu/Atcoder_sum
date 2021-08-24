#!/usr/bin/env python3
from itertools import accumulate,chain,combinations,groupby,permutations,product
from collections import deque,Counter
from bisect import bisect_left,bisect_right
from math import gcd,sqrt,sin,cos,tan,degrees,radians,ceil,floor
from fractions import Fraction
from decimal import Decimal
import sys
#rstripが必要なことも
#input = lambda: sys.stdin.readline().rstrip()
#inputの高速化、基本はいらん、入力が長いときに使用
#from sys import setrecursionlimit
#setrecursionlimit(10**7)
MOD=10**9+7
n,m = map(int, input().split())
g = [[] for _ in range(n)] # 隣接リスト
INF=float('inf')
for _ in range(m):
    a, b = [int(x) for x in input().split()]
    g[a-1].append(b-1)
    g[b-1].append(a-1)
def bfs(u):
    queue = deque([u])
    d = [None] * n # uからの距離の初期化
    d[u] = 0 # 自分との距離は0
    while queue:
        v = queue.pop()
        #print(v)
        for i in g[v]:
            #print(i)
            if d[i] is None:
                d[i] = d[v] + 1
                queue.append(i)
    return d
def dfs(now):
    #print(now, end=' ')
    for i in g[now]:
        dfs(i)
#float型の無限大inf
def resolve():
    #n=int(input())
    #n,m = map(int, input().split())
    #A = list(map(int, input().split()))
   
    #d=bfs(0)
    #print(g)
    dd=dfs(0)
    print(dd[n-1])
    #print(d)

if __name__ == "__main__":
    resolve()


