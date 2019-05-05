# Iter Deep Search
from Graph import mapGraph

graph,dist = mapGraph()

class Node:
    def __init__(self, city_name):
        self.city_name = city_name
        self.children = []


class Tree:
    def __init__(self, city_name):
        self.root = Node(city_name)

    def bubble_sort(self, name_list):
        count = len(name_list)
        for i in range(0, count):
            for j in range(i + 1, count):
                if name_list[i] > name_list[j]:
                    name_list[i], name_list[j] = name_list[j], name_list[i]
        return name_list

    def add_children(self):
        g = self.bubble_sort(graph[self.root.city_name])
        for child in g:
            self.root.children.append(Node(child))
        return self.root.children

    def get_Children_name(self):
        child_list = []
        for child in self.add_children():
            child_list.append(child.city_name)
        return child_list

class iter_Search:
    def __init__(self, start_name, end_name):
        self.start_city = Node(start_name)
        self.end_city = Node(end_name)
        self.num_node = []

    def IDDFS(self):
        for depth in range(15):
            path = {}
            path[self.start_city.city_name] = (self.start_city.city_name)
            found = self.DLS(self.start_city, depth, path)
            if found != None:
                gn = []
                new_list = path[found.city_name].split(' -> ')
                for i in range(len(new_list) - 1):
                    gn.append(dist[new_list[i + 1] + new_list[i]])
                return path[found.city_name], sum(self.num_node), sum(gn)

    def DLS(self, node, depth, path):
        if depth == 0 and node.city_name == self.end_city.city_name:
            return node
        elif depth == 0 and node.city_name != self.end_city.city_name:
            del path[node.city_name]
        elif depth > 0:
            name = node.city_name
            if Tree(name).add_children() == [] or all([i in path for i in Tree(name).get_Children_name()]):
                del path[name]
            else:
                for child in Tree(name).add_children():
                    if child.city_name not in path:
                        path[child.city_name] = ((path[name]) + (' -> ') + (child.city_name))
                        found= self.DLS(child, depth - 1, path)
                        self.num_node.append(1)
                        if found != None:
                            return found

        return None



