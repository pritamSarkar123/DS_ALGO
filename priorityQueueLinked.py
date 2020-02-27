class Node:
    def __init__(self,data=None,priority=None,next=None,previous=None):
        self.data=data
        self.priority=priority
        self.next=next
        self.previous=previous
class PQueue:
    def __init__(self):
        self.front=Node(priority=-9999999)
        self.rear=Node(priority=9999999)
        self.front.next=self.rear
        self.rear.previous=self.front
    def enqueue(self,data,priority):
        newNode=Node(data,priority)
        currentNode=self.front
        while True:
            if currentNode.priority <= newNode.priority and newNode.priority < (currentNode.next).priority:
                newNode.next=currentNode.next
                newNode.previous=currentNode
                (currentNode.next).previous=newNode
                currentNode.next=newNode
                return
            currentNode=currentNode.next
    def dequeue(self):
        if self.front.next==self.rear or self.rear.previous==self.front:
            print("No element to dequeue")
            return None
        tempNode=(self.front.next).next
        dequeued=tempNode.previous
        data=dequeued.data
        priority=dequeued.priority
        tempNode.previous=self.front
        self.front.next=tempNode
        del dequeued
        return (data,priority)
    def getFront(self):
        if self.front.next==self.rear or self.rear.previous==self.front:
            print("No element so no front")
            return None
        currentNode=self.front.next
        return (currentNode.data,currentNode.priority)
    def getRear(self):
        if self.front.next==self.rear or self.rear.previous==self.front:
            print("No element so no rear")
            return None
        currentNode=self.rear.previous
        return (currentNode.data,currentNode.priority)
    def showQueue(self):
        if self.front.next==self.rear or self.rear.previous==self.front:
            print("No element to Show")
            return
        elements={}
        currentNode=self.front
        while currentNode.next!=self.rear:
            currentNode=currentNode.next
            elements[currentNode.priority]=currentNode.data
        print(elements)
    def length(self):
        if self.front.next==self.rear or self.rear.previous==self.front:
            return 0
        currentNode=self.front
        leng=-1
        while currentNode!=self.rear:
            currentNode=currentNode.next
            leng+=1
        return leng

'''myQueue=PQueue()
myQueue.enqueue(5,1)
myQueue.enqueue(10,5)
myQueue.enqueue(99,2)
myQueue.enqueue(45,3)
myQueue.enqueue(53,7)
myQueue.showQueue()
print(myQueue.getFront())
print(myQueue.getRear())
print(myQueue.dequeue())
print(myQueue.length())
myQueue.showQueue()'''


