print("Enter number of vertices")
v=int(input())
print("Enter number of edges")
e=int(input())
adj=[]
for i in range(v):
    adj.append([0]*v)

ll=[]
for i in range(v):
    ll.append([])

print("Enter edges and weights")
for i in range(e):
    x,y,w=[int(j) for j in input().split()]
    adj[x][y]=w
    adj[y][x]=w
    ll[x].append(y)
    ll[y].append(x)


dist=[100000]*v
dist[0]=0
visited=[0]*v
tot=0
length=0
flag=0
while(tot<v):
    idx=-1
    minm=99999
    print(visited)
    print(dist)
    for i in range(v):
        if dist[i]<minm and visited[i]==0:
            minm=dist[i]
            idx=i
    if idx!=-1:
        visited[idx]=1
        length+=dist[idx]
        for q in ll[idx]:
            if visited[q]==0:
                dist[q]=min(dist[q],adj[idx][q])
        tot+=1
    else:
        print("CANNOT FORM MINIMAL SPANNING TREE")
        flag=1
        break
    
if flag==0:
    print(length)