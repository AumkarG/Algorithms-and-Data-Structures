class MyCircularDeque:
    
    

    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the deque to be k.
        """
        self.arr=[]
        self.k=k
        self.l=0
        

    def insertFront(self, value: int) -> bool:
        """
        Adds an item at the front of Deque.
        Return true if the operation is successful.
        """
        if(self.l<self.k):
            ar1=[value]
            ar1.extend(self.arr)
            self.arr=ar1
            self.l+=1
            return True
        return False
        

    def insertLast(self, value: int) -> bool:
        """
        Adds an item at the rear of Deque. Return true if the operation is successful.
        """
        if(self.l<self.k):
            self.arr.append(value)
            self.l+=1
            return True
        return False
        
        

    def deleteFront(self) -> bool:
        """
        Deletes an item from the front of Deque. Return true if the operation is successful.
        """
        if(self.l>0):
            self.arr=self.arr[1:]
            self.l-=1
            return True
        return False
        

    def deleteLast(self) -> bool:
        """
        Deletes an item from the rear of Deque. Return true if the operation is successful.
        """
        if(self.l>0):
            self.arr=self.arr[:self.l-1]
            self.l-=1
            return True
        return False
        

    def getFront(self) -> int:
        """
        Get the front item from the deque.
        """
        if(self.l>0):
            return self.arr[0]
        return -1

    def getRear(self) -> int:
        """
        Get the last item from the deque.
        """
        if(self.l>0):
            return self.arr[self.l-1]
        return -1
    
    def isEmpty(self) -> bool:
        """
        Checks whether the circular deque is empty or not.
        """
        return(self.l==0)

    def isFull(self) -> bool:
        """
        Checks whether the circular deque is full or not.
        """
        return(self.l==self.k)

# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()
