# cook your dish here
import math
T=int(input())
ans1=[]
ans2=[]
for i in range(T):
    n=i+1
    N=n
    print("N =",N)
    x=(n)*(n+1)/2
    j=0
    if(x%2==1):
        j=0
    else:
        t=n*n+n
        t/=2
        k=int(math.sqrt(t))
        if (k*k+k)>t:
            k=k-1
        t=k
        z=int(t*(t+1)/2)
        y=int(x/2)
        if(z== x/2):
            p=n-t
            a=(t)*(t-1)/2
            b=p*(p+1)/2
            j=int(a+b)
        else:
            j=n-t
    

    ans1.append(j)
    n=N
    t=x/2
    c=0
    for i in range(n-1):
        for j in range(i+1,n):
            arr=[p for p in range(1,n+1)]
            swp=arr[i]
            ar
            r[i]=arr[j]
            arr[j]=swp
            summ=0
            for z in arr[::-1]:
                if summ+z==t:
                    c+=1
                    break
                if summ+z>t:
                    break
                summ+=z

    ans2.append(c)

for i in range(N):
    if(ans1[i]!=ans2[i]):
        print(ans1[i],ans2[i],i+1)


