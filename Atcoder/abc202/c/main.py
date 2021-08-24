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
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = list(map(int, input().split()))
    ans=0
    CNT=[0]*(n+1)
    a=1
    Acnt=Counter(A)
    values, counts = zip(*Acnt.most_common())
    #print(Acnt)
    #print(values[0])
    #for i in range(n):
        #B[i]=[i+1,B[i]]
    for i in range(n):
        CNT[B[C[i]-1]]+=1
    #print(CNT)
    #a=CNT[values[0]]
    for value,count in zip(values,counts):
        ans+=CNT[value]*count
    print(ans)





if __name__ == "__main__":
    resolve()


