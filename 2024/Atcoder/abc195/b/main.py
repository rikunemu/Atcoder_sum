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
    a, b ,w= map(int, input().split())
    #A = list(map(int, input().split()))
    cnt="UNSATISFIABLE"
    count=(b-a)//2
    ans1=ans2=10**5
    w*=1000
    aa=kazo=0
    for i in range(a,count):
        if w%i==0:
            aa=w//i
            ans1=min(ans1,aa)
        for j in range(a+1,count):
            while aa<w:
                kazo+=1
                aaa=i*kazo
                if (w-aaa)%j==0:
                    ans1=min(ans1,(w-aaa)//j+kazo)
            kazo=0



if __name__ == "__main__":
    resolve()


