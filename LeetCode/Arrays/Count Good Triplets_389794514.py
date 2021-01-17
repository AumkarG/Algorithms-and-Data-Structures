class Solution(object):
    def countGoodTriplets(self, arr, a, b, c):
        n=len(arr)
        count=0
        for i in range(0,n-2):
            for j in range(i+1,n-1):
                d1=abs(arr[i]-arr[j])
                if(d1<=a):
                    for k in range(j+1,n):
                        d2=abs(arr[j]-arr[k])
                        d3=abs(arr[k]-arr[i])
                        if(d2<=b and d3<=c):
                            count+=1    
        return count
