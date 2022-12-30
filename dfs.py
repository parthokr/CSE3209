import sys
from copy import deepcopy
from pprint import pprint

def dfs():
    v = int(input("No of nodes: "))
    labels = input("Node labels: ").split(' ')
    e = int(input("No of edges: "))

    graph = {}
    for i in range(e):
        _from, to, cost = input(f"Enter edge {i + 1}: ").split()
        tmp = graph.get(_from, [])
        tmp.append((to, cost))
        graph[_from] = tmp

    pprint(graph)

    start = input('Start node: ')
    goal = input('Goal node: ')
    stack = [(start, 0)]
    visited = [] # marking already visited node to get around cyclic graph
    routes = {}
    estimated_cost = {}
    max_depth = 5
    while len(stack) > 0:
        # print(stack)
        current, depth = stack.pop()
        if depth >= max_depth:
            continue
        if current not in visited:
            visited.append(current)

        print(f'Selected: {current} to expand')

        if current == goal:
            print(f'Found {goal}')
            goal_route = routes[goal] + [goal]
            for i in range(len(goal_route)):
                print(f'{goal_route[i]}', end=["-->", "\n"][i == len(goal_route)-1])
            print(estimated_cost[goal])

            print(routes)
            print(estimated_cost)
            return

        for to, cost in graph.get(current, [])[::-1]:
            if to not in visited:
                visited.append(to)
                stack.append((to, depth+1))

                tmp = deepcopy(routes.get(current, []))
                tmp.append(current)

                routes[to] = tmp

                estimated_cost[to] = estimated_cost.get(to, estimated_cost.get(current, 0)) + int(cost)


if __name__ == '__main__':
    sys.stdin = open('input.txt', 'r')
    t = int(input())
    for _ in range(t):
        dfs()



