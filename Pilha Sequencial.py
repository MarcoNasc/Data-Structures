# PILHA SEQUENCIAL


class Node():
    def __init__(self, info):
        self.info = info

    def __str__(self):
        return str(self.info)


class SeqStack():
    def __init__(self, maxi):
        self.stack = []
        self.maxi = maxi - 1
        self.top = 0

    def insert(self, node):
        if self.top > self.maxi:
            print('ERROR:\n Risk of stack overflow, operation aborted')
            return
        self.stack.append(node)
        self.top += 1

    def unstacking(self):
        try:
            self.stack.pop()
            self.top -= 1
            return
        except IndexError:
            print('ERROR:\nEmpty stack.')

    def is_empty(self):
        try:
            if self.stack[0]:
                return False
        except IndexError:
            return True

    def size(self):
        print(self.top)
        return

    def parse(self):
        try:
            for i in self.stack:
                print(i, end=' ')
            print()
            return
        except IndexError:
            print('ERROR:\n Empty stack.')
            return
