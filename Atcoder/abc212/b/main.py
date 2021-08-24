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
    x=(input())
    cnt=0
    ans=0
    #a, b = map(int, input().split())
    #A = list(map(int, input().split()))
    for i in range(len(x)-1):
        if x[i]==x[i+1]:
            cnt+=1
        if int(x[i])==int(x[i+1])-1:
            ans+=1
        if int(x[i])==9 and int(x[i+1])==0:
            ans+=1
    if cnt==3 or ans==3:
        print("Weak")
    else:
        print("Strong")

if __name__ == "__main__":
    resolve()


