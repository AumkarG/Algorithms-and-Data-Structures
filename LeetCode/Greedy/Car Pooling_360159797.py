class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        
        load = [0] * 1001
        occupancy = 0
        j=0
        for i in range(len(trips)):
            load[trips[i][1]] += trips[i][0]
            load[trips[i][2]] -= trips[i][0]
            j+=2
        k=0
        for i in load:
            if(i!=0): 
                occupancy += i
                k+=1
                if occupancy > capacity:
                    return False
                if(k>=j):
                    return True
        return True
