#!/usr/bin/env python3
from itertools import accumulate,chain,combinations,groupby,permutations,product
from collections import deque,Counter
from bisect import bisect_left,bisect_right
from math import gcd,sqrt,sin,cos,tan,degrees,radians,ceil,floor
from fractions import Fraction
from decimal import Decimal
import sys
import numpy as np
#rstripが必要なことも
#input = lambda: sys.stdin.readline().rstrip()
#inputの高速化、基本はいらん、入力が長いときに使用
#from sys import setrecursionlimit
#setrecursionlimit(10**7)
MOD=10**9+7
INF=float('inf')
#float型の無限大inf
def resolve():
    h,w = map(int, input().split())
    #A = list(map(int, input().split()))
    a = [list(map(int, input().split())) for l in range(h)]
    a=np.array(a)
    amax=np.min(a)
    ans=0
    for i in range(h):
        for j in range(w):
            ans+=a[i][j]-amax
    print(ans)
    #n=int(input())
    #a, b = map(int, input().split())
    #A = list(map(int, input().split()))

if __name__ == "__main__":
    resolve()


