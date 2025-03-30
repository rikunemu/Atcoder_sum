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
    n,m = map(int, input().split())
    ANS=[0]*(m*(m+1)//2)
    cnt=0
    #A = list(map(int, input().split()))
    for i in range(n):
        cnt=0
        A = list(map(int, input().split()))
        for j in range(m):
            for z in range(j,m):
                ANS[cnt]+=max(A[j],A[z])
                cnt+=1
    print(max(ANS))





if __name__ == "__main__":
    resolve()


