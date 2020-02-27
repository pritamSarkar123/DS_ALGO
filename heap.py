class Heap:
    def __init__(self,minHeap=False,maxHeap=True): #by default max heap
        self.list=[]
        self.minHeap=minHeap
        self.maxHeap=maxHeap
        if self.minHeap:
            self.maxHeap=False
    def isExhist(self,value): #to avoid duplicacy
        for i in self.list:
            if value==i:
                return True
        return False
    def isLeaf(self,length,index): #whether a node is a leaf node or not
        if 2*index+1>length-1:
            return True
        else:
            return False
    def maxIndex(self,length,index): #returns maximum index among 2 children
        if 2*index+2>length-1:
            return 2*index+1
        else:
            if self.list[2*index+1]>self.list[2*index+2]:
                return 2*index+1
            else:
                return 2*index+2
    def minIndex(self,length,index): #returns minimum index among 2 children
        if 2*index+2>length-1:
            return 2*index+1
        else:
            if self.list[2*index+1]<self.list[2*index+2]:
                return 2*index+1
            else:
                return 2*index+2
    def heapify(self,*args):
        for i in args:
            if not self.isExhist(i):
                self.list.append(i)
        length=len(self.list)
        if self.maxHeap:
            i=length-1
            while i>=0: #bottom to top
                if not self.isLeaf(length,i):
                    maxIndex=self.maxIndex(length,i)
                    if self.list[i]<self.list[maxIndex]:
                        self.list[i],self.list[maxIndex]=self.list[maxIndex],self.list[i]
                i-=1
            i=0
            while i<=length-1: #top to bottom
                if not self.isLeaf(length,i):
                    maxIndex=self.maxIndex(length,i)
                    if self.list[i]<self.list[maxIndex]:
                        self.list[i],self.list[maxIndex]=self.list[maxIndex],self.list[i]
                i+=1
        else:
            i=length-1
            while i>=0: #bottom to top
                if not self.isLeaf(length,i):
                    minIndex=self.minIndex(length,i)
                    if self.list[i]>self.list[minIndex]:
                        self.list[i],self.list[minIndex]=self.list[minIndex],self.list[i]
                i-=1
            i=0
            while i<=length-1: #top to bottom
                if not self.isLeaf(length,i):
                    minIndex=self.minIndex(length,i)
                    if self.list[i]>self.list[minIndex]:
                        self.list[i],self.list[minIndex]=self.list[minIndex],self.list[i]
                i+=1
    def heapInsert(self,*args):
        if self.maxHeap:
            for i in args:
                if not self.isExhist(i):
                    self.list.append(i)
                    j=len(self.list)
                    if j>1: #when list have more than one elements after apendingg
                        j=j-1
                        while j>0:
                            index=int((j-1)/2)
                            if self.list[index]<self.list[j]:
                                self.list[index],self.list[j]=self.list[j],self.list[index]
                            j=index
        else:
            for i in args:
                if not self.isExhist(i):
                    self.list.append(i)
                    j=len(self.list)
                    if j>1: #when list have more than one elements after appending
                        j=j-1
                        while j>0:
                            index=int((j-1)/2)
                            if self.list[index]>self.list[j]:
                                self.list[index],self.list[j]=self.list[j],self.list[index]
                            j=index
    def heapDelete(self):
        length=len(self.list)
        if length>0:
            data=self.list[0]
            self.list[0],self.list[-1]=self.list[-1],self.list[0]
            self.list=self.list[:-1]
            length=len(self.list)
            if self.maxHeap:
                i=0
                while not self.isLeaf(length,i):
                    maxIndex=self.maxIndex(length,i)
                    if self.list[i]<self.list[maxIndex]:
                        self.list[i],self.list[maxIndex]=self.list[maxIndex],self.list[i]
                    i=maxIndex
            else:
                i=0
                while not self.isLeaf(length,i):
                    minIndex=self.minIndex(length,i)
                    if self.list[i]>self.list[minIndex]:
                        self.list[i],self.list[minIndex]=self.list[minIndex],self.list[i]
                    i=minIndex
            return data
        else:
            print("nothing to delete")
            return None
    def heapDeleteForSorting(self):
        sortedList=[]
        while len(self.list)>0:
            sortedList.append(self.heapDelete())
        self.list=sortedList[:]
    def heapSort(self):
        if len(self.list)==0:
            print("no element to sort")
            return
        print("before sorting",end=" ")
        print(self.list)
        self.heapDeleteForSorting()
        print("after sorting",end=" ")
        print(self.list)
    def showHeap(self):
        print(self.list)

'''myheap=Heap(minHeap=False)
myheap.heapify(50,30,20,10,15,8,57)
myheap.heapInsert(16,20,18)
myheap.showHeap()
print(myheap.heapDelete())
myheap.showHeap()
print(myheap.heapDelete())
myheap.showHeap()
print(myheap.heapDelete())
myheap.showHeap()
myheap.heapSort()
myheap=Heap(minHeap=True)
myheap.heapify(50,30,20,10,15,8,57)
myheap.heapInsert(16,20,18)
myheap.heapSort()'''





        






        
        
        