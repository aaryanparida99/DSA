from collections import deque

graph = {
    'A' : ['B','C','D'],
    'B' : ['E'],
    'C' : ['E', 'F'],
    'D' : ['F'],
    'E' : ['G'],
    'F' : ['G'],
    'G' : []
}

visited = set()

def breadth_first_search(visited,graph,root):
    queue = deque([root,])
    visited.add(root)

    while queue:
        node = queue.pop()
        print(node, end=" ")

        for neighbour in graph[node]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.appendleft(neighbour)


#Driver Code
breadth_first_search(visited, graph, 'A')