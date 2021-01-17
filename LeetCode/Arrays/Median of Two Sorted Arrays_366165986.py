class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        i=0
        j=0
        m=len(nums1)
        n=len(nums2)
        tot=0
        if((m+n)%2==0):
            ix=(m+n)//2-1
            s=0
            c=0
            while(1==1 and c<2):
                if(i<m and j<n):
                    if(tot==ix or tot==ix+1):
                        if(nums1[i]<nums2[j]):
                            s+=nums1[i]
                            i+=1
                        else:
                            s+=nums2[j]
                            j+=1
                        tot+=1
                        c+=1
                    else:
                        if(nums1[i]<nums2[j]):
                            i+=1
                        else:
                            j+=1
                        tot+=1                    
                elif(i==m):
                    if(tot==ix or tot==ix+1):
                        s+=nums2[j]
                        c+=1
                    j+=1
                    tot+=1
                else:
                    if(tot==ix or tot==ix+1):
                        s+= nums1[i]
                        c+=1
                    i+=1
                    tot+=1 
            return s/2
            
            
        else:
            ix=(m+n)//2
            while(1==1):
                if(i<m and j<n):
                    if(tot==ix):
                        if(nums1[i]<nums2[j]):
                            return nums1[i]
                        else:
                            return nums2[j]
                    else:
                        if(nums1[i]<nums2[j]):
                            i+=1
                        else:
                            j+=1
                        tot+=1                    
                elif(i==m):
                    if(tot==ix):
                        return nums2[j]
                    else:
                        j+=1
                        tot+=1
                else:
                    if(tot==ix):
                        return nums1[i]
                    else:
                        i+=1
                        tot+=1
                        
