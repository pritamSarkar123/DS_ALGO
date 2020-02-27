class node:
    def __init__(self,key=None,value=None):
        self.key=key
        self.value=value
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=node()
    def appendItem(self,key,value):
        newNode=node(key,value)
        currentNode=self.head
        while currentNode.next!=None:
            currentNode=currentNode.next
        currentNode.next=newNode
    def distinctKey(self,key):
        currentNode=self.head
        while currentNode!=None:
            if currentNode.key==key:
                return False
            currentNode=currentNode.next
        return True
    def modifyItem(self,key,value):
        currentNode=self.head
        while currentNode!=None:
            if currentNode.key==key:
                currentNode.value=value
                return
            currentNode=currentNode.next
        print("nothing to modify!")
    def getListElement(self,key):
        currentNode=self.head
        while currentNode!=None:
            if currentNode.key==key:
                return currentNode
            currentNode=currentNode.next
        print("element not found !")
        return None
    def deleteFromList(self,key):
        currentNode=self.head
        while currentNode.next!=None:
            if (currentNode.next).key==key:
                tempNode=(currentNode.next).next
                currentNode.next=tempNode
                print("deletion successful")
                return 
            currentNode=currentNode.next
        print("element not found for deletion!")
class HashTable:
    lists=[]
    def __init__(self,noOfLists=1):
        self.noOfLists=noOfLists
        for i in range(noOfLists):
            self.lists.append(LinkedList())
    def hash1(self,key):
        return key % 35
    def hash2(self,key):
        return 7-(key % 7)
    def map(self,keyString):
        i=0
        key=0
        #ascii sum
        while i<len(keyString):
            key+=ord(keyString[i])
            i+=1
        for i in range(int(self.noOfLists/2)):
            position=(self.hash1(key)*self.hash1(key) + i * self.hash2(key)) % self.noOfLists
        return position
    def insertElementInTable(self,key,value):
        if len(self.lists)==0:
            print("Hash Table Not exhist")
            return
        position=self.map(key)
        if self.lists[position].distinctKey(key)==None:
            return
        if self.lists[position].distinctKey(key):
            self.lists[position].appendItem(key,value)
        else:
            self.lists[position].modifyItem(key,value)
        print("insertion successful")
    def modifyElementInTable(self,key,value):
        if len(self.lists)==0:
            print("Hash Table Not exhist")
            return
        position=self.map(key)
        self.lists[position].modifyItem(key,value)
    def getElementFromTable(self,key):
        if len(self.lists)==0:
            #print("Hash Table Not exhist")
            return None
        position=self.map(key)
        element=self.lists[position].getListElement(key)
        if element!=None:
            #print("slot["+str(position)+"] : key : "+key+" value : "+element.value)
            return element
    def deleteElementFromTable(self,key):
        if len(self.lists)==0:
            print("Hash Table Not exhist")
            return
        position=self.map(key)
        self.lists[position].deleteFromList(key)
    def dropTable(self):
        if len(self.lists)==0:
            print("Hash Table Not exhist")
            return
        del self.lists[:]
        print("Tablle Dropped -_-")


'''myHashTable=HashTable(5)
myHashTable.insertElementInTable("pritam","vanu")
myHashTable.insertElementInTable("eshani","golla")
myHashTable.insertElementInTable("pujki","maa")
myHashTable.insertElementInTable("rahul","badam")
myHashTable.insertElementInTable("vusha1","debu")
myHashTable.insertElementInTable("jyptirmay","jaguli")
myHashTable.getElementFromTable("pritam")
myHashTable.getElementFromTable("eshani")
myHashTable.getElementFromTable("pujki")
myHashTable.getElementFromTable("nakbuchi")
myHashTable.getElementFromTable("jyptirmay")
myHashTable.getElementFromTable("rahul")
myHashTable.deleteElementFromTable("bulbul")
myHashTable.deleteElementFromTable("rahul")
myHashTable.insertElementInTable("pujki","Chotomaa")
myHashTable.getElementFromTable("pujki")  
myHashTable.dropTable()  
myHashTable.getElementFromTable("pujki") 
myHashTable.getElementFromTable("jyptirmay")
myHashTable.insertElementInTable("pujki","Chotomaa")
myHashTable.getElementFromTable("pujki")


myHashTable=HashTable(5)
myHashTable.insertElementInTable("pritam","vanu")
myHashTable.insertElementInTable("eshani","golla")
myHashTable.insertElementInTable("pujki","maa")
myHashTable.insertElementInTable("rahul","badam")
myHashTable.insertElementInTable("vusha1","debu")
myHashTable.insertElementInTable("jyptirmay","jaguli")
myHashTable.getElementFromTable("pritam")
myHashTable.getElementFromTable("eshani")
myHashTable.getElementFromTable("pujki")
myHashTable.getElementFromTable("nakbuchi")
myHashTable.getElementFromTable("jyptirmay")
myHashTable.getElementFromTable("rahul")
myHashTable.deleteElementFromTable("bulbul")
myHashTable.deleteElementFromTable("rahul")
myHashTable.insertElementInTable("pujki","Chotomaa")
myHashTable.getElementFromTable("pujki")  '''
