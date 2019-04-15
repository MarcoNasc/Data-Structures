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
        node.before = self.top
        self.top = node
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
            return
        print('Top ->', end=' ')
        while node:
            print(node.info, end=' ')
            node = node.before
        print()
        return

    def delete(self):
        if not self.top:
            print('ERROR: Empty stack.')
            return
        self.top = temp
        self.top = self.top.before
        temp = None
        return

    def count_r(self):
        return self.count_re(self.top)

    def count_re(self, node):
        if not node:
            return 0
        return 1 + self.count_re(node.before)

    def height(self, node):
        return self.count_re(node.before)

    def depth(self, node):
        return self.height(self.top) - self.height(node)
