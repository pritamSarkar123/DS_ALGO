from queueByLinkedList import Queue
class Node:
    def __init__(self,data=None):
        self.data=data
        self.leftChild=None
        self.rightChild=None
        self.height=1
    def getHeight(self):
        if self==None:
            return 0
        else:
            return self.height
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
    def getBalance(self):
        if self.leftChild and self.rightChild:
            return self.leftChild.height-self.rightChild.height
        elif self.leftChild==None and self.rightChild:
            return -self.rightChild.height
        elif self.leftChild and self.rightChild==None:
            return self.leftChild.height
        else:
            return 0
    def adjustHeight(self):
        if self.leftChild and self.rightChild:
            self.height=1+max(self.leftChild.getHeight(),self.rightChild.getHeight())
        elif self.leftChild and self.rightChild==None:
            self.height=1+self.leftChild.getHeight()
        elif self.leftChild==None and self.rightChild:
            self.height=1+self.rightChild.getHeight()
        else:
            self.height=1
    def rotateLeft(self,root):
        temp=root.rightChild
        root.rightChild=temp.leftChild
        temp.leftChild=root
        root.adjustHeight()
        temp.adjustHeight()
        return temp        
    def rotateRight(self,root):
        temp=root.leftChild
        root.leftChild=temp.rightChild
        temp.rightChild=root
        root.adjustHeight()
        temp.adjustHeight()
        return temp
    def preorder(self): #no need for elses, automatically returns
        if self:
            print(self.data,self.height)
            if self.leftChild:
                self.leftChild.preorder()
            if self.rightChild:
                self.rightChild.preorder()
    def inorder(self): #no need for elses, automatically returns
        if self:
            if self.leftChild:
                self.leftChild.inorder()
            print(self.data,self.height)
            if self.rightChild:
                self.rightChild.inorder()
    def insert(self,data):
        if self.data==data:
            return self
        if self.data>data:
            if self.leftChild:
                self.leftChild=self.leftChild.insert(data)
            else:
                self.leftChild=Node(data)
        if self.data<data:
            if self.rightChild:
                self.rightChild= self.rightChild.insert(data)
            else:
                self.rightChild=Node(data)
        self.adjustHeight()      
        balance=self.getBalance()
        if balance > 1 and self.leftChild.data > data:
            self=self.rotateRight(self)
        if balance < -1 and self.rightChild.data < data:
            self=self.rotateLeft(self)
        if balance > 1 and self.leftChild.data < data:
            self.leftChild=self.leftChild.rotateLeft(self.leftChild)
            self=self.rotateRight(self)
        if balance < -1 and self.rightChild.data > data:
            self.rightChild=self.rightChild.rotateRight(self.rightChild)
            self=self.rotateLeft(self)
        return self
    def adjustTree(self):
        if self.leftChild and self.rightChild:
            self.leftChild=self.leftChild.adjustTree()
            self.rightChild=self.rightChild.adjustTree()
        elif self.leftChild==None and self.rightChild:
            self.rightChild=self.rightChild.adjustTree()
        elif self.leftChild and self.rightChild==None:
            self.leftChild=self.leftChild.adjustTree()
        else:
            self.height=1
            return self
        self.adjustHeight()      
        balance=self.getBalance()
        if balance > 1 and self.leftChild.leftchild!=None:
            self=self.rotateRight(self)
        if balance < -1 and self.rightChild.rightChild!=None:
            self=self.rotateLeft(self)
        if balance > 1 and self.leftChild.rightChild!=None:
            self.leftChild=self.leftChild.rotateLeft(self.leftChild)
            self=self.rotateRight(self)
        if balance < -1 and self.rightChild.leftChild!=None:
            self.rightChild=self.rightChild.rotateRight(self.rightChild)
            self=self.rotateLeft(self)
        return self
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
class AVL:
    def __init__(self):
        self.root=None
    def insert(self,data):
        if self.root==None:
            self.root=Node(data)
        else:
            self.root=self.root.insert(data)
        print("{} inserted".format(data))
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
            return 
        #case 2
        elif self.root.search(data)==False:
            return 
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
        self.root=self.root.adjustTree()
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

myBst=AVL()
myBst.insert(30)
myBst.insert(20)
myBst.insert(80)
myBst.insert(10)
myBst.insert(25)
myBst.insert(78)
myBst.insert(92)
myBst.insert(5)
myBst.insert(94)
myBst.insert(93)
myBst.insert(2)
myBst.preorder()
myBst.inorder()
myBst.delete(94)
myBst.delete(30)
myBst.preorder()
myBst.inorder()
