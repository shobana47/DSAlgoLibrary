class Stack:
    def _init_(self,size):
        self.Stack = []
        self.max_size=size
        
    def push(self, item):
        if len(self.Stack) < self.max_size:
            self.Stack.append(item)  
            print(f"Pushed {item} to stack.")
        else:
            print("Stack overflow. Cannot push more items.")

    def pop(self):
        if not self.is_empty():
            popped_item = self.Stack.pop()  
            print(f"Popped {popped_item} from stack.")
            return popped_item
        else:
            print("Stack Underflow. Cannot pop.")
            return None

    def is_empty(self):
        return len(self.Stack) == 0 

    def peek(self):
        if not self.is_empty():
            print(self.Stack[-1])  
        else:
            print("Stack is empty.")
            return None  

    def display(self):
        print("Current stack:",self.Stack)
          
size=int(input("enter size of the stack in list:"))
obj = Stack(size)
print("1.push 2.pop 3.peek 4.display 5.exit")
while 1:
    choice=int(input("Enter a choice :"))

    if choice==1:
        item=int(input("Enter a data :"))
        obj.push(item)

    elif choice==2:
        obj.pop()

    elif choice==3:
        obj.peek()

    elif choice==4:
        obj.display()

    elif choice==5:
        break

    else:
        print("Invalid choice.Please try again")
