def cost(i,j,cs,bs,k):
    if abs(bs[i]-bs[j])>0:
        return False
    else:
        c=k+1-abs(i-j)-abs(cs[i]-cs[j])
        if c>0:
            return True
        else:
            return False
T=int(input())
for k in range(T):
    n,k=[int(x) for x in input().split()]
    s=input()
    l=len(s)
    cs=[0]*n
    bs=[0]*n
    if(s[0]==':'):
        cs[0]=1
    if(s[0]=='X'):
        bs[0]=1
    mag=[]
    iron=[]
    for i in range(0,n):
        if s[i]==':':
            cs[i]=cs[i-1]+1
        else:
            cs[i]=cs[i-1]
        if s[i]=='X':
            bs[i]=bs[i-1]+1
        else:
            bs[i]=bs[i-1]
    count=0
    for i in range(0,n):
        if s[i]=='I':
            if(len(mag)==0):
                iron.append(i)
            else:
                flag=0
                j=0
                while(j<len(mag)):
                    m=mag[j]
                    if cost(m,i,cs,bs,k):
                        count+=1
                        mag.pop(j)
                        flag=1
                        break
                    else:
                        mag.pop(j)
                if(flag==0):
                    iron.append(i)
        if s[i]=='M':
            if(len(iron)==0):
                mag.append(i)
            else:
                flag=0
                j=0
                while j<len(iron):
                    z=iron[j]
                    if cost(i,z,cs,bs,k):
                        count+=1
                        iron.pop(j)
                        flag=1
                        break
                    else:
                        iron.pop(j)
                if(flag==0):
                    mag.append(i)
    print(count)
            
                        
        
            
            
    
