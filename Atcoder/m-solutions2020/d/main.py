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
    cnt=0
    #a, b = map(int, input().split())
    A = list(map(int, input().split()))
    dp=[0]*(n+1)
    dp[0]=1000
    for i in range(n-1):
        
        dp[i+1]=max(dp[i],dp[i]//A[i]*A[i+1]+dp[i]%A[i])
        #if dp[i]<dp[i]//A[i]*A[i+1]:
            #cnt=dp[i]%A[i]
        #print(dp[i+1])
    #dp[n]=max(dp[n-1],dp[n-1]//A[n-2]*A[n-1])
    print(dp[n-1])

if __name__ == "__main__":
    resolve()


