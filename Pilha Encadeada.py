# PILHA ENCADEADA


class Node():
    def __init__(self, i):
        self.info = i
        self.next = None

    def __str__(self):
        return str(self.info)


class LinkedStack():
    def __init__(self):
        self.first = None
        self.last = None

    def insert(self, node):
        if not self.first:
            self.first = node
            self.last = node
            return
        j = self.first
        self.first = node
        node.next = j
        return

    def access(self):
        if not self.first:
            print('ERROR: Empty stack.')
            return
        return self.first.info

    def parse(self):
        node = self.first
        if not node:
            print('ERROR: Empty stack.')
        while node:
            print(node.info, end=' ')
            node = node.next
        print()

    def delete(self):
        if not self.first:
            print('ERROR: Empty stack.')
            return
        j = self.first.next
        self.first.next = None
        self.first = j
        return
