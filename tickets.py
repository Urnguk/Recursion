N=int(input())
A=[0]*N
B=[0]*N
C=[0]*N
for i in range(N):
    A[i],B[i],C[i]=list(map(int, input().split()))
Price=[0]*N
Price[0]=min(min(A[0],B[0]),C[0])
if N==1:
    print(Price[0])
elif N==2:
    print(min(min(Price[0]+A[1],B[0]),C[0]))

else:
    Price[1]=min(min(Price[0]+A[1],B[0]),C[0])
    Price[2]=min(min(Price[1]+A[2],Price[0]+B[1]),C[0])
    for i in range(3,N):
        Price[i]=min(min(Price[i-1]+A[i], Price[i-2]+B[i-1]),Price[i-3]+C[i-2])
    print(Price[N-1])
