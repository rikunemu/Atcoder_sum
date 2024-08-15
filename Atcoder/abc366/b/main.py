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
INF=float('inf')
#float型の無限大inf
def resolve():
    N=int(input())
    #a, b = map(int, input().split())
    #A = list(map(int, input().split()))
    S = [input() for _ in range(N)]
    M = max(map(len, S))
    T = [["*"] * N for _ in range(M)]
    for i in range(N):
        for j in range(len(S[i])):
            T[j][N - i - 1] = S[i][j]
    for i in range(M):
        while T[i][-1] == "*":
            T[i].pop()
        print("".join(T[i]))

if __name__ == "__main__":
    resolve()


