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
    h,w,x,y = map(int, input().split())
    S = []
    for _ in range(h):
        S.append(input())
    #print(S[0][2])
    x-=1
    y-=1
    xx=x
    yy=y
    ans=0
    if S[xx][yy]=="#":
        print(ans)
        exit()
    xx+=1
    while xx<h:
        if S[xx][yy]==".":
            ans+=1
        else:
            break
        xx+=1
    xx=x
    xx-=1
    while xx>=0:
        #print(S[xx][yy])
        if S[xx][yy]==".":
            ans+=1
        else:
            break
        xx-=1
    xx=x
    yy+=1
    while yy<w:
        if S[xx][yy]==".":
            ans+=1
        else:
            break
        yy+=1
    yy=y
    yy-=1
    while yy>=0:
        if S[xx][yy]==".":
            ans+=1
        else:
            break
        yy-=1
    print(ans+1)
    


if __name__ == "__main__":
    resolve()


