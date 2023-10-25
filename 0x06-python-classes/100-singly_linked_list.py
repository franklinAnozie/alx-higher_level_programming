#!/usr/bin/python3
"""Define classes for a singly-linked list."""


class Node(object):
    """Represent a node in a singly-linked list."""
    def __init__(self, data, next_node=None):
        """Initialize a new Node.
        Args:
            data (int): The data of the new Node.
            next_node (Node): The next node of the new Node.
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Get/set the data of the Node."""
        return self.__data

    @data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        else:
            self.__data = value

    @property
    def next_node(self):
        """Get/set the next_node of the Node."""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        else:
            self.__next_node = value


class SinglyLinkedList:
    """Represent a singly-linked list."""
    def __init__(self):
        """Initalize a new SinglyLinkedList."""
        self.__head = None

    def sorted_insert(self, value):
        """Insert a new Node to the SinglyLinkedList.
        The node is inserted into the list at the correct
        ordered numerical position.
        Args:
            value (Node): The new Node to insert.
        """
        new_node = Node(value)
        if self.__head is None:
            new_node.next_node = None
            self.__head = new_node
        elif self.__head.data > value:
            new_node.next_node = self.__head
            self.__head = new_node
        else:
            temp_node = self.__head
            while (temp_node.next_node is not None
                   and temp_node.next_node.data < value):
                temp_node = temp_node.next_node
            new_node.next_node = temp_node.next_node
            temp_node.next_node = new_node

    def __str__(self):
        """Define the print() representation of a SinglyLinkedList."""
        nodes = []
        temp_node = self.__head
        while temp_node is not None:
            nodes.append(str(temp_node.data))
            temp_node = temp_node.next_node
        return '\n'.join(nodes)
