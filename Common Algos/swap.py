

passw=['abcd','cdab','adcb']

lst=[]
for i in passw:
    x=[0]*26
    y=[0]*26
    c=1
    for j in i:
        if(c%2==1):
            x[ord(j)-97]+=1
        else:
            y[ord(j)-97]+=1
        c+=1
    lst.append([x,y])
tot=0
i=0
while(i<len(lst)):
    k=i+1
    while(k<len(lst)):
        flag=0
        for p in range(26):
            if(lst[i][0][p]!=lst[k][0][p] or lst[i][1][p]!=lst[k][1][p]):
                flag=1
                break
        if(flag==0):
            lst.pop(k)
            k+=0
        else:
            k+=1
    tot+=1
    i+=1
print(tot)