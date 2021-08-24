#!/usr/bin/env python3
from itertools import accumulate,chain,combinations,groupby,permutations,product
from collections import deque,Counter
from bisect import bisect_left,bisect_right
#from math import gcd,sqrt,sin,cos,tan,degrees,radians,ceil,floor
from fractions import Fraction
from decimal import Decimal
import sys
import math
#rstripが必要なことも
#input = lambda: sys.stdin.readline().rstrip()
#inputの高速化、基本はいらん、入力が長いときに使用
#from sys import setrecursionlimit
#setrecursionlimit(10**7)
def permutations_count(n, r):
    return math.factorial(n) // math.factorial(n - r)
MOD=10**9+7
INF=float('inf')
#float型の無限大inf
def resolve():
    S=(input())
    T='*chokudai'
    dp=Counter()
    dp['*']=1
    for char in S:
        if char in T:

            char_prev=T[T.index(char)-1]
            dp[char]+=dp[char_prev]
            dp[char]%=MOD
    print(dp['i'])


if __name__ == "__main__":
    resolve()


