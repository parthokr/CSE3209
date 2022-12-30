import sys
from copy import deepcopy
from pprint import pprint

sys.stdin = open('input.txt', 'r')
v = int(input("No of nodes: "))
labels = input("Node labels: ").split(' ')
e = int(input("No of edges: "))

graph = {}
for i in range(e):
    _from, to, cost = input(f"Enter edge {i+1}: ").split()
    tmp = graph.get(_from, [])
    tmp.append((to, cost))
    graph[_from] = tmp

pprint(graph)

start = input('Start node: ')
goal = input('Goal node: ')
print()


def bfs():
    queue = [start]
    visited = [] # marking already visited node to get around cyclic graph
    routes = {}
    estimated_cost = {}

    while len(queue) > 0:
        # print(queue)
        current = queue.pop(0)
        print(f'Selected: {current} to expand')
        if current == goal:
            print(f'Found {goal}')
            goal_route = routes[goal] + [goal]
            for i in range(len(goal_route)):
                print(f'{goal_route[i]}', end=["-->", "\n"][i == len(goal_route)-1])
            print(estimated_cost[goal])
            return
        for to_cost in graph[current]:
            to, cost = to_cost
            if to not in visited:
                print(f'Visiting {to}')
                visited.append(to)
                queue.append(to)

                tmp = deepcopy(routes.get(current, []))
                tmp.append(current)

                routes[to] = tmp

                estimated_cost[to] = estimated_cost.get(to, estimated_cost.get(current, 0)) + int(cost)

bfs()




