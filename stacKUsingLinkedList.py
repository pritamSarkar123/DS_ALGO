class Node:
    def __init__(self,data=None,next=None):
        self.data=data
        self.next=None
class Stack:
    def __init__(self):
        self.head=Node()
    def push(self,data):
        currentNode=self.head
        newNode=Node(data)
        newNode.next=currentNode.next
        currentNode.next=newNode
    def length(self):
        currentNode=self.head
        length=-1
        while currentNode!=None:
            currentNode=currentNode.next
            length+=1
        return length
    def isEmpty(self):
        if self.length()==0:
            return True
        else:
            return False
    def pop(self):
        if self.isEmpty()==True:
            print("Empty!, can not pop")
            return None
        currentNode=self.head
        currentNode=currentNode.next
        data=currentNode.data
        self.head.next=currentNode.next
        del currentNode
        return data
    def peek(self):
        if self.isEmpty()==True:
            print("Empty!, can not peek")
            return None
        currentNode=self.head.next
        data=currentNode.data
        return data
    def showStack(self):
        elements=[]
        currentNode=self.head
        while currentNode.next!=None:
            currentNode=currentNode.next
            elements.append(currentNode.data)
        print(elements)

'''myStack=Stack()
myStack.push(5)
myStack.push(10)
myStack.push(15)
myStack.push(20)
print(myStack.peek())
myStack.showStack()
print(myStack.pop())
myStack.showStack()'''



    
    
    