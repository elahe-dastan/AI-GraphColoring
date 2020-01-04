from random import randrange


class Node:

    def __init__(self,N):
        self.N = N
        self.color = randrange(4)

    def add_edge(self, E):
        self.E = E
