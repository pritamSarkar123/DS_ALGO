#scanning a graph 
from hashTable import HashTable as HT
from GraphScanner import Scan
MAXVAL=9999
scan=Scan()
ADJ_MAT,length=scan.scanGraph("graph.txt")
nodes=HT(length+2)
nodes=HT(length+2)
charList=[]
j=0
for i in range(length):
    nodes.insertElementInTable(str(i),j)
    charList.append(str(i))
    j+=1

class NodeG:
    def __init__(self,node=None,weight=None):
        self.node=node   #int
        self.weight=weight #int
        self.next=None
class LinkedListG:
    def __init__(self,nodes,nodeNames):
        self.head=NodeG(node=int((nodes.getElementFromTable(nodeNames)).value))
    def appendItem(self,node,weight):
        newNode=NodeG(node,weight)
        currentNode=self.head
        while currentNode.next!=None:
            currentNode=currentNode.next
        currentNode.next=newNode
    def getListElement(self,node):
        currentNode=self.head
        while currentNode.next!=None:
            currentNode=currentNode.next
            if currentNode.node==node:
                return currentNode
        return None
class ADJlist:
    def __init__(self,nodes,charList):
        self.list=[]
        self.nodes=nodes
        self.charList=charList
        for nodeNames in charList:
            self.list.append(LinkedListG(nodes,nodeNames))
        #print(self.list[0].head.node)
    def scanGraph(self,ADJ_MAT):
        colums=len(self.charList)
        for linkObj in self.list:
            head=linkObj.head
            connectingNode=head.node
            for connectedNode in range(colums):
                if ADJ_MAT[connectingNode][connectedNode]!=MAXVAL and ADJ_MAT[connectingNode][connectedNode]!=0:
                    linkObj.appendItem(connectedNode,ADJ_MAT[connectingNode][connectedNode])
    def ifConnected(self,node1,node2):
        el1=int((self.nodes.getElementFromTable(node1)).value)
        el2=int((self.nodes.getElementFromTable(node2)).value)
        available=self.list[el1].getListElement(el2)
        if available==None:
            print("The {} and {} is not connected ".format(node1,node2))
        else:
            if available.weight==None:
                print("The {} and {} is self looped ".format(node1,node2))
            else:
                print("The {} and {} is connected by weigth {}".format(node1,node2,available.weight))

            
graph=ADJlist(nodes,charList)
graph.scanGraph(ADJ_MAT)
graph.ifConnected("0","5")
graph.ifConnected("0","1")
graph.ifConnected("3","6")
graph.ifConnected("2","2")

