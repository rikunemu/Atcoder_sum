#!/usr/bin/env python3
from itertools import accumulate,chain,combinations,groupby,permutations,product
from collections import deque,Counter
from bisect import bisect_left,bisect_right
from math import gcd,sqrt,sin,cos,tan,degrees,radians,ceil,floor
from fractions import Fraction
from decimal import Decimal
import sys,math
#rstripが必要なことも
#input = lambda: sys.stdin.readline().rstrip()
#inputの高速化、基本はいらん、入力が長いときに使用
#from sys import setrecursionlimit
#setrecursionlimit(10**7)
MOD=10**9+7
INF=float('inf')
#float型の無限大inf

def has_duplicates(seq):
    return len(seq) - len(set(seq))

def resolve():
    #n=int(input())
    n, m = map(int, input().split())
    a = [[] for _ in range(n+1)]
    cnt=0
    for _ in range(m):
        u, v = map(int, input().split())
        if u != v:
            a[u].append(v)
            a[v].append(u)
        else:
            cnt+=1
    count=0
    #print(a)
    for i in range(n+1):
        count+=has_duplicates(a[i])
    print(cnt+math.ceil(count/2))
        

if __name__ == "__main__":
    resolve()