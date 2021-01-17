def BFS(strt,adj,N):

    queue=[]
    queue.append(strt)
    q=[]
    final=[]
    final=[[strt]]
    print(final)
    while(len(queue)!=0 or len(q)!=0):
        print(final)
        x=queue.pop(0)
        print(x,final)
        for i in range(N):
            if adj[x][i]==1 and vis[i]==0:
                q.append(i)
                vis[i]=1
        if(len(queue)==0):
            print(q)
            if(len(q)!=0):
                queue.extend(q)
                final.append(q)
                q=[]
    print(final)
      



N=int(input())
E=int(input())

adj=[]
for i in range(N):
    adj.append([0]*N)

for i in range(E):
    x,y=[int(i) for i in input().split()]
    adj[x][y]=1



BFS(0,adj,N)

