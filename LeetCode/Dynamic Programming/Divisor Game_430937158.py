import math

class Solution:
    def divisorGame(self, N: int) -> bool:
        arr=[-1]*N
        for i in range(2,N+1):
            flg=0
            lim=int(math.sqrt(i))+1
            for j in range(1,lim):
                if i%j==0 and arr[i-j-1]==-1:
                    flg=1
                    break
            if(flg==1):
                arr[i-1]=1
        return arr[N-1]==1
                
                           
        
