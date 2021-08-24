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
    s=(input())
    #a, b = map(int, input().split())
    #A = list(map(int, input().split()))
    cnt=count=iti=0
    count=1
    for i in range(len(s)):
        #print(cnt)
        if s[i]=="*":
            if s[i-1]=="0" or s[i+1]=="0":
                count=0
            else:
                pass
        if s[i]=="+":
            if s[i-1]!="0" and count==1:
                cnt+=1
            count=1
            iti=i
    if "0" not in s[iti:]:
        cnt+=1
    print(cnt)
        






if __name__ == "__main__":
    resolve()


