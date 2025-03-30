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
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    #A=set(A)
    #B=set(B)
    ANS=list(A)+list(B)
    #ANS=ANS.sort()
    ANS.sort()
    #print(ANS)
    ans=10**10
    cnt=10**10
    for i in range(len(ANS)-1):
        if A.count(ANS[i])==1 or A.count(ANS[i+1])==1:
            cnt=abs(ANS[i]-ANS[i+1])

        
        if ans>cnt:
            ans=cnt
    print(ans)


if __name__ == "__main__":
    resolve()


