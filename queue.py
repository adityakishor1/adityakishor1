class MyCircularQueue():
    def __init__(self,k):
        self.k=k
        self.queue=[None]*k
        self.head= self.tail= -1
    def enqueue(self, data):
        if((self.tail+1)%self.k==self.head):
            print("The circular queue is full\n")
        elif(self.head==-1):
            self.head=0
            self.tail=0
            self.queue[self.tail]=data
        else:
            self.tail=(self.tail+1)%self.k
            self.queue[self.tail]=data
    def dequeue(self):
        if(self.head==-1):
            print("The Circular queue is empty now\n")
        elif(self.head==self.tail):
            temp=self.queue[self.head]
            self.head=-1
            self.tail=-1
            return temp
        else:
            temp=self.queue[self.head]
            self.head=(self.head+1)%self.k
            return temp
    def printCqueue(self):
        if(self.head==-1):
            print("no element in the circular queue is found")
        elif(self.tail>=self.head):
            for i in range(self.head, self.tail+1):
                print(self.queue[i],end=" ")
            print()
        else:
            for i in range(self.head, sekf.k):
                print(self.queue[i], end=" ")
            for i in range(0, self.tail+1):
                print(self.queue[i], end=" ")
            print()

obj= MyCircularQueue(5)
obj.enqueue(12)
obj.enqueue(22)
obj.enqueue(31)
obj.enqueue(44)
obj.enqueue(57)
print("Initial queue values")
obj.printCqueue()
obj.dequeue()
print("After removing an element fromthe queue")
obj.printCqueue()
        
    
