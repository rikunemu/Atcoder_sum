#!/usr/bin/env python3
from itertools import accumulate,chain,combinations,groupby,permutations,product
from collections import deque,Counter
from bisect import bisect_left,bisect_right
from math import gcd,sqrt,sin,cos,tan,degrees,radians,ceil,floor
from fractions import Fraction
from decimal import Decimal
import numpy as np
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
    n=int(input())
    cnt = 1
    ans = 0
    #a, b = map(int, input().split())
    P = list(map(int, input().split()))
    result = sorted(P, reverse=True)
    ANS = [n+100] * n
    for i in range(len(P)):
        for j in range(n):
            if P[j] == result[i] and ANS[j]==n+100:
                ANS[j] = cnt
                ans += 1
        if i+1 < n:
             if result[i] != result[i+1]:
                cnt += ans
                ans = 0
    for i in range(n):
        print(ANS[i])
        
        
        
    
    

if __name__ == "__main__":
    resolve()