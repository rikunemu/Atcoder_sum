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
    n=int(input())
    #a, b = map(int, input().split())
    #A = list(map(int, input().split()))
    x = [0] * n
    y = [0] * n
    for i in range(n):
        x[i],y[i]=map(int,input().split())
    ans=0
    for i in range(n):
        for j in range(i+1,n):
            cnt=(y[i]-y[j])/(x[i]-x[j])
            if -1<=cnt<=1:
                ans+=1
    print(ans)

if __name__ == "__main__":
    resolve()


