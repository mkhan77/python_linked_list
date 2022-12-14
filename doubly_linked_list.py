class Node:
    def __init__(self, value, prev = None, next = None) -> None:
        self.value = value
        self.next = next
        self.prev = prev
    
    def __repr__(self) -> str:
        return f'Node: {self.value}'

class LinkedList:
    """ Class to implement a doubly linked list """

    def __init__(self, head: Node) -> None:
        self.head = head

    def __repr__(self) -> str:
        curr = self.head
        li = []
        while curr:
            li.append(curr.value)
            curr = curr.next
        return ' <-> '.join([str(i) for i in li])

    def add(self, value):
        if self.head == None:
            self.head = Node(value)
        else:
            curr = self.head
            while curr:
                if curr.next == None:
                    curr.next = Node(value, prev=curr)
                    break
                curr = curr.next
    
    def values(self):
        curr = self.head
        result = []
        while curr:
            result.append(curr.value)
            curr = curr.next
        return result

    def find(self, value):
        curr = self.head
        while curr:
            if curr.value == value:
                return curr
            curr = curr.next
    
    def delete(self, value):
        curr = self.head
        prev = None
        while curr:
            if curr.value == value:
                if prev:
                    prev.next = curr.next
                else:
                    self.head = curr.next
                return
            else:
                prev = curr
                curr = curr.next
        



if __name__ == '__main__':
    n3 = Node(3)
    n2 = Node(2, next=n3)
    n1 = Node(1, next=n2)
    linked_list = LinkedList(n1)
    linked_list.add(4)
    print(linked_list)
    linked_list.add(5)
    print('Added 5')
    print(linked_list.find(3))
    linked_list.delete(1)
    print('Removed 1')
    print(linked_list)