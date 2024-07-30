#Circular Queue implementation in python

class MyCircularQueue():
    def __init__(self, k):
        self.k = k 
        self.queue = [None] * k 
        self.head = self.tail = -1 
        
    #Insert an element into the circular queue 
    def enqueue(self, data):
        if((self.tail + 1) % self.k == self.head):
            print("The circualr queue is full\n") 
            
        elif(self.head == -1):
            self.head = 0 
            self.tail = 0
            self.queue[self.tail] = data 
            
        else:
            self.tail = (self.tail + 1) % self.k 
            self.queue[self.tail] = data
            
    def dequeue(self):
        if(self.head == -1):
            print("The circular queue is epty\n")
        elif(self.head == self.tail):
            temp = self.queue[self.head]
            self.head = (self.head + 1) % self.k  
            return temp 
        
    def printCQueue(self):
        if(self.head == -1):
            print("No element in the circular queue")
            
        elif(self.tail >= slef.head):
            for i in range(self.head, self.tail + 1):
                print(self.queue[i], end= " ")
            print()
        else: 
            for i in range(self.head, self.k):
                print(self.queue[i], end=" ")
            for i in range(o, self.tail + 1 ):
                print(self.queue[i], end= " ")
                
            print()
            
# Your MyCircularQueue object will be instantiated and called as such:
obj = MyCircularQueue(5)
obj.enqueue(1)
obj.enqueue(2)
obj.enqueue(3)
obj.enqueue(4)
obj.enqueue(5)
print("Initial queue")
obj.printCQueue()

obj.dequeue()
print("After removing an element from the queue")
obj.printCQueue()
            
        
        

