# PILHA SEQUENCIAL

from nodo import *

class SeqStack():
    def __init__(self, max):
        self.stack = []
        self.max = max - 1
        self.top = 0

    def stacking(self, node):
        if self.top > self.max:
            print('ERROR:\n risk of stack overflow, operation aborted')
        elif self.top <= self.max:
            self.stack.append(node)
            self.top += 1

    def unstacking(self):
        try:
            self.stack.pop()
            self.top -= 1
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

    def parse(self):
        try:
            for i in self.stack:
                print(i.val, end=' ')
            print()
        except IndexError:
            print('ERROR:\n empty stack.')
