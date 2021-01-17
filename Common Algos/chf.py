import math
T=int(input())
for i in range(T):
    n=i+1
    N=n
    x=(n)*(n+1)/2
    if(x%2==1):
        blob=0
    else:
        t=n*n+n
        t/=2
        k=int(math.sqrt(t))
        while(k*k+k)>t:
            k=k-1
        t=k
        z=int(t*(t+1)/2)
        y=int(x/2)
        if(z==x/2):
            p=n-t
            a=(t)*(t-1)/2
            b=p*(p+1)/2
            j=int(a+b)
            print(j,k,N)
        else:
            j=n-t
