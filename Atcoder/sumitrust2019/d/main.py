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
    S=input()
    S = [int(s) for s in S]
    #S=list(map(int, input().split()))
    ans=0
    for q in product(range(10),repeat=3):
        #print(q)
        i=0
        for s in S:
            if s==q[i]:
                if i==2:
                    ans+=1
                    break
                else:
                    i+=1
    print(ans)


if __name__ == "__main__":
    resolve()


