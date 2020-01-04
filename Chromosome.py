from Config import Config


class Chromosome:
    def __init__(self):
        iran_map = Config()
        self.nodes = iran_map.make_chromosome()

    def fitness_function(self):
        value = 0
        for node in self.nodes:
            color = node.color
            for neighbour_node in node.E:
                if color == neighbour_node.color:
                    value += 1
        return value/self.edge_size()

    def edge_size(self):
        size = 0
        for node in self.nodes:
            size += len(node.E)
        return size