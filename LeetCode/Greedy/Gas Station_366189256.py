class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n=len(gas)
        x=[0]*n
        i=0
        while(i<n):
            if(gas[i]>=cost[i]):
                j=i
                t=0
                t+=gas[j]-cost[j]
                x=j
                j=(j+1)%n
                while(j!=x and t>=0):
                    t+=gas[j]-cost[j]
                    if(t>=0):
                        j=(j+1)%n
                if(j==x):
                    return x
                elif(j==x-1):
                    return -1
                else:
                    i=max(j+1,i+1)
            else:
                i+=1
    
        return -1
            
            
        
