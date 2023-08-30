#linked list implementation using python
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
    
class LinkedList:
    def __init__(self):
        self.head = None
    
    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            ptr = self.head
            while ptr.next:
                ptr = ptr.next
            ptr.next = new_node
    
    def display(self):
        ptr = self.head
        while ptr:
            print(ptr.data, end=" -> ")
            ptr = ptr.next
        print("X")

def main():
    ll = LinkedList()
    while True:
        print("*****MAIN MENU*****")
        print("1. Append\t2. Display\t3. EXIT")
        print("Enter choice: ")
        choice = int(input())
        if choice==1:
            data = input("Enter data to insert: ")
            ll.append(data)
        elif choice==2:
            print("The Linked List: ")
            ll.display()
        elif choice==3:
            print("Exiting Program")
            break
        else:
            print("Invalid Option Selected")

if __name__ == "__main__":
    main()