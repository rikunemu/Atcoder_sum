#!/usr/bin/env python3
from itertools import accumulate,chain,combinations,groupby,permutations,product
import collections
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
    ANS1=[]
    ANS2=[]
    for i in range(n):
        S=input()
        if S[0]=="!":
            ANS1.append(S)
        else:
            ANS2.append(S)
    #print(ANS1)
    #ANS1=set(ANS1)
    #ANS2=set(ANS2)
    #print(ANS2)
    c=collections.Counter(ANS2)
    for i in ((ANS1)):
        #cnt=c[i[1:]]
        if c[i[1:]]>=1:
            print(i[1:])
            exit()
    print("satisfiable")
    


if __name__ == "__main__":
    resolve()


