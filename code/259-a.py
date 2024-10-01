N,M,X,T,D = map(int,input().split())
L = [T-X*D+i*D if i<X else T for i in range(N+1)]
print(L[M])