import sys


def hc():
    v = int(input("No of nodes: "))
    h = {}
    for _ in range(v):
        node, _h = input('(node, h): ').split(' ')
        h[node] = int(_h)
    e = int(input("No of edges: "))
    graph = {}
    for i in range(e):
        _from, to = input(f"Enter edge {i + 1}: ").split()
        graph[_from] = to

    start = input('Start node: ')
    current = start
    while True:
        # if h[graph[current]] > h[current]:
        #     current = graph[current]
        # else:
        #     break
        # print(current)
        current = graph.get(current)
        if current is None or h[graph[current]] < h[current]:
            break


    print(current)


if __name__ == '__main__':
    sys.stdin = open('input_hc.txt', 'r')
    t = int(input())
    for _ in range(t):
        hc()
