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
    #a, b = map(int, input().split())
    #A = list(map(int, input().split()))
    a,a1,a2,a3=0,0,0,0
    for i in range(4):
        S=(input())
        if S=="H":
            a+=1
        if S=="2B":
            a1+=1
        if S=="3B":
            a2+=1
        if S=="HR":
            a3+=1
    if a1==1 and a==1 and a2==1 and a3==1:
        print("Yes")
    else:
        print("No")

if __name__ == "__main__":
    resolve()


