# Uniform Cost Search

from Graph import mapGraph

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


class unifcost_Search:
    def __init__(self, start_name, end_name):
        self.start_city = Node(start_name)
        self.end_city = Node(end_name)



    def find_endcity(self):
        queue = []
        path = {}
        goal = []
        num_node = 0
        queue.append((self.start_city.city_name, 0))
        path[self.start_city.city_name] = (self.start_city.city_name)
        while(queue):
            index = queue[0][1]
            order = 0
            for i in range(len(queue)):
                if queue[i][1] < index:
                    index = queue[i][1]
                    order = i
            name, cost = queue.pop(order)
            num_node += 1
            if name == self.end_city.city_name:
                if goal == []:
                    goal = [cost, path[name]]
                elif goal != [] and any([cost > queue[i][1] for i in range(len(queue))]):
                    continue
                elif all([cost <= queue[i][1] for i in range(len(queue))]):
                    return goal, num_node
                break
            elif name != self.end_city.city_name:
                if Tree(name).get_Children_name() == []:
                    continue

                else:
                    for child in Tree(name).get_Children_name():
                        if child in path.viewkeys():
                            old_cost = 0
                            for i in range(len(queue)):
                                if queue[i][0] == child:
                                    old_cost = queue[i][1]
                                    index1 = i
                            if old_cost > dist[child + name] + cost:
                                del queue[index1]
                                total_cost = dist[child + name] + cost
                                queue.append((child, total_cost))
                                tem_tuple = path[name]
                                path[child] = ((tem_tuple) + (' -> ') + (child))
                        elif child not in path.viewkeys():
                            total_cost = dist[child + name] + cost
                            queue.append((child, total_cost))
                            tem_tuple = path[name]
                            path[child] = ((tem_tuple) + (' -> ') + (child))
        return goal,num_node






