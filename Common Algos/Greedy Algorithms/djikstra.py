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


print("Enter source and destination")
source,dest=[int(i) for i in input().split()]

visit=[0]*v

dist=[100000]*v
dist[source]=0

total=0

while(total!=v):        
    minm=100000
    close=-1
    for i in range(v):
        if visit[i]==0 and dist[i]<=minm:
            close=i
            minm=dist[i]
    visit[close]=1
    for ad in ll[close]:
        if dist[close]+adj[close][ad]<dist[ad]:
            dist[ad]=dist[close]+adj[close][ad]
    total+=1

print("Shortest path to destination",dist[dest])

