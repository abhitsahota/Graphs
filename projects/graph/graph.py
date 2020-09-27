"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy

class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        # Create the new key with the vertex ID and se thte value to an empty set (meaning no edges yet)
        try:
            if vertex_id not in self.vertices:
                self.vertices[vertex_id] = set()
        except:
            return Exception

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        # Find vertex v1 and add v2 to the set of edges
        try: 
            if v1 in self.vertices and v2 in self.vertices:
                self.vertices[v1].add(v2)
        except:
            return Exception

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        try: 
            if vertex_id in self.vertices:
                return self.vertices[vertex_id]
        except: 
            return Exception


    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        # Create an empty queue and enqueue the starting_vertex
        # create empty set to track visited verticies

        #while the queue is not empty
            # get th current vertex (dequeue from queue)

            # Check if the current vertex has been visited
                # print the current vertes
                # mark the current vertex as visited
                    # add the current vertex to a visited set

                # queue up all the current vertex's neighhours (seo we can visit them next)

        the_que = Queue()
        the_que.enqueue(starting_vertex)
        track_set = set()

        while the_que.size() > 0:
            curr = the_que.popleft()
        
            if curr not in track_set:
                print(curr)
                track_set.add(curr)
                for neighbour in self.users[curr]:
                    the_que.append(neighbour)


    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        # Create an empty stack and add the starting_vertex
        # create empty set to track visited verticies

        #while the stack is not empty
            # get th current vertex (dequeue from queue)

            # Check if the current vertex has been visited
                # print the current vertes
                # mark the current vertex as visited
                    # add the current vertex to a visited set

                # push up all the current vertex's neighhours (seo we can visit them next)
        the_stack = Stack()
        the_stack.push(starting_vertex)
        track_set = set()

        while the_stack.size() > 0:
            curr = the_stack.pop()
        
            if curr not in track_set:
                print(curr)
                track_set.add(curr)
                for neighbour in self.vertices[curr]:
                    the_stack.push(neighbour)


    def dft_recursive(self, starting_vertex, visited = None):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        if visited == None:
            visited = []

        visited.append(starting_vertex)
        for neighbour in self.vertices[starting_vertex]:
            if neighbour not in visited:
                self.dft_recursive(neighbour, visited)

        return visited

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        # We want to track if there is a path between the verticies and what the shortest path is

        # Create an empty queue and enqueue the path to the (attaching a list within the queue) starting_vertex
        # create empty set to track visited verticies



        #while the queue is not empty
            # get th current vertex path (dequeue from queue)
            # set the current vertes t the last element of the path

            # Check if the current vertex has been visited

                # Check if the current verties is the destination
                    # if it is, then return

                # mark the current vertex as visited
                    # add the current vertex to a visited set
                    
                # queue up news path with each path
                    # take current path
                    # append the neight to it
                    # queue up the new path

        the_que = Queue()
        start = [starting_vertex]
        the_que.enqueue(start)
        track_set = set()

        while the_que:
            path = the_que.dequeue()
            curr = path[-1]
        
            if curr not in track_set:
                if curr == destination_vertex:
                    return path
                else:
                    track_set.add(curr)

                for neighbour in self.vertices[curr]:
                    new_path = list(path) # needed to create a brand new list not just point to existing path list in memory
                    new_path.append(neighbour)

                    the_que.enqueue(new_path)
        return None


    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        
        the_stack = Stack()
        start = [starting_vertex]
        the_stack.push(start)
        track_set = set()

        while the_stack:
            path = the_stack.pop()
            curr = path[-1]
        
            if curr not in track_set:
                if curr == destination_vertex:
                    return path
                else:
                    track_set.add(curr)

                for neighbour in self.vertices[curr]:
                    new_path = list(path) # needed to create a brand new list not just point to existing path list in memory
                    new_path.append(neighbour)

                    the_stack.push(new_path)
        return None

    def dfs_recursive(self, starting_vertex, destination_vertex, path = []):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        visited = set()
        return self.dft_recursive_helper([starting_vertex], destination_vertex, visited)
    
    # retuns path starting vertex to destination vertex, else retunr empty list
    def dfs_recursive_helper(self, curr_path, destination_vertex, visited):
        curr_vertex = curr_path[-1]

        if curr_vertex == destination_vertex: #base case
            return curr_path

        visited.add(curr_vertex)

        for neighbors in self.get_neighbors(curr_vertex):
            if neighbors not in visited:
                new_path = list(path)
                new_path.append(neighbors)
                res = self.dfs_recursive_helper(new_path, destination_vertex, visited)
                if len(res) > 0: # if non empty array is returned
                    return res

        return []


if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    # print(graph.vertices)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    # graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    # graph.dft(1)
    # graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    # print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    # print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))
