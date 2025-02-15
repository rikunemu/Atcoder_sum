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
    # n=int(input())
    N, Q = map(int, input().split())
    #A = list(map(int, input().split()))
    ans = 0
    cnt = [0] + [1] * N
    # 0,1,2,3,4,5 と増えていく感じ
    pos = list(range(N+1))

    for q in range(Q):
        query = list(map(int, input().split()))
        if query[0] == 2:
            print(ans)
        if query[0] == 1:
            P = query[1]
            H = query[2]
            # 鳩が移動したため-1
            cnt[pos[P]] -=1
            # 鳩が移動してカウントが1になったか確認
            if cnt[pos[P]] == 1:
                ans -=1
            # 鳩がどの場所にいるの確認
            pos[P] = H 
            # 巣に移動したため1増やす
            cnt[pos[P]] += 1
            # 複数いるか確認
            if cnt[pos[P]] == 2:
                ans += 1


            


if __name__ == "__main__":
    resolve()