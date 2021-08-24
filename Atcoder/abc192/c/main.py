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
    n,k = map(int, input().split())
    ans=n
    #A = list(map(int, input().split()))
    n=str(n)
    #tisa=sorted(n)
    #deka = sorted(n, reverse=True)
    #na=[i for i in n if i !="0"]
    #print(na)
    a=aa=0
    
    for i in range(k):
        #na=[i for i in n if i !="0"]
        deka = sorted(n, reverse=True)
        tisa=sorted(n)
        #print(deka)
        #print(tisa)
        cnt=len(deka)
        for i in range(len(deka)):
            a+=int(deka[i])*10**(cnt-1)
            aa+=int(tisa[i])*10**(cnt-1)
            cnt-=1
        

        n=a-aa
        #print(a)
        #print(aa)
        if ans==n:
            print(ans)
            exit()
        ans=n
        n=str(n)
        a=aa=0
    print(n)



if __name__ == "__main__":
    resolve()


