# FILA ENCADEADA


class Node():
    def __init__(self, i):
        self.info = i
        self.next = None

    def __str__(self):
        return str(self.info)


class FilaE():
    def __init__(self):
        self.first = None
        self.last = None

    def insert(self, node):
        if not self.first:
            self.first = node
            self.last = node
            return

        self.last.next = node
        self.last = node
        return

    def access(self):
        if self.first:
            return self.first.info

    def parse(self):
        node = self.first
        while node:
            print(node.info, end=' ')
            node = node.next
        print()

    def delete(self):
        if not self.first:
            return
        temp = self.first.next
        self.first.next = None
        self.first = temp
        return

    def count_it(self):
        node = self.first
        cont = 0
        while node:
            cont += 1
            node = node.next
        return cont

    def count_r(self):
        return self.count_re(self.first)

    def count_re(self, node):
        if not node:
            return 0
        return 1 + self.count_re(node.next)

    def height(self, node):
        return self.count_re(node.next)

    def depth(self, node):
        return self.height(self.first) - self.height(node)

    def is_ordered(self):
        node = self.first
        while node.next:
            if node.next.info > node.info:
                node = node.next
            else:
                return False
        return True

    def is_equal(self, other):
        node1 = self.first
        node2 = other.first
        while node1:
            if node1.info != node2.info:
                return False
            else:
                node1 = node1.next
                node2 = node2.next
        return True

    def is_equal_r(self, other):

        if self.count_it() != other.count_it():
            return False

        return bool(self.is_equal_re(self.first, other.first))

    def is_equal_re(self, node1, node2):

        if not node1:
            return 1
        return node1.info == node2.info * self.is_equal_re(node1.next, node2.next)
