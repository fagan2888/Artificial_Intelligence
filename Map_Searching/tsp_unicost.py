#TSP Uniform Cost Search

from Graph import mapGraph
from unicost import unifcost_Search
graph, dist = mapGraph()


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
        for child in graph[self.root.city_name]:
            self.root.children.append(Node(child))
        return self.root.children

    def get_Children_name(self):
        child_list = []
        for child in self.add_children():
            child_list.append(child.city_name)
        return child_list


class tsp_unifcost_Search:
    def __init__(self, start_name):
        self.start_city = Node(start_name)

    def find_min_ind(self, list1):
        mini = list1[0]
        index = 0
        for i in range(len(list1)):
            if list1[i] < mini:
                mini = list1[i]
                index = i
        return mini, index

    def search_all_nodes(self):
        queue = []
        path = []
        node1 = self.start_city
        # num_node = 0
        cost = 0
        # mini = 0
        # ind = 0
        queue.append(node1.city_name)
        path.append(node1.city_name)
        while(queue):
            cost_list = []
            coli = []
            child_list = []
            for child in Tree(node1.city_name).get_Children_name():
                if child not in path:
                    cost_list.append((child, dist[child + node1.city_name]))
                    child_list.append(child)
            if cost_list != []:
                for i in range(len(cost_list)):
                    coli.append(cost_list[i][1])
                mini, ind = self.find_min_ind(coli)
                node1_name, cost1 = cost_list.pop(ind)
                node1 = Node(node1_name)
                if node1_name in queue:
                    queue.remove(node1_name)
                path.append(node1_name)
                child_list.pop(ind)
                queue.extend(child_list)
            elif all([i in path for i in Tree(node1_name).get_Children_name()]):
                new_queue = []
                for n in queue:
                    if n not in path:
                        new_queue.append(n)
                queue = new_queue
                if queue == []:
                    for i in range(len(path) - 1):
                        cost = cost + dist[path[i + 1] + path[i]]
                    new_path = (path[0])
                    for j in range(len(path) - 1):
                        new_path = ((new_path) + (' -> ') + (path[j + 1]))
                    return new_path, len(path), cost
                node2 = queue.pop(0)
                if node2 in queue:
                    queue.remove(node2)
                con_path = unifcost_Search(node1_name, node2).find_endcity()
                conneted_path = con_path[0][1].split(' -> ')
                conneted_path = conneted_path[1:]
                path.extend(conneted_path)
                node1 = Node(node2)

        for i in range(len(path) - 1):
            cost = cost + dist[path[i + 1] + path[i]]
        new_path = (path[0])
        for j in range(len(path) - 1):
            new_path = ((new_path) + (' -> ') + (path[j + 1]))
        return new_path, len(path), cost


