import sys
from copy import deepcopy
from pprint import pprint
from queue import PriorityQueue


def ucs():
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
    pq = PriorityQueue()
    pq.put((0, (start, None)))
    popped = []
    routes = {}
    estimated_cost = {start: 0}
    while not pq.empty():
        current, prev = pq.get()[1]  # pop from the heap
        if current not in popped:  # if the popped node is not already popped
            popped.append(current)
            # tmp = deepcopy(routes.get(prev, []))
            # if prev is not None:
            #     tmp.append(prev)
            # routes[current] = tmp
            for to, cost in graph.get(current, []):  # expand current node
                old_cost = estimated_cost.get(to, sys.maxsize)  # default is inf
                new_cost = estimated_cost.get(current) + int(cost)  # eval new cost
                if new_cost < old_cost:  # if new cost is less than the previous one
                    print(f'Min {to} for {current}')
                    # print(routes.get(to, []))
                    # print(routes.get(current, []))
                    estimated_cost[to] = new_cost # set new minimized cost
                    routes[to] = routes.get(current, []) + [current]  # update route

                pq.put((cost, (to, current)))
    # print(estimated_cost)
    # print(routes)
    print(f'Found {goal}')
    goal_route = routes[goal] + [goal]
    for i in range(len(goal_route)):
        print(f'{goal_route[i]}', end=["-->", "\n"][i == len(goal_route) - 1])
    print(estimated_cost[goal])
    print(estimated_cost)
    print(routes)

if __name__ == '__main__':
    sys.stdin = open('input.txt', 'r')
    t = int(input())
    for _ in range(t):
        ucs()
