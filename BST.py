from queueByLinkedList import Queue
class Node:
    def __init__(self,data=None,leftChild=None,rightChild=None):
        self.data=data
        self.leftChild=leftChild
        self.rightChild=rightChild
    def insert(self,data):
        if self.data==data:
            return False
        elif self.data > data:
            if self.leftChild:
                return self.leftChild.insert(data)
            else:
                self.leftChild=Node(data)
                return True
        else:
            if self.rightChild:
                return self.rightChild.insert(data)
            else:
                self.rightChild=Node(data)
                return True
    def search(self,data):
        if self.data==data:
            return True
        elif self.data>data:
            if self.leftChild:
                return self.leftChild.search(data)
            else:
                return False
        else:
            if self.rightChild:
                return self.rightChild.search(data)
            else:
                return False
    def preorder(self): #no need for elses, automatically returns
        if self:
            print(self.data)
            if self.leftChild:
                self.leftChild.preorder()
            if self.rightChild:
                self.rightChild.preorder() 
    def inorder(self): #no need for elses, automatically returns
        if self:
            if self.leftChild:
                self.leftChild.inorder()
            print(self.data)
            if self.rightChild:
                self.rightChild.inorder()
    def postorder(self): #no need for elses, automatically returns
        if self:
            if self.leftChild:
                self.leftChild.postorder()
            if self.rightChild:
                self.rightChild.postorder()
            print(self.data)
    def findMin(self):
        if self:
            if self.leftChild:
                return self.leftChild.findMin()
            else:
                return self.data
    def findMax(self):
        if self:
            if self.rightChild:
                return self.rightChild.findMax()
            else:
                return self.data
    def findNode(self,data):
        if self.data==data:
            return self
        elif self.data>data:
            if self.leftChild:
                return self.leftChild.findNode(data)
            else:
                return None
        else:
            if self.rightChild:
                return self.rightChild.findNode(data)
            else:
                return None
    def inorderSuccssor(self,data):
        currentNode=self.findNode(data)
        if currentNode.rightChild!=None:
            return self.rightChild.findMin()
        else:
            succssor=None
            ansestor=self
            while ansestor.data!=currentNode.data:
                if ansestor.data>currentNode.data:
                    succssor=ansestor
                    ansestor=ansestor.leftChild
                else:
                    ansestor=ansestor.rightChild
            return succssor.data
    def BFS(self):
        queue=Queue()
        queue.enqueue(self)
        while queue.isEmpty()!=True:
            front=queue.getFront()
            if front.leftChild:
                queue.enqueue(front.leftChild)
            if front.rightChild:
                queue.enqueue(front.rightChild)
            data=(queue.deque()).data
            print(data)
    def getHeight(self):
        if self.leftChild and self.rightChild:
            return 1 + max(self.leftChild.getHeight(),self.rightChild.getHeight())
        elif self.leftChild and self.rightChild==None:
            return 1 + self.leftChild.getHeight()
        elif self.leftChild==None and self.rightChild:
            return 1 + self.rightChild.getHeight()
        else:
            return 1
    def getSize(self):
        if self.leftChild and self.rightChild:
            return 1+self.leftChild.getSize()+self.rightChild.getSize()
        elif self.leftChild and self.rightChild==None:
            return 1+self.leftChild.getSize()
        elif self.leftChild==None and self.rightChild:
            return 1+self.rightChild.getSize()
        else:
            return 1
    def isEqual(self,root):
        if self.leftChild and self.rightChild:
            if root.leftChild==None and root.rightChild==None:
                return False
            elif root.leftChild==None and root.rightChild:
                return False
            elif root.leftChild and root.rightChild==None:
                return False
            else:
                if self.data!=root.data:
                    return False
                leftBool=self.leftChild.isEqual(root.leftChild)
                rightBool=self.rightChild.isEqual(root.rightChild)
                if leftBool==True and rightBool==True:
                    return True
                else:
                    return False
                #####
        elif self.leftChild and self.rightChild==None:
            if root.leftChild==None and root.rightChild==None:
                return False
            elif root.leftChild==None and root.rightChild:
                return False
            elif root.leftChild and root.rightChild:
                return False
            else: ####
                if self.data!=root.data:
                    return False
                leftBool=self.leftChild.isEqual(root.leftChild)
                if leftBool==True:
                    return True
                else:
                    return False
        elif self.leftChild==None and self.rightChild:
            if root.leftChild==None and root.rightChild==None:
                return False
            elif root.leftChild and root.rightChild==None:
                return False
            elif root.leftChild and root.rightChild:
                return False
            else:#######
                if self.data!=root.data:
                    return False
                rightBool=self.rightChild.isEqual(root.rightChild)
                if rightBool==True:
                    return True
                else:
                    return False
        else:
            if root.leftChild and root.rightChild:
                return False
            elif root.leftChild==None and root.rightChild:
                return False
            elif root.leftChild and root.rightChild==None:
                return False
            else:######
                if self.data!=root.data:
                    return False
                else:
                    return True


    
class BST:
    def __init__(self):
        self.root=None
    def insert(self,data):
        if self.root:
            return self.root.insert(data)
        else:
            self.root=Node(data)
            return True
    def search(self,data):
        if self.root:
            return self.root.search(data)
        else:
            return False
    def preorder(self):
        if self.root==None:
            return
        print("Pre order :")
        self.root.preorder()
    def inorder(self):
        if self.root==None:
            return
        print("In order :")
        self.root.inorder()
    def postorder(self):
        if self.root==None:
            return
        print("Post order :")
        self.root.postorder()
    def findMin(self):
        if self.root==None:
            return None
        return self.root.findMin()
    def findMax(self):
        if self.root==None:
            return None
        return self.root.findMax()
    def inorderSuccssor(self,data):
        if self.root==None:
            return None
        if self.root.search(data)==False:
            return None
        return self.root.inorderSuccssor(data)
    def BFS(self):
        if self.root==None:
            return
        self.root.BFS()
    def delete(self,data):
        #case1 tree is empty
        #case2 value not present in tree
        #case3 value in root node
        #case4 node has left child only
        #case5 node has right child only
        #case6 node has both left and right child
        #case7 node has no child at all
        
        #case1
        if self.root==None:
            return False
        #case 2
        elif self.root.search(data)==False:
            return False
        #case 3
        elif self.root.data==data:
            if self.root.leftChild==None and self.root.rightChild==None: #only one node no child
                self.root=None
            if self.root.leftChild and self.root.rightChild==None:       #have left child
                self.root=self.root.leftChild
            if self.root.leftChild==None and self.root.rightChild:       #have right child
                self.root=self.root.rightChild
            if self.root.leftChild and self.root.rightChild:             #have both child
                delNodeParent=self.root
                delNode=self.root.rightChild
                while delNode.leftChild:
                    delNodeParent=delNode
                    delNode=delNode.leftChild
                self.root.data=delNode.data
                if delNode.rightChild:                         #del node has right child only
                    if delNode.data<delNodeParent.data:
                        delNodeParent.leftChild=delNode.rightChild
                    else:
                        delNodeParent.rightChild=delNode.rightChild
                else:                                          #delnode has no child
                    if delNode.data<delNodeParent.data:
                        delNodeParent.leftChild=None
                    else:
                        delNodeParent.rightChild=None
            return True
        #case 4,5,6,7
        else:
            #finding the node first which contains the data
            parent=None
            node=self.root
            while node and node.data!=data:
                parent=node
                if data<node.data:
                    node=node.leftChild
                else:
                    node=node.rightChild
            #case 4
            if node.leftChild and node.rightChild==None:
                if node.data<parent.data:             #node is left child of parent
                    parent.leftChild=node.leftChild
                else:                                 #node is rigth cild of parent
                    parent.rightChild=node.leftChild
            #case 5
            if node.leftChild==None and node.rightChild:
                if node.data<parent.data:             #node is left child of parent
                    parent.leftChild=node.rightChild
                else:                                 #node is rigth cild of parent
                    parent.rightChild=node.rightChild
            #case 6
            if node.leftChild and node.rightChild:
                delNodeParent=node
                delNode=node.rightChild
                while delNode.leftChild:
                    delNodeParent=delNode
                    delNode=delNode.leftChild
                node.data=delNode.data
                if delNode.rightChild:                #del node has right child only
                    if delNode.data<delNodeParent.data:
                        delNodeParent.leftChild=delNode.rightChild
                    else:
                        delNodeParent.rightChild=delNode.rightChild
                else:                                  #delnode has no child
                    if delNode.data<delNodeParent.data:
                        delNodeParent.leftChild=None
                    else:
                        delNodeParent.rightChild=None
            #case 7
            if node.leftChild==None and node.rightChild==None:
                if node.data<parent.data:             #node is left child of parent
                    parent.leftChild=None
                else:                                 #node is rigth cild of parent
                    parent.rightChild=None
            return True
    def getHeight(self):
        if self.root:
            return self.root.getHeight()
        else:
            return 0
    def getSize(self):
        if self.root:
            return self.root.getSize()
        else:
            return 0
    def isEqual(self,obj):
        if self.root==None and obj.root==None:
            return True
        if self.root.getHeight()!=obj.root.getHeight():
            return False
        if self.root.getSize()!=obj.root.getSize():
            return False
        return self.root.isEqual(obj.root)

'''myBst=BST()
myBst.insert(30)
myBst.insert(20)
myBst.insert(80)
myBst.insert(10)
myBst.insert(25)
myBst.insert(78)
myBst.insert(92)
myBst.insert(5)'''
'''print(myBst.search(90))
print(myBst.search(92))
myBst.preorder()
myBst.inorder()
myBst.postorder()
print(myBst.findMin())
print(myBst.findMax())
print(myBst.inorderSuccssor(30))
myBst.BFS()'''
#myBst.delete(30)
#myBst.delete(80)
#myBst.delete(92) ##!!!!!!!!!!!!!!!!!!!!!!!
#myBst.inorder()
#print(myBst.getHeight())
#print(myBst.getSize())
#myBst1=BST()
'''myBst1.insert(30)
myBst1.insert(20)
myBst1.insert(80)
myBst1.insert(10)
myBst1.insert(25)
myBst1.insert(78)
#myBst1.insert(92)
myBst1.insert(5)
print(myBst.isEqual(myBst1))'''
