import math
class Solution(object):
    def splitIntoFibonacci(self, S):
        n=len(S)
        res=[]
        larg=math.pow(2,31)-1
        for i in range(1,n-1):
            n1=int(S[:i])
            if(n1>larg or (i>1 and S[0]=='0')):
                break
            for j in range(i+1,n):
                x=S[i:j]
                if(len(x)>1 and x[0]=='0'):
                    break
                n2=int(S[i:j])
                if(n2>larg):
                    break
                s=n1+n2
                l=len(str(s))
                if(j+l<=n):
                    k=j
                    res=[n1,n2]
                    while(1==1):
                        y=int(S[k:k+l])
                        if(y>larg):
                            res=[]
                            break
                        if(y==s):
                            res.append(S[k:k+l])
                            if(k+l==n):
                                return res
                            n1=n2                        
                            n2=int(S[k:k+l])
                            s=n1+n2
                            k=k+l
                            l=len(str(s))
                            if(k+l>n):
                                n1=int(S[:i])
                                res=[]
                                break
                        else:
                            n1=int(S[:i])
                            res=[]
                            break
                    
                else: 
                    break
        return res
