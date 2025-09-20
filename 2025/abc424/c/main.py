#!/usr/bin/env python3
from itertools import accumulate,chain,combinations,groupby,permutations,product
from collections import deque,Counter
from bisect import bisect_left,bisect_right
from math import gcd,sqrt,sin,cos,tan,degrees,radians,ceil,floor
from fractions import Fraction
from decimal import Decimal
import sys

# 入力
def rI(): return int(sys.stdin.readline().rstrip())
def rLI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def rI1(): return (int(sys.stdin.readline().rstrip())-1)
def rLI1(): return list(map(lambda a:int(a)-1,sys.stdin.readline().rstrip().split()))
def rS(): return sys.stdin.readline().rstrip()
def rLS(): return list(sys.stdin.readline().rstrip().split())

#rstripが必要なことも
#input = lambda: sys.stdin.readline().rstrip()
#inputの高速化、基本はいらない、入力が長いときに使用
#from sys import setrecursionlimit
#setrecursionlimit(10**7)
MOD=10**9+7
INF=float('inf')
G = {}
n=int(input())
cnt = 0
status = []
#float型の無限大inf
def dfs(s):
    global cnt
    global status
    status[s] = True
    if 0 in G[s]:
        cnt +=1
        return
    for r in G[s]:
        if not status[r]:
            dfs(r)
def resolve():
    global cnt
    ANS = [0]*(n+1)
    #a, b = map(int, input().split())
    #A = list(map(int, input().split()))
    for i in range(1,n+1):
        G[i] = set() # 頂点iに隣接する頂点の集合
        a, b = map(int, input().split())
        if a == 0 and b == 0:
            G[i].add(0)
            continue
        G[i].add(a)
        G[i].add(b)
    for key in range(1,n+1):
        global status
        status = [False]*(n+1)
        # 頂点keyに隣接する頂点がない場合は、空集合を出力
        dfs(key)
    print(cnt)



if __name__ == "__main__":
    resolve()