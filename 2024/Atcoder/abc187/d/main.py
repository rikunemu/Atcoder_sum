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
    ANS=[]
    ANS1=[]
    aans=bans=0
    ans=cnt=cnt1=0
    for i in range(n):
        a, b = map(int, input().split())
        aans+=a
        bans+=b
        ANS.append((a,b))
        ANS1.append((2*a+b,a))

    ANS = sorted(ANS, key=lambda x:(-x[0],-x[1]),reverse=True)
    #print(ANS)
    bans=aans
    for i in range(n):
        aans-=ANS[i][0]
        ans+=ANS[i][0]+ANS[i][1]
        cnt+=1
        if ans>aans:
            #print(cnt)
            break
    ANS1 = sorted(ANS1, key=lambda x:(x[0],x[1]),reverse=True)
    #print(ANS1)
    ans=0
    for i in range(n):
        #bans-=ANS1[i][1]
        ans+=ANS1[i][0]
        cnt1+=1
        if ans>bans:
            #print(cnt)
            break   
    
    print((cnt1))




if __name__ == "__main__":
    resolve()


