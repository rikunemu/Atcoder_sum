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
    a, b,c = map(int, input().split())
    #A = list(map(int, input().split()))
    if a>=b:
        if a==b:
            if c==0:
                print("Aoki")
                exit()
            else:
                print("Takahashi")
                exit()
        print("Takahashi")
    else:
        print("Aoki")


if __name__ == "__main__":
    resolve()


