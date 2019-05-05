import csv


def mapGraph():
    graph = {}
    distances = {}
    edge_count = 0
    with open('graph 2.txt', 'r') as filein:
        csvreader = csv.reader(filein)
        for line in csvreader:
            city1 = line[0]
            city2 = line[1].strip()
            edge_count += 1
            if city1 in graph:
                graph[city1].append(city2)
            else:
                graph[city1] = [city2]
            if city2 in graph:
                graph[city2].append(city1)
            else:
                graph[city2] = [city1]
            dist = float(line[2].strip())
            distances[city1 + city2] = dist
            distances[city2 + city1] = dist
    return graph, distances

