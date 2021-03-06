# LISTA SEQUENCIAL

class Node():
    def __init__(self, info):
        self.info = info

    def __str__(self):
        return str(self.info)

class Fila:
    def __init__(self, maxlen):
        self.maxlen = maxlen
        self.fila = []
        self.last = 0

    def insert(self, node):
        if self.last == self.maxlen:
            print('Array is already full.')
            return False

        self.fila.append(node)
        self.last += 1

    def parse(self):
        for i in self.fila:
            print(i.info, end=' ')
        print()

    def remove(self):
        self.fila.pop(0)
