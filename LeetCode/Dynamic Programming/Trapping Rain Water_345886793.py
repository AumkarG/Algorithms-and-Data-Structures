class Solution(object):
    def trap(self, height):
        l=len(height)
        if(l<3):
            return 0
        mxr=[-1]*(l-2)
        mxl=[-1]*(l-2)
        mxl[0]=height[0]
        for i in range(1,l-2):
            if(height[i]>mxl[i-1]):
                mxl[i]=height[i]
            else:
                mxl[i]=mxl[i-1]
        mxr[l-3]=height[l-1]
        for i in range(1,l-2):
            if(height[l-1-i]>mxr[l-2-i]):
                mxr[l-3-i]=height[l-1-i]
            else:
                mxr[l-3-i]=mxr[l-i-2]
    
        sum=0
        for i in range(l-2):
            m=min(mxr[i],mxl[i])
            if(m>height[i+1]):
                sum+=m-height[i+1]
        return sum;
