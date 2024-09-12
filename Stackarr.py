class Stackarr:
    def __init__(self,size):
        self.size=size
        self.arr=[None]*size
        self.top=-1
    def push(self,data):
        if self.top==self.size-1:
            print("Stackoverflow!")
        else:
            self.top+=1
            self.arr[self.top]=data
    def pop(self):
        if self.top==-1:
            print("Stackunderflow!")
        else:
            self.top-=1
            return self.arr[self.top+1]
    def peek(self):
        if self.top==-1:
            print("Stackunderflow!")
        else:
            return self.arr[self.top]
    def display(self):
        if self.top == -1:
            print("Stack is Empty")
        else:
            print(self.arr[:self.top+1])
size = int(input("Enter size: "))
obj = Stackarr(size)
while True:
    print("1.Push\n2.Pop\n3.Peek\n4.Display")
    choice = int(input("Enter choice: "))
    if choice==1:
        data=int(input("Enter the data:"))
        obj.push(data)
    elif choice==2:
        obj.pop()
    elif choice==3:
        print(obj.peek())
    elif choice==4:
        obj.display()
    else:
        print("Invalid choice")
        

        
        
            
            
            
