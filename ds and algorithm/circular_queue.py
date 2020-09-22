class CircularQueue():
    def __init__(self, size):
        self.size =size
        self.queue= [None] * size
        self.head=head = -1
        self.tail=tail = -1

    def Enqueue(self, item):
        if ((self.tail +1) % self.size == self.head):
            print("The Circular Queue if full")
        
        elif self.head == -1:
            self.head = 0
            self.tail = 0
            self.queue[self.head] = item
        else:
            self.tail=(self.tail +1)% self.size
            self.queue[self.tail]=item

    def Dequeue(self):
        if self.head == -1:
            print("Circular Queue is Empty")

        elif (self.head == self.tail):
            temp = self.queue[self.head]
            self.head = -1
            self.tail = -1
            return temp
        else:
            temp = self.queue[self.head]
            self.head = (self.head + 1) % self.size
            return temp
        
    def PrintQueue(self):
        if self.head == -1:
            print("Circular Queue is Empty")
        
        elif (self.tail > self.head):
            for i in range(self.head, self.tail+1):
                print(self.queue[i],end=" ")
            print()
        
        else :
            for i in range(self.head, self.size):
                print(self.queue[i],end=" ")
            print()
            for i in range(0 ,self.tail):
                print(self.queue[i],end=" ")

Cqueue =CircularQueue(4)
Cqueue.Enqueue(1)
Cqueue.Enqueue(2)
Cqueue.Enqueue(3)
Cqueue.Enqueue(4)
Cqueue.Enqueue(5)

Cqueue.PrintQueue()
Cqueue.Dequeue()
Cqueue.Dequeue()
Cqueue.PrintQueue()