class Solution:
    def climbStairs(self, n: int) -> int:
        arr=[0]*max(2,n)
        arr[0]=1
        arr[1]=2
        if(n<=2):
            return arr[n-1]
        for i in range(3,n+1):
            arr[i-1]=arr[i-2]+arr[i-3]
        return arr[n-1]
