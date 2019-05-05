from tsp_bfs import tsp_bfs_Search
from tsp_dfs import tsp_dfs_Search
from tsp_iter import tsp_iter_Search
from tsp_unicost import tsp_unifcost_Search
from tsp_astar import tps_astar_Search
import csv


def main():
    # print('input the origin:')
    # origin = raw_input()
    # print('input algorithm choice (B, D, I, U, A):')
    # choice = raw_input()
    if choice == 'B':
        c, num, cost = tsp_bfs_Search(origin).search_all_nodes()
        print('total number of nodes expanded:')
        print(num)
        print('solution path:')
        print(c)
        print('cost:')
        print(cost)
    if choice == 'D':
        c, num, cost = tsp_dfs_Search(origin).search_all_nodes()
        print('total number of nodes expanded:')
        print(num)
        print('solution path:')
        print(c)
        print('cost:')
        print(cost)
    if choice == 'I':
        c, num, cost = tsp_iter_Search(origin).IDDFS()
        print('total number of nodes expanded:')
        print(num)
        print('solution path:')
        print(c)
        print('cost:')
        print(cost)
    if choice == 'U':
        path1, num1, cost1 = tsp_unifcost_Search(origin).search_all_nodes()
        print('total number of nodes expanded:')
        print(num1)
        print('solution path:')
        print(path1)
        print('cost:')
        print(cost1)
    if choice == 'A':
        path2, num, cost2 = tps_astar_Search(origin).search_all_nodes()
        print('total number of nodes expanded:')
        print(num)
        print('solution path:')
        print(path2)
        print('cost:')
        print(cost2)

if __name__ == '__main__':
    text = []
    with open('tsp.txt', 'r') as file1:
        csvreader = csv.reader(file1)
        for line in csvreader:
            text.append(line)

    origin = text[0][0]
    destination = text[1][0]
    choice = text[2][0]
    main()


