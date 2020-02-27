from hashTable import HashTable as HT
from GraphScanner import Scan
MAXVAL=9999

scan=Scan()
ADJ_MAT,length=scan.scanGraph("graph.txt")
nodes=HT(length+2)
charList=[]
j=0
for i in range(length):
    nodes.insertElementInTable(str(i),j)
    charList.append(str(i))
    j+=1
class GraphADJM:
    def __init__(self,ADJ_MAT,nodes):
        self.nodes=nodes
        self.ADJ_MAT=ADJ_MAT
    def ifConnected(self,node1,node2):
        element1=self.nodes.getElementFromTable(node1)
        element2=self.nodes.getElementFromTable(node2)
        el1=int(element1.value)
        el2=int(element2.value)
        if self.ADJ_MAT[el1][el2]!=MAXVAL and self.ADJ_MAT[el1][el2]!=0:
            print("The {} and {} is connected by weigth {}".format(node1,node2,self.ADJ_MAT[el1][el2]))
        if self.ADJ_MAT[el1][el2]==MAXVAL:
            print("The {} and {} is not connected ".format(node1,node2))
        if self.ADJ_MAT[el1][el2]==0:
            print("The {} and {} is same node ".format(node1,node2))

graph=GraphADJM(ADJ_MAT,nodes)
graph.ifConnected("0","5")
graph.ifConnected("0","1")
graph.ifConnected("3","6")
graph.ifConnected("2","2")
