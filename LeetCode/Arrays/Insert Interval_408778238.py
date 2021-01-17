class Solution(object):
    def insert(self, intervals, newInterval):
        fin=[]
        done=False
        for i in intervals:
            merge=False
            if(i[1]>=newInterval[0] and i[1]<=newInterval[1]):
                merge=True
            elif(i[0]>=newInterval[0] and i[0]<=newInterval[1]):
                merge=True
            elif(i[0]<=newInterval[0] and i[1]>=newInterval[0]):
                merge=True
            if(merge==True):
                newInterval=[min(newInterval[0],i[0]),max(newInterval[1],i[1])]
            else:
                if(newInterval[0]<i[0] and done==False):
                    fin.append(newInterval)
                    done=True
                fin.append(i)
        if(done==False):
            fin.append(newInterval)
        return fin
            
