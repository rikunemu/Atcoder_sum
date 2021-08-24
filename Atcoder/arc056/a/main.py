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
    #n=int(input())
    a, b,k,l = map(int, input().split())
    ans1=a*k
    ans2=b*(k//l)+a*(k%l)
    ans3=b*(ceil(k/l))
    print(min(ans1,ans2,ans3))
    #A = list(map(int, input().split()))

if __name__ == "__main__":
    resolve()


