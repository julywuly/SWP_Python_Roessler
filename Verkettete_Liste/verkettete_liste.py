import random


class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def add_end(self, value):
        new_node = Node(value)
        if self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.size += 1

    def length(self):
        return self.size

    def print_elements(self):
        current = self.head
        elements = []
        while current:
            elements.append(current.value)
            current = current.next
        return elements

    def __iter__(self):
        self.current = self.head
        return self

    def __next__(self):
        if self.current is None:
            raise StopIteration
        value = self.current.value
        self.current = self.current.next
        return value

    def first_index(self, value):
        current = self.head
        index = 0
        while current:
            if current.value == value:
                return index
            current = current.next
            index += 1
        return -1

    def last_index(self, value):
        current = self.head
        index = -1
        position = 0
        while current:
            if current.value == value:
                index = position
            current = current.next
            position += 1
        return index

    def search_value(self, value):
        current = self.head
        while current:
            if current.value == value:
                return True
            current = current.next
        return False

    def delete(self, value):
        current = self.head
        previous = None

        if current and current.value == value:
            self.head = current.next
            if self.head is None:
                self.tail = None
            self.size -= 1
            return

        while current:
            if current.value == value:
                break
            previous = current
            current = current.next

        if current is None:
            print("Value not found!")
            return

        if current == self.tail:
            self.tail = previous
            if self.tail:
                self.tail.next = None
        else:
            previous.next = current.next

        self.size -= 1


if __name__ == "__main__":
    linked_list = LinkedList()

    for _ in range(10):
        linked_list.add_end(random.randint(1, 100))

    print("Length of the list:", linked_list.length())
    print("Elements of the list:", linked_list.print_elements())

    # Asking for a value to search
    value_to_search = int(input("Enter a value to search: "))
    print(f"Searching for value {value_to_search}: {linked_list.search_value(value_to_search)}")

    # Asking for a value to delete
    value_to_delete = int(input("Enter a value to delete: "))
    print(f"Deleting value {value_to_delete}")
    linked_list.delete(value_to_delete)
    print("Elements after deletion:", linked_list.print_elements())

    value_to_find_first_index = int(input("Enter a value to find its first index: "))
    print(f"First index of value {value_to_find_first_index}: {linked_list.first_index(value_to_find_first_index)}")

    value_to_find_last_index = int(input("Enter a value to find its last index: "))
    print(f"Last index of value {value_to_find_last_index}: {linked_list.last_index(value_to_find_last_index)}")

    print("Length of the list after all operations:", linked_list.length())
