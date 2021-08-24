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
    n,m,x = map(int, input().split())
    SUM=[0]*(m+1)
    SUM[0]=100
    ans=10**10
    cnt=fun=0
    #A = list(map(int, input().split()))
    a = [list(map(int, input().split())) for l in range(n)]
    for i in range(2**n):
        for j in range(n):
            if ((i>>j)&1):
                cnt+=a[j][0]
                for z in range(1,m+1):
                    SUM[z]+=a[j][z]
        for k in range(1,m+1):
            if SUM[k]<x:
                fun=1
            SUM[k]=0
        if fun==0:
            if cnt<ans:
                ans=cnt
        fun=cnt=0
    if ans==10**10:
        ans=-1
    print(ans)

                    



if __name__ == "__main__":
    resolve()


