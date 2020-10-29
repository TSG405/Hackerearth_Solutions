'''
Problem Statement: https://www.hackerearth.com/challenges/competitive/codemonk-arrays-strings/algorithm/monk-and-rotation-3/
'''


t=int(input())
while(t):
    n,k=list(map(int,input().split()))
    f=list(map(int,input().split()))
    re=k%n
    temp=f[:n-(re)]
    temp1=f[n-(re):]
    nf=temp1+temp
    for un in nf:
        print(un,end=" ")
    print("\n")
    t=t-1
