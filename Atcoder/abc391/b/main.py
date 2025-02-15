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
# https://atcoder.jp/contests/abc391/tasks/abc391_b
def resolve():
    # n=int(input())
    N, M = map(int, input().split())

    # M * M マス分を受け取る
    S = [input() for _ in range(N)]
    T = [input() for _ in range(M)]

    # Sの中にTが入っているか見るため全探索する
    # 範囲分の探索
    for i in range(N-M+1):
        for j in range(N-M+1):
            flag = True
            for a in range(M):
                for b in range(M):
                    if S[i+a][j+b] != T[a][b]:
                        flag = False
            if flag:
                print(i+1,j+1)
                return


    #A = list(map(int, input().split()))

if __name__ == "__main__":
    resolve()