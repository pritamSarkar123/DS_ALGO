class Node:
    def __init__(self,data=None,next=None,previous=None):
        self.data=data
        self.next=next
        self.previous=previous
class Queue:
    prevQFinished=True
    def __init__(self):
        if Queue.prevQFinished==False:
            self.front=None
            self.rear=None
            print("New Q can not be created")
            return
        self.front=Node()
        self.rear=Node()
        self.front.next=self.rear
        self.rear.previous=self.front
        Queue.prevQFinished=False

    def isEmpty(self):
        if self.front.next==self.rear or self.rear.previous==self.front:
            return True
        else:
            return False    

    def enqueue(self,data):
        if self.front==None and self.rear==None:
            print("front and rear is not created")
            return
        newNode=Node(data)
        newNode.previous=self.rear.previous
        newNode.next=self.rear
        (self.rear.previous).next=newNode
        self.rear.previous=newNode
    def deque(self):
        if self.front==None and self.rear==None:
            print("can not dequeue")
            return
        if self.front.next==self.rear or self.rear.previous==self.front:
            print("No element to dequeue")
            return None
        tempNode=(self.front.next).next
        dequeued=tempNode.previous
        data=dequeued.data
        tempNode.previous=self.front
        self.front.next=tempNode
        del dequeued
        if self.isEmpty()==True:
            Queue.prevQFinished==True  
        return data
    def showQueue(self):
        if self.front==None and self.rear==None:
            print("can not show")
            return
        if self.front.next==self.rear or self.rear.previous==self.front:
            print("No element to Show")
            return
        elements=[]
        currentNode=self.front
        while currentNode.next!=self.rear:
            currentNode=currentNode.next
            elements.append(currentNode.data)
        print(elements)
myQueue=Queue()
myQueue.enqueue(5)
myQueue.enqueue(10)
myQueue.enqueue(15)
myQueue.enqueue(25)
myQueue.showQueue()
print(Queue.prevQFinished)
myQueue1=Queue()
myQueue1.enqueue(5)
myQueue1.showQueue()
    
