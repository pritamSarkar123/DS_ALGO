class Node:
    def __init__(self,data=None,next=None,previous=None):
        self.data=data
        self.next=next
        self.previous=previous
class Queue:
    def __init__(self):
        self.front=Node()
        self.rear=Node()
        self.front.next=self.rear
        self.rear.previous=self.front
    def enqueue(self,data):
        newNode=Node(data)
        newNode.previous=self.rear.previous
        newNode.next=self.rear
        (self.rear.previous).next=newNode
        self.rear.previous=newNode
    def deque(self):
        if self.front.next==self.rear or self.rear.previous==self.front:
            print("No element to dequeue")
            return None
        tempNode=(self.front.next).next
        dequeued=tempNode.previous
        data=dequeued.data
        tempNode.previous=self.front
        self.front.next=tempNode
        del dequeued
        return data
    def getFront(self):
        if self.front.next==self.rear or self.rear.previous==self.front:
            print("No element so no front")
            return None
        currentNode=self.front.next
        return currentNode.data
    def getRear(self):
        if self.front.next==self.rear or self.rear.previous==self.front:
            print("No element so no rear")
            return None
        currentNode=self.rear.previous
        return currentNode.data
    def showQueue(self):
        if self.front.next==self.rear or self.rear.previous==self.front:
            print("No element to Show")
            return
        elements=[]
        currentNode=self.front
        while currentNode.next!=self.rear:
            currentNode=currentNode.next
            elements.append(currentNode.data)
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
    def isEmpty(self):
        if self.front.next==self.rear or self.rear.previous==self.front:
            return True
        else:
            return False

'''myQueue=Queue()
myQueue.enqueue(5)
myQueue.enqueue(10)
myQueue.enqueue(15)
myQueue.enqueue(25)
myQueue.showQueue()
print(myQueue.length())
print(myQueue.getFront())
print(myQueue.getRear())
print(myQueue.deque())
myQueue.showQueue()'''

        




        




