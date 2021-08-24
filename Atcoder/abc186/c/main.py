#!/usr/bin/env python3
# coding: utf-8
# Your code here!
n=int(input())
cnt=0
ans=0
for i in range(1,10**6):
    #print(i)
    if i>n:
        break
    ans=str(i)
    if ans.count("7")>=1:
        cnt+=1
    if ans.count("7")==0 and oct(int(ans)).count("7")>=1:
        cnt+=1
print(n-cnt)
    
    



