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
    A=[]
    #a, b = map(int, input().split())
    #A = list(map(int, input().split()))
    for i in range(n):
        A.append((i+1,int(input())))
    cnt=1
    ans=A[0][1]
    #print(ans)
    for i in range(1,n):
        if ans==2:
            print(cnt)
            exit()
        ans=A[ans-1][1]
        cnt+=1
    print(-1)



if __name__ == "__main__":
    resolve()


