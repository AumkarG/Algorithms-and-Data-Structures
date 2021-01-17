class Solution(object):
    def lengthOfLastWord(self, s):
        l=0
        l_past=0
        for i in s:
            if(l!=0):
                if(i==' '):
                    l_past=l
                    l=0
                else:
                    l+=1
            else:
                if(i!=' '):
                    l+=1
        if(l!=0):
            return l
        else:
            return l_past
        
            
