class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.temp = None
        self.tail = None

    def create(self, data):
        newnode = Node(data)
        if self.head is None:
            self.head = newnode
            self.temp = newnode
            self.tail = newnode
        else:
            self.tail.next = newnode
            self.tail = newnode
            self.tail.next = self.head

    def display(self):
        self.temp = self.head
        while self.temp.next is not self.head:
            print(self.temp.data, end=" ")
            self.temp = self.temp.next
        print(self.temp.data)

    def delete_at_front(self):
        self.head = self.head.next
        self.tail.next = self.head

    def delete_at_end(self):
        self.temp = self.head
        while self.temp.next.next is not self.head:
            self.temp = self.temp.next
        self.temp.next.next = None
        self.temp.next = self.head
        self.tail = self.temp

    def delete_at_middle(self, pos):
        self.temp = self.head
        i = 1
        while i < pos - 1:
            self.temp = self.temp.next
            i += 1
        self.temp.next = self.temp.next.next
        
obj = LinkedList()
while True:
    print("1.Create\n2.Display\n3.Delete at Front\n4.Delete at End\n5.Delete at Middle\n6.Exit")
    choice = int(input("Enter choice: "))
    if choice == 1:
        data = int(input("Enter data: "))
        obj.create(data)
    elif choice == 2:
        obj.display()
    elif choice == 3:
        obj.delete_at_front()
    elif choice == 4:
        obj.delete_at_end()
    elif choice == 5:
        pos = int(input("Enter position: "))
        obj.delete_at_middle(pos)
    elif choice == 6:
        break
    else:
        print("Invalid Choice!")
