class Graph:
    def __init__(self,vertex):
        self.mat=[]
        self.vertex=vertex
        for i in range(self.vertex):
            row=[]
            for j in range(self.vertex):
                row.append(0)
            self.mat.append(row)
    def graph(self,edge):
        for i in range(edge):
            src=int(input("Enter the src:"))
            dest=int(input("Enter the destination:"))
            #weight=int(input("Enter the weight:"))
            self.mat[src][dest]=1
            
            
    def display(self):
        for i in range(self.vertex):
            for j in range(self.vertex):
                print(self.mat[i][j],end=" ")
            print()
while(True):
    vertex=int(input("Enter the no.of vertex:"))
    obj=Graph(vertex)
    edge=int(input("Enter the no.of edges:"))
    obj.graph(edge)
    obj.display()
