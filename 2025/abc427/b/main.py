#!/usr/bin/env python3
from itertools import accumulate,chain,combinations,groupby,permutations,product
from collections import deque,Counter
from bisect import bisect_left,bisect_right
from math import gcd,sqrt,sin,cos,tan,degrees,radians,ceil,floor
from fractions import Fraction
from decimal import Decimal
import sys

# 入力
def rI(): return int(sys.stdin.readline().rstrip())
def rLI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def rI1(): return (int(sys.stdin.readline().rstrip())-1)
def rLI1(): return list(map(lambda a:int(a)-1,sys.stdin.readline().rstrip().split()))
def rS(): return sys.stdin.readline().rstrip()
def rLS(): return list(sys.stdin.readline().rstrip().split())

#rstripが必要なことも
#input = lambda: sys.stdin.readline().rstrip()
#inputの高速化、基本はいらない、入力が長いときに使用
#from sys import setrecursionlimit
#setrecursionlimit(10**7)
MOD=10**9+7
INF=float('inf')
#float型の無限大inf
n=int(input())
#a, b = map(int, input().split())
#A = list(map(int, input().split()))
ans=1
SUM=[0]*(n+1)
SUM[0]=1
SUM[1]=1
for i in range(2,n+1):
    ans=0
    for j in range(i):
        nn=str(SUM[j])
        anssine=0
        for z in range(len(str(nn))):
            anssine+=int(nn[z])
        ans+=anssine
    SUM[i]=ans
print(SUM[n])
