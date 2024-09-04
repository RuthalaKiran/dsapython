class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_begining(self, data):
        node = Node(data, self.head)
        self.head = node

    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return
        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = Node(data, None)

    def insert_at(self, index, data):
        if index < 0 or index > self.get_length():
            raise Exception("invalid index")
        if index == 0:
            self.insert_at_begining(data)
            return
        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                node = Node(data, itr.next)
                itr.next = node
                break
            itr = itr.next
            count += 1

    def print(self):
        if self.head is None:
            print("Linked List is empty")
            return
        itr = self.head
        llstr = ""
        while itr:
            llstr += str(itr.data) + "-->"
            itr = itr.next
        print(llstr)

    def insert_values(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)

    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next
        return count

    def remove_at(self, index):
        if index < 0 or index >= self.get_length():
            raise Exception("Invalid index")
        if index == 0:
            self.head = self.head.next
            return
        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                itr.next = itr.next.next
                break
            itr = itr.next
            count += 1
        print("removed")

    def remove_start(self):
        if self.head is None:
            print("there is not elements to remove")
            return
        self.head = self.head.next

    def remove_end(self):
        if not self.head:
            print("list is empty")
            return
        if not self.head.next:
            self.head = None
            return
        second_last_node = self.head
        while second_last_node.next.next:
            second_last_node = second_last_node.next
        second_last_node.next = None

    def search_value(self, val):
        if not self.head:
            print("list is empty")
            return
        itr = self.head
        while itr:
            if itr.data == val:
                print(f"{val} found")
                return
            itr = itr.next
        print(f"{val} not found")

    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev
    


if __name__ == "__main__":
    ll = LinkedList()
    ll.insert_values([1, 2, 3, 4, 5])
    print("length of linkedlist", ll.get_length())
    ll.print()
    ll.insert_at(4, "mango")
    ll.print()
    print("length of linkedlist", ll.get_length())
    ll.search_value(10)
    ll.reverse()
    ll.print()
