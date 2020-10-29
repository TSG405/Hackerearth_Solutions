'''
Problem Statement: https://www.hackerearth.com/practice/codemonk/
'''

for k in range(int(input())):
    n,k = list(map(int, input().split()))
    A = input()
    B = A
    c = 0
    for i in range(1, n+1):
        A = A[1:]+A[:1]
        if(max(A,B) != B):
            B = A
            c = i
    if(k == 1):
        print(c)
        continue
    A = B
    for j in range(k - 1):
        if ((j>0) and (x==n or B==A[x:]+A[:x])):
            c=c+(x*(k-2))
            break
        A = A[1:] + A[:1]
        x=1
        while( A != B):
            A = A[1:] + A[:1]
            x += 1
        c+=x
    print(c)
