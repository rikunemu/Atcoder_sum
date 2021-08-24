#!/usr/bin/env python3
from itertools import accumulate,chain,combinations,groupby,permutations,product
from collections import deque,Counter
from bisect import bisect_left,bisect_right
from math import gcd,sqrt,sin,cos,tan,degrees,radians,ceil,floor,factorial
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
    a, b,k= map(int, input().split())
    aa=bb=0
    #A = list(map(int, input().split()))
    cnt=factorial(a+b)//(factorial(a)*factorial(b))
    ANS=[]
    #print(cnt)
    for i in range(a+b):
        if ceil(cnt/2)>=k:
            ANS.append("a")
            aa+=1
            cnt=ceil(cnt/2)
            k-=ceil(cnt/2)
        else:
            ANS.append("b")
            bb+=1
            cnt=ceil(cnt/2)
            k-=ceil(cnt/2)
        if aa>=a or bb>=b:
            break
    #print("".join(ANS))
    ans="a"*(a-aa)+"b"*(b-bb)
    #print(ans)
    ANS.append(ans)
    #ANS[::-1]
    print("".join(ANS))



if __name__ == "__main__":
    resolve()


