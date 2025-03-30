#!/usr/bin/env python3
from itertools import accumulate,chain,combinations,groupby,permutations,product
from collections import deque,Counter
from bisect import bisect_left,bisect_right
from math import gcd,sqrt,sin,cos,tan,degrees,radians,ceil,floor
from fractions import Fraction
from decimal import Decimal
import sys,copy
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
    #A = list(map(int, input().split()))
    A=[]
    B=[]
    for _ in range(m):
        a,b = map(int, input().split())
        A.append(a)
        B.append(b)
    k=int(input())
    C=[]
    D=[]
    CNT=[]
    for _ in range(k):
        c,d = map(int, input().split())
        C.append(c)
        D.append(d)
        #CNT.append(c)
    ans=0
    count=0
    for i in range(2**k):
        CNT=copy.copy(C)
        for j in range(k):
            #if((i>>j)&1):
            if ((i >> j) & 1):
                CNT[k-1-j]=D[k-1-j]
            #else:
                #CNT[k-1-j]=C[k-1-j]
        #print(CNT)
        for z in range(m):
            if A[z] in CNT and B[z] in CNT:
                ans+=1
        #print(ans)
        if count<ans:
            count=ans
        ans=0
    print(count)


    


if __name__ == "__main__":
    resolve()


