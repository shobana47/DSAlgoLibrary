class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
        self.temp = None

    def create(self, data):
        newnode = Node(data)
        if self.head is None:
            self.head = newnode
            self.temp = newnode
        else:
            self.temp.next = newnode
            self.temp = self.temp.next

    def display(self):
        self.temp = self.head
        while self.temp is not None:
            print(self.temp.data, end=" ")
            self.temp = self.temp.next
        print()

    def delete_at_front(self):
        self.head = self.head.next

    def delete_at_mid(self, pos):
        i = 1
        self.temp = self.head
        while i < pos - 1:
            self.temp = self.temp.next
            i += 1
        self.temp.next = self.temp.next.next

    def delete_at_end(self):
        self.temp = self.head
        while self.temp.next.next is not None:
            self.temp = self.temp.next
        self.temp.next = None


obj = LinkedList()
while True:
    print("1.Create\n2.Display\n3.Delete at front\n4.Delete at end\n"
          "5.Delete at Mid\n6.Exit\n")

    choice = int(input("Enter a choice: "))
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
        obj.delete_at_mid(pos)
    else:
        print("Invalid Choice! Enter Again!")

