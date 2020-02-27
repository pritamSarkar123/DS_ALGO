class node:
    def __init__(self,data=None):
        self.data=data
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=node()
    def appendItem(self,data):
        newNode=node(data)
        currentNode=self.head
        while currentNode.next!=None:
            currentNode=currentNode.next
        currentNode.next=newNode
    def lengthOfList(self):
        currentNode=self.head
        length=-1 #not considering the 1st head element
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
    def getListElement(self,index):
        if index >= self.lengthOfList() or index==-1:
            print('index out of bound unable to get element!')
            return None
        currentNode=self.head
        #not considering the 1st head element
        currentNodeIndex=-1
        while True:
            if currentNodeIndex==index:
                print(currentNode.data)
                return currentNode
            currentNode=currentNode.next
            currentNodeIndex+=1
    def eraseListItem(self,index):
        if index >= self.lengthOfList() or index==-1:
            print('index out of bound unable to erase element!')
            return
        currentNode=self.head
        #not considering the 1st head element
        currentNodeIndex=-1
        while True:
            if currentNodeIndex==index-1:
                tempNode=(currentNode.next).next
                currentNode.next=tempNode
                return
            currentNode=currentNode.next
            currentNodeIndex+=1
    def insertIntoList(self,data,index):
        if index > self.lengthOfList() or index==-1:
            print('index out of bound unable to insert element!')
            return
        newNode=node(data)
        currentNode=self.head
        #not considering the 1st head element
        currentNodeIndex=-1
        if index==self.lengthOfList():
            self.appendItem(data)
            return
        while True:
            if currentNodeIndex==index-1:
                tempNode=currentNode.next
                currentNode.next=newNode
                newNode.next=tempNode
                return
            currentNode=currentNode.next
            currentNodeIndex+=1
    def modifyElement(self,data,index):
        if index >= self.lengthOfList() or index==-1:
            print('index out of bound unable to modify element!')
            return
        currentNode=self.head
        #not considering the 1st head element
        currentNodeIndex=-1
        while True:
            if currentNodeIndex==index:
                currentNode.data=data
                return
            currentNode=currentNode.next
            currentNodeIndex+=1
    def getElement(self,index):
        if index >= self.lengthOfList() or index==-1:
            print('index out of bound unable to get element!')
            return None
        currentNode=self.head
        #not considering the 1st head element
        currentNodeIndex=-1
        while True:
            if currentNodeIndex==index:
                return currentNode
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







'''myList=LinkedList()
myList.appendItem(5)
myList.appendItem(10)
myList.appendItem(15)
myList.appendItem(20)
myList.appendItem(25)
myList.appendItem(28)
print(myList.lengthOfList())
myList.displayOfList()
myList.getListElement(10)
myList.getListElement(0)
myList.getListElement(2)
myList.eraseListItem(10)
myList.displayOfList()
myList.eraseListItem(0)
myList.displayOfList()
myList.eraseListItem(2)
myList.displayOfList()
myList.eraseListItem(3)
myList.displayOfList()
myList.insertIntoList(5,0)
myList.displayOfList()
myList.insertIntoList(4,100)
myList.displayOfList()
myList.insertIntoList(18,3)
myList.insertIntoList(32,3)
myList.insertIntoList(8,3)
myList.insertIntoList(9,3)
myList.displayOfList()
myList.insertIntoList(15,4)
myList.displayOfList()
myList.modifyElement(34,4)
myList.displayOfList()
myList.reverseOfList()
myList.displayOfList()
myList.sortList()
myList.displayOfList()
myList.sortList(True)
myList.displayOfList()'''

    




        
