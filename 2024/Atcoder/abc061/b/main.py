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
    CNT=[0]*n
    #A = list(map(int, input().split()))
    for i in range(m):
        a,b = map(int, input().split())
        CNT[a-1]+=1
        CNT[b-1]+=1
    print(*CNT,sep="\n")

if __name__ == "__main__":
    resolve()


