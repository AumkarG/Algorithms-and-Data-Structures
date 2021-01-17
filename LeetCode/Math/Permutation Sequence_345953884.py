from math import factorial
import math


class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        digs=[i for i in range(1,n+1)]
        n-=1
        ans=""
        while(n!=0):
            print(digs)
            f=factorial(n)
            idx=k//f
            if(k//f==k/f):
                idx-=1
            d=digs.pop(idx)
            k=k%f
            ans+=str(d)
            n-=1
        ans+=str(digs[0])
        return ans
            
