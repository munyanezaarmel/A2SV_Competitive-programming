class MyCircularDeque:

    def __init__(self, k):
        self.size=k
        self.q=[0]*self.size
        self.front=-1
        self.rear=-1

    def insertFront(self, value):
        if self.isFull():
            return False
        if self.isEmpty():
            self.front=self.rear=0
        else:
            self.front=(self.front-1)%self.size 
        self.q[self.front]=value
        return True

    def insertLast(self, value):
        if self.isFull():
            return False
        if self.isEmpty():
            self.front=self.rear=0
        else:
            self.rear=(self.rear+1)%self.size 
        self.q[self.rear]=value
        return True

    def deleteFront(self):
        if self.isEmpty():
            return False
        item=self.q[self.front]
        if self.front==self.rear:
            self.front=self.rear=-1
        else:
            self.front=(self.front+1)%self.size 
        return True

    def deleteLast(self) :
        if self.isEmpty():
            return False
        item=self.q[self.rear]
        if self.front==self.rear: 
            self.front=self.rear=-1
        else:
            self.rear=(self.rear-1)%self.size 
        return True

    def getFront(self) :
        if self.front==-1:
            return -1
        return self.q[self.front]

    def getRear(self) :
        if self.rear==-1:
            return -1
        return self.q[self.rear]

    def isEmpty(self) :
        return self.front==self.rear==-1

    def isFull(self) :
        if (self.rear + 1) % self.size == self.front:
            return True
        return False