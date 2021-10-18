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
    sumbyou=0
    SUM=[]
    ANS=[]
    for i in range(n):
        a, b = map(int, input().split())
        sumbyou+=a/b
        SUM.append(a/b)
        ANS.append(b)

    sumbyou=sumbyou/2
    ans=0
    for i in range(n):
        if sumbyou>SUM[i]:
            ans+=SUM[i]*ANS[i]
            sumbyou-=SUM[i]
        elif sumbyou==SUM[i]:
            ans+=SUM[i]*ANS[i]
            print(ans)
            exit()
        else:
            ans+=sumbyou*ANS[i]
            print(ans)
            exit()


if __name__ == "__main__":
    resolve()


