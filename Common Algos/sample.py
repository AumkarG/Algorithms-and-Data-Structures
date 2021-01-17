n=int(input())
s=str(2*n-1)
l=len(s)
if(n<=4):
    print(n*(n-1)/2)
else:
    t=0
    lst=[]
    for i in s:
        if(i!='9'):
            t=1
            break
    if(t==0):
        print(1)
    else:
        t=0
        for j in s[1:]:
            if(j!='9'):
                t=1
                break
        if(t==0):
            lst.append(int(s))
        k=int(s[0])-1
        x=''.join(map(str, ['9']*(l-1)))

        while(k>0):
            lst.append(int(str(k)+x))
            k-=1
        if(len(s)!=1):       
            lst.append(int(x))
        s=0
        print(lst)
        for i in lst:
            if(n<i):
                s+=int(i//2)
                s-=(i-n-1)
            else:
                s+=int(i//2)
        print(s)
