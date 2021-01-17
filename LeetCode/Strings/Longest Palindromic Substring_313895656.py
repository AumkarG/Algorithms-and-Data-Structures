class Solution(object):
    def longestPalindrome(self, s):
        l=len(s)
        ind=0
        mx=1
        for i in range(l):
            flag=1
            count=0
            while(flag==1 and i-count>=0 and i+count<l):
                if(s[i-count]==s[i+count]):
                    count+=1
                else:
                    flag=0
            if((count-1)*2+1>mx):
                mx=2*(count-1)+1
                ind=i
        
        tp=0
        print(mx)
        print(ind)
        for i in range(l-1):
            flag=1
            count=0
            while(flag==1 and i-count>=0 and i+count+1<l):
                if(s[i-count]==s[i+count+1]):
                    count+=1
                else:
                    flag=0
            if(count*2>mx):
                tp=1
                mx=2*count
                ind=i
        if(tp==0):
            return(s[ind-(mx-1)/2:ind+(mx+1)/2])
        else:
            return(s[ind-mx/2+1:ind+mx/2+1])
