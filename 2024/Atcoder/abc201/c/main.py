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
    cnt=ans=0
    count=0
    for i in range(len(s)):
        if s[i]=="o":
            cnt+=1
    if cnt>=5:
        print(ans)
        exit()
    #print(s[0]+s[1])
    ANS=[0]*10
    for i in range(0,10):
        for j in range(0,10):
            for z in range(0,10):
                for k in range(0,10):
                    if s[i]=="o":
                        ANS[i]+=1
                    if s[j]=="o":
                        ANS[j]+=1
                    if s[z]=="o":
                        ANS[z]+=1
                    if s[k]=="o":
                        ANS[k]+=1
                    #print((str(i)+str(j)+str(z)+str(k)))
                    #print((sum([u > 0 for u in ANS])))
                    #print(ANS)
                    if (sum([u >= 1 for u in ANS]))>=cnt:
                    #a=(str(i)+str(j)+str(z)+str(k))

                    #c=Counter(a)
                    #if len(c)>=cnt:

                        if (s[i]+s[j]+s[z]+s[k]).count('o')>=cnt:
                            if (s[i]+s[j]+s[z]+s[k]).count('x')==0:
                                ans+=1
                                #print("unko")
                    ANS=[0]*10
                
    #print(c)
    print(ans)



if __name__ == "__main__":
    resolve()


