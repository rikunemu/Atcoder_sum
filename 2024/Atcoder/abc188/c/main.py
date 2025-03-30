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
    A = list(map(int, input().split()))
    max1=max2=cnt1=cnt2=0
    max1=A[0]
    cnt1=1
    for i in range(1,2**n//2):
        if max1<A[i]:
            max1=A[i]
            cnt1=i+1
    max2=A[2**n//2]
    cnt2=2**n//2+1
    for i in range(2**n//2,2**n):
        if max2<A[i]:
            max2=A[i]
            cnt2=i+1   
    #print(max1,max2)
    if max1>max2:
        print(cnt2)
    else:
        print(cnt1)

    
    

if __name__ == "__main__":
    resolve()


