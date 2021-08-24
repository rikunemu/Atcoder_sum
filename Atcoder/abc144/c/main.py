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
def make_divisors(n):
    lower_divisors , upper_divisors = [], []
    i = 1
    while i*i <= n:
        if n % i == 0:
            lower_divisors.append(i)
            if i != n // i:
                upper_divisors.append(n//i)
        i += 1
    return lower_divisors + upper_divisors[::-1]
def resolve():
    n=int(input())
    ANS=(make_divisors(n))
    ans=ans1=10**12
    for i in range(len(ANS)):
        for j in range(i,len(ANS)):
            if ANS[i]*ANS[j]==n:
                ans=ANS[i]+ANS[j]
                if ans<ans1:
                    ans1=ans
    print(ans1-2)
    #print(ANS)
    #if len(ANS)%2==0:
        #ans=ANS[len(ANS)//2-1]+ANS[len(ANS)//2]
        #print(ans-2)
    #else:
        #ans=ANS[len(ANS)//2-1]+ANS[len(ANS)//2+1]
        #print(ans-2)

    #a, b = map(int, input().split())
    #A = list(map(int, input().split()))

if __name__ == "__main__":
    resolve()


