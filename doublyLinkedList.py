class node:
    def __init__(self,data=None,next=None,previous=None):
        self.data=data
        self.next=next
        self.previous=previous
class DoublyLinkedList:
    def __init__(self):
        self.head=node()
    def appendElement(self,data):
        newNode=node(data)
        currentNode=self.head
        while currentNode.next!=None:
            currentNode=currentNode.next
        newNode.previous=currentNode
        currentNode.next=newNode
    def lengthOfList(self):
        currentNode=self.head
        length=-1
        while currentNode!=None:
            currentNode=currentNode.next
            length+=1
        return length
    def displayOfList(self):
        elements=[]
        currentNode=self.head
        while currentNode.next!=None:
            currentNode=currentNode.next
            elements.append(currentNode.data)
        print(elements)
    def getElementFromList(self,index):
        if index >= self.lengthOfList() or index <=-1:
            print("Index out of bound, unable to search !")
            return None
        currentNode=self.head
        currentNodeIndex=-1
        while True:
            if currentNodeIndex==index:
                print(currentNode.data)
                return currentNode
            currentNode=currentNode.next
            currentNodeIndex+=1
    def getElement(self,index):
        if index >= self.lengthOfList() or index <=-1:
            print("Index out of bound, unable to search !")
            return None
        currentNode=self.head
        currentNodeIndex=-1
        while True:
            if currentNodeIndex==index:
                return currentNode
            currentNode=currentNode.next
            currentNodeIndex+=1
    def eraseElementFromList(self,index):
        if index >= self.lengthOfList() or index <=-1:
            print("Index out of bound, unable to erase !")
            return
        currentNode=self.head
        currentNodeIndex=-1
        while True:
            if currentNodeIndex==index-1:
                tempnode=(currentNode.next).next
                currentNode.next=tempnode
                tempnode.previous=currentNode
                print("Element erazed!")
                return
            currentNode=currentNode.next
            currentNodeIndex+=1
    def insertElementInList(self,data,index):
        if index > self.lengthOfList() or index <=-1:
            print("Index out of bound, unable to insert")
            return
        newNode=node(data)
        currentNode=self.head
        currentNodeIndex=-1
        while True:
            if currentNodeIndex==index-1:
                tempnode=currentNode.next
                newNode.next=tempnode
                tempnode.previous=newNode
                currentNode.next=newNode
                newNode.previous=currentNode
                return
            currentNode=currentNode.next
            currentNodeIndex+=1
    def modifyElement(self,index,data):
        if index >= self.lengthOfList() or index <=-1:
            print("Index out of bound, unable to modify")
            return
        currentNode=self.head
        currentNodeIndex=-1
        while True:
            if currentNodeIndex==index:
                currentNode.data=data
                return
            currentNode=currentNode.next
            currentNodeIndex+=1
    def reverseOfList(self):
        length=self.lengthOfList()
        for i in range(0,int(length/2)):
            element1=self.getElement(i)
            element2=self.getElement(length-1-i)
            temp=element1.data
            element1.data=element2.data
            element2.data=temp
    def mergeList(self,low,mid,high):
        sortedList=[]
        m=mid
        n=high
        i,j=low,mid+1
        while i<=m and j<=n:
            element_i=self.getElement(i)
            element_j=self.getElement(j)
            if(element_i.data <= element_j.data):
                sortedList.append(element_i.data)
                i+=1
            else:
                sortedList.append(element_j.data)
                j+=1
        while(i<=m):
            element_i=self.getElement(i)
            sortedList.append(element_i.data)
            i+=1
        while(j<=n):
            element_j=self.getElement(j)
            sortedList.append(element_j.data)
            j+=1
        #placing elements in linkedlist
        i=low
        j=0
        while i<=high:
            element_i=self.getElement(i)
            element_i.data=sortedList[j]
            j+=1
            i+=1
    def mergeSort(self,lowerLimit,highetLimit):
        low=lowerLimit
        high=highetLimit
        if(low<high):
            mid=int((low+high)/2)
            self.mergeSort(low,mid)
            self.mergeSort(mid+1,high)
            self.mergeList(low,mid,high)
    def sortList(self,reverse=False):
        self.reverse=reverse
        length=self.lengthOfList()
        low=0
        high=length-1
        self.mergeSort(low,high)
        if self.reverse==True:
            self.reverseOfList()

mylist=DoublyLinkedList()
mylist.appendElement(90)
mylist.appendElement(24)
mylist.appendElement(30)
mylist.appendElement(45)
mylist.appendElement(29)
mylist.appendElement(58)
mylist.appendElement(13)
mylist.appendElement(75)
mylist.appendElement(89)
mylist.displayOfList()
mylist.lengthOfList()
mylist.getElement(25)
mylist.getElement(5)
mylist.eraseElementFromList(5)
mylist.insertElementInList(57,5)
mylist.displayOfList()
mylist.reverseOfList()
mylist.displayOfList()
mylist.sortList()
mylist.displayOfList()
mylist.sortList(True)
mylist.displayOfList()
