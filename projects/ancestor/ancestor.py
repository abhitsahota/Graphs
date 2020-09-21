'''
Conduct a BFS traversal to find all of the connect parent to the given child node
Need to build a graph of the children and parents from the list of lists

track the paths in a larger list
if there is no parent path then return -1

compare path lengths
    return the longest path
    if paths are equal
        return lower id number

'''

from util import Queue

def earliest_ancestor(ancestors, starting_node):
    # Create a graph that maps parents to keys and childs as the edges to other vectors

    # Check if the starting node is ever a child
    ct = 0
    for pair in ancestors:
        # If starting node never appears as the second number in a pair, it has no parents, so return -1
        if starting_node == pair[1]:
            ct += 1
    
    if ct == 0:
        return -1


    graph = createGraph(ancestors)

    # Conduct BFS

    q = Queue()
    q.enqueue([starting_node])
    list_of_paths = []
    visited = set()

    while q.size() > 0:
        path = q.dequeue()
        list_of_paths.append(path)
        curr = path[-1]

        if curr not in visited:
            visited.add(curr)
            for node in graph:
                if curr in graph[node]:
                    new_path = list(path)
                    new_path.append(node)
                    q.enqueue(new_path)

    max_size = 0
    o_ancestor = None
    for path in list_of_paths:
        size = len(path)

        if size > max_size:
            max_size = size
            new_o_ancestor = path[-1]
            o_ancestor = new_o_ancestor
        elif size == max_size:
            pot_o_ancestor = path[-1]
            if pot_o_ancestor < o_ancestor:
                o_ancestor = pot_o_ancestor
    print(o_ancestor)
    return o_ancestor
            



def createGraph(ancestors):

    graph = {}

    for pair in ancestors:
        parent, child = pair[0], pair[1]
        if parent in graph:
            graph[parent].add(child)
        else:
            graph[parent] = { child }

    return graph

test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]

earliest_ancestor(test_ancestors, 1)