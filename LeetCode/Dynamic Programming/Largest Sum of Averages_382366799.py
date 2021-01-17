class Solution(object):
    def largestSumOfAverages(self, A, K):
        sm=[A[0]]
        mat=[A[0]]
        l=len(A)
        if(K==1):
            return(float(sum(A))/l)
        for i in range(1,l):
            sm.append(sm[i-1]+A[i])
            mat.append(float(sm[i])/(i+1))
   
        for j in range(2,K+1):
            mat_new=[]
            for t in range(j-1):
                mat_new.append(mat[t])
            for k in range(j-1,l):
                mx=-1
                mat_new.append(-1)
                for i in range(0,k):
                    z = float(sm[k]-sm[i])/(k-i)
                    if (z + mat[i])>mx:
                        mx= z + mat[i]
                mat_new[k] = mx
            mat=mat_new
        return(mat[l-1])
