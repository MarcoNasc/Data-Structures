# PILHA ENCADEADA


class Node():
    def __init__(self, i):
        self.info = i
        self.before = None

    def __str__(self):
        return str(self.info)


class LinkedStack():
    def __init__(self):
        self.top = None

    def insert(self, node):
        if not self.top:
            self.top = node
            return
        j = self.top
        self.top = node
        node.before = j
        return

    def access(self):
        if not self.top:
            print('ERROR: Empty stack.')
            return
        return self.top.info

    def parse(self):
        node = self.top
        if not node:
            print('ERROR: Empty stack.')
        while node:
            print(node.info, end=' ')
            node = node.before
        print()

    def delete(self):
        if not self.top:
            print('ERROR: Empty stack.')
            return
        j = self.top.before
        self.top.before = None
        self.top = j
        return
