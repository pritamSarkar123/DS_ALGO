class Scan:
    def __init__(self):
        self.MAXVAL=9999
        self.ADJ_MAT=[]
    def scanGraph(self,path):
        f=open(path,"r")
        text=f.read()
        text=text.splitlines()
        for line in text:
            words=line.split(",")
            lis=[]
            for word in words:
                if word=="MAXVAL":
                    lis.append(self.MAXVAL)
                else:
                    lis.append(int(word))
            self.ADJ_MAT.append(lis)
        f.close()
        return self.ADJ_MAT,len(text)
