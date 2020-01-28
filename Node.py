from random import randrange


class Node:

    def __init__(self,id):
        self.id = id
        self.color = randrange(4)

    def add_edge(self, E):
        self.E = E
