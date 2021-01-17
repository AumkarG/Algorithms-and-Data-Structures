
N=int(input())
X=[int(i) for i in input().split()]
lng=[]
for i in range(N):
    lng.append([])

lng[0].append(X[0])

for i in range(1,N):
    app=[]
    maxl=0
    loc=-1
    for j in range(i):
        if(X[j]>X[i]):
            if(len(lng[j])>maxl):
                maxl=len(lng[j])
                loc=j
    if(loc==-1):
        app.append(X[i])
    else:
        app.extend(lng[loc])
        app.append(X[i])
    lng[i]=app

mx=0
maxarr=[]
for i in lng:
    if(len(i)>mx):
        maxarr=i
        mx=len(i)

print(maxarr)
