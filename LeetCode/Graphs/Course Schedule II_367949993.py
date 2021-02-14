class Solution(object):
    def findOrder(self, n , prerequisites):
        adj=[]
        for i in range(n):
            adj.append([])
        ind=[0]*n
        for i in prerequisites:
            adj[i[1]].append(i[0])
            ind[i[0]]+=1
        queue=[]
        for i in range(n):
            if(ind[i]==0):
                queue.append(i)
        visit=[0]*n
        vcount=0
        course=[]
        for i in queue:
            vcount+=1
            visit[i]=1
            course.append(i)
            for x in adj[i]:
                if(visit[x]==0):
                        ind[x]-=1
                        if(ind[x]==0):
                            visit[x]=1
                            queue.append(x)
        if(vcount<n):
                return []
        return course
