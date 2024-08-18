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

def decimal_normalize(value):
    """
    浮動小数点数の場合、末尾の不要な0を削除する。
    整数値の場合、そのまま整数として返す。

    Parameters
    ----------
    value : float or int
        対象となる数値。

    Returns
    -------
    int or float
        不要な末尾の0が削除された数値。
    """
    if isinstance(value, float) and value.is_integer():
        return int(value)
    return value

def resolve():
    x=float(input())
    #a, b = map(int, input().split())
    #A = list(map(int, input().split()))
    print(decimal_normalize(x))

if __name__ == "__main__":
    resolve()