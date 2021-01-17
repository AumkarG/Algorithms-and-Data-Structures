class Solution(object):
    def lengthOfLongestSubstring(self, s):
        arr=dict()
        l=0
        grl=0
        low=0
        for i in range(len(s)):
            if(s[i] in arr):
                ix=arr[s[i]]
                if(ix<low):
                    l+=1 
                    arr[s[i]]=i
                else:  
                    if(l>grl):
                        grl=l
                    l=i-ix
                    arr[s[i]]=i      
                    low=ix+1
            else:
                l+=1 
                arr[s[i]]=i
        if(l>grl):
            grl=l    
        return grl
        
