class node:
    def __init__(self,data):
        self.data=data
        self.next=None
class stack:
    def __init__(self):
        self.top=None
    def push(self,data):
        newnode=node(data)
        newnode.next=self.top
        self.top=newnode
    def pop(self):
        if self.top==None:
            print("Stackunderflow!")
        else:
            self.top=self.top.next
    def peek(self):
        if self.top==None:
            print("Stack is empty")
            return None
        else:
            print(self.top.data)
    def display(self):
        temp=self.top
        while temp:
            print(temp.data,end="->")
            temp=temp.next
obj=stack()
while True:
    print("1.Push\n2.Pop\n3.Peek\n4.Display")
    choice=int(input("Enter your choice:"))
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
