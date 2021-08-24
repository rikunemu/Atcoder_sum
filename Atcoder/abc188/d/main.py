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
    C=10**9+5
    n,c1 = map(int, input().split())
    #A = list(map(int, input().split()))
    ANS=[0]*C
    for _ in range(n):
        a,b,c = map(int, input().split())
        ANS[a]+=c
        ANS[b+1]-=c
    S=list(accumulate(ANS))
    ans=0
    for i in S:
        if i>c1:
            ans+=c1
        elif S<0:
            ans+=0
        else:
            ans+=i
    print(ans)

if __name__ == "__main__":
    resolve()


