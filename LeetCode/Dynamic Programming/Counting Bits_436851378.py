class Solution:
    def countBits(self, num: int) -> List[int]:
        if num==0:
            return [0]
        if num==1:
            return [0,1]
        res=[0,1]
        i=1
        while 2**i<=num:
            if 2**(i+1)<=num:
                l=len(res)
                for j in res[0:l]:
                    res.append(j+1)
            else:
                left=num-2**i+1
                l=len(res)
                for j in res[0:left]:
                    res.append(j+1)
            i+=1
        return res
            
            
        
