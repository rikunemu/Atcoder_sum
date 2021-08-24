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
    q=int(input())
    #a, b = map(int, input().split())
    #A = list(map(int, input().split()))
    ANS=[]
    for i in range(q):
        A = list(map(int, input().split()))
        if A[i][0]==1:
            ANS.append(A[i][1])
        if A[i][0]==2:
            ANS= list(map(lambda x: x+ ANS[i][1],ANS))
        if A[i][0]==3:
            a=min(ANS)
            print(a)
            ANS.remove(a)




if __name__ == "__main__":
    resolve()


