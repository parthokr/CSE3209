import sys
from pprint import pprint
from queue import PriorityQueue


def a_star():
    v = int(input("No of nodes: "))
    heuristics = {}
    for i in range(v):
        node, h = input(f"Enter node {i + 1}: ").split()
        heuristics[node] = int(h) if h != 'INF' else sys.maxsize

    e = int(input("No of edges: "))
    graph = {}
    for i in range(e):
        _from, to, cost = input(f"Enter edge {i + 1}: ").split()
        tmp = graph.get(_from, [])
        tmp.append((to, int(cost)))
        graph[_from] = tmp

    pprint(graph)

    start = input('Start node: ')
    goal = input('Goal node: ')
    pq = PriorityQueue()
    pq.put((heuristics[start] + 0, (start, None)))
    popped = []
    routes = {}
    estimated_cost = {start: 0}
    while not pq.empty():
        current, prev = pq.get()[1]  # pop from the heap
        if (current, estimated_cost[current]) not in popped:  # if the popped node is not already popped
            print(f'Selected {current, prev}')
            popped.append((current, estimated_cost[current]))
            print(routes)
            for to, cost in graph.get(current, []):  # expand current node
                old_cost = estimated_cost.get(to, sys.maxsize)  # default is inf
                new_cost = estimated_cost.get(current) + int(cost)  # eval new cost
                if new_cost < old_cost:  # if new cost is less than the previous one
                    estimated_cost[to] = new_cost
                    routes[to] = routes.get(current, []) + [current]

                pq.put((cost + heuristics[to], (to, current)))
    print(f'Found {goal}')
    goal_route = routes[goal] + [goal]
    for i in range(len(goal_route)):
        print(f'{goal_route[i]}', end=["-->", "\n"][i == len(goal_route) - 1])
    print(routes)
    print(estimated_cost[goal])


if __name__ == '__main__':
    sys.stdin = open('input_a_heuristics.txt', 'r')
    t = int(input())
    for _ in range(t):
        a_star()
