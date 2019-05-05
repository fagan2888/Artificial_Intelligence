# TSP Iter Deep Search
from Graph import mapGraph
from Iter_deep import iter_Search

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

class tsp_iter_Search:
    def __init__(self, start_name):
        self.start_city = Node(start_name)


    def IDDFS(self):
        stack = []
        path = []
        cost = 0
        node1 = self.start_city
        stack.append(self.start_city)
        path.append(self.start_city.city_name)
        while(stack):

            new_list = []
            for child_city in Tree(node1.city_name).add_children():
                if child_city.city_name not in path:
                    new_list.append(child_city.city_name)
            if len(new_list) > 1:
                node1 = Node(new_list[0])
                for i in new_list[1:]:
                    stack.append(Node(i))
                path.append(node1.city_name)
            elif len(new_list) == 1:
                node1 = Node(new_list[0])
                path.append(node1.city_name)
            elif new_list == []:
                new_stack = []
                for m in stack:
                    if m.city_name not in path:
                        new_stack.append(Node(m.city_name))
                stack = new_stack
                if stack == []:
                    for i in range(len(path) - 1):
                        cost = cost + dist[path[i + 1] + path[i]]
                    new_path = (path[0])
                    for j in range(len(path) - 1):
                        new_path = ((new_path) + (' -> ') + (path[j + 1]))
                    return new_path, len(path), cost
                new_node = stack.pop()
                con_path = iter_Search(node1.city_name, new_node.city_name).IDDFS()
                conneted_path1 = con_path[0].split(' -> ')
                conneted_path1.pop(0)
                path.extend(conneted_path1)
                node1 = new_node
        for i in range(len(path) - 1):
            cost = cost + dist[path[i + 1] + path[i]]
        new_path = (path[0])
        for j in range(len(path) - 1):
            new_path = ((new_path) + (' -> ') + (path[j + 1]))
        return new_path, len(path), cost


    # def __init__(self, start_name):
    #     self.start_city = Node(start_name)
    #     self.num_node = []
    #     self.path = []
    #
    # def IDDFS(self):
    #     cost = 0
    #     for depth in range(15):
    #         self.path.append(self.start_city.city_name)
    #         found = self.DLS(self.start_city, depth, self.path)
    #         if found != None:
    #             for i in range(len(self.path) - 1):
    #                 cost = cost + dist[self.path[i + 1] + self.path[i]]
    #             return self.path, sum(self.num_node), cost
    #
    # def DLS(self, node, depth, path):
    #     if depth == 0 and all([i for i in graph.viewkeys() if i in self.path]):
    #         return self.path
    #     elif depth == 0 and not all([i for i in graph.viewkeys() if i in self.path]):
    #         new_list = []
    #         for item in graph.viewkeys():
    #             if item not in path:
    #                 new_list.append(item)
    #         new_node = new_list.pop()
    #         con_path = iter_Search(node, new_node).IDDFS()
    #         conneted_path1 = con_path[0].split(' -> ')
    #         conneted_path1.pop(0)
    #         self.path.extend(conneted_path1)
    #         return self.path
    #     elif depth > 0:
    #         name = node.city_name
    #         if Tree(name).add_children() == [] or all([i in self.path for i in Tree(name).get_Children_name()]):
    #             new_list = []
    #             for item in graph.viewkeys():
    #                 if item not in path:
    #                     new_list.append(item)
    #             new_node = new_list.pop()
    #             con_path = iter_Search(node, new_node).IDDFS()
    #             conneted_path1 = con_path[0].split(' -> ')
    #             conneted_path1.pop(0)
    #             self.path.extend(conneted_path1)
    #         else:
    #             for child in Tree(name).add_children():
    #                 if child.city_name not in path:
    #                     self.path.append(child.city_name)
    #                     found= self.DLS(child, depth - 1, path)
    #                     self.num_node.append(1)
    #                     if found != None:
    #                         return found
    #
    #     return None



