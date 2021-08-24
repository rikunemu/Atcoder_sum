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
    
    cnt=0
    a,b = map(int, input().split())
    if (b-a)<=4000:

        for i in range(a,b+1):
            for j in range(i+1,b+1):
                ans=gcd(i,j)
                if cnt<ans:
                    cnt=ans
    else:
        for i in range(2,10**5):
            
            ans=b//i
            #print(ans)
            if (b-a)>=ans:
                print(ans)
                exit()
            
    print(cnt)

    

if __name__ == "__main__":
    resolve()


