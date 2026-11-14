#!/usr/bin/env python3
"""
CSC 301 - Linked List Example
Student: Akerele Paul Bayo
Matric: 240502023
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        """Insert a new node at the beginning of the list"""
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        print(f"Inserted {data} at the beginning")

    def display(self):
        """Display all elements in the linked list"""
        if self.head is None:
            print("Linked List is empty")
            return

        current = self.head
        print("Linked List: ", end="")
        while current:
            print(current.data, end=" → ")
            current = current.next
        print("None")


def main():
    ll = LinkedList()

    print("=== Linked List Operations ===\n")
    ll.insert_at_beginning(30)
    ll.insert_at_beginning(20)
    ll.insert_at_beginning(10)
    ll.insert_at_beginning(5)

    print()
    ll.display()

if __name__ == "__main__":
    main()
