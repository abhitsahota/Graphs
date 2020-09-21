"""
https://leetcode.com/problems/destination-city/

Understand

Input: paths = [["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]]
Output: "Sao Paulo"
Explanation: Starting at "London" city you will reach "Sao Paulo" city which is the destination city.
Your trip consist of: "London" -> "New York" -> "Lima" -> "Sao Paulo".

Plan
1. Translate the problem into graph terminology
Vertex = a city
Edge = route from city to another city
Weights not needed

2. Build your graph
We can easily build a graph using adjacency lists from the input

3. Traverse your graph
Either BFT/DFT will work. You can start from any vertices.
If the current node we're at is not a key in the dictionary (graph), then it means it has
no outbound edges. That's the destination city
"""

from collections import deque

class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        if len(paths) == 0:
            return ''
        graph = self.createGraph(paths)
        stack = deque()
        stack.append(paths[0][0])
        visited = set()
        while len(stack) > 0:
            curr = stack.pop()
            visited.add(curr)
            if curr not in graph:
                return curr
            else:
                for neighbor in graph[curr]:
                    if neighbor not in visited:
                        stack.append(neighbor)
        return ''

    def createGraph(self, paths):
        graph = {}
        for edge in paths:
            origin, destination = edge[0], edge[1]
            if origin in graph:
                graph[origin].add(destination)
            else:
                graph[origin] = { destination }
        return graph



"""
Given two words (begin_word and end_word), and a dictionary's word list, return the shortest transformation sequence from begin_word to end_word, such that:

Only one letter can be changed at a time.
Each transformed word must exist in the word list. Note that begin_word is not a transformed word.
Note:

Return None if there is no such transformation sequence.
All words contain only lowercase alphabetic characters.
You may assume no duplicates in the word list.
You may assume begin_word and end_word are non-empty and are not the same.

Sample:
beginWord = "hit",
endWord = "cog",
wordList = ["hot","dot","dog","lot","log","cog"]
["hit", "hot", "dot", "dog", "cog"]

beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log"]
[]

1. Translate the problem into graph terminology
vertex - a word
edge - possible one letter transformation from a word to another word (undirected)
path - transformations of a word
weights - n/a

2. Build your graph
- we can create all possible transformations of beginWord and its transformation, but that would waste a lot of memory
- instead, we can determine which vertex to visit next if the transformation is in the wordList

3. Traverse the graph
- shortest = BFS
- we can traverse the graph using BFS and a queue
- use a set to avoid re-visiting nodes
- start from beginWord, and generate word transformations from it. enqueue nodes that are in the wordList
- keep track of the path we're currently on as we're traversing via a list
- once we find endWord, then we simply return the path to that node
"""

from collections import deque

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def findLadders(beginWord, endWord, wordList):
    words = set(wordList)
    visited = set()
    queue = deque()
    queue.append([beginWord])
    while len(queue) > 0:
        currPath = queue.popleft()
        currWord = currPath[-1]
        if currWord in visited:
            continue
        visited.add(currWord)
        if currWord == endWord:
            return currPath
        for i in range(len(currWord)):
            for letter in alphabet:
                transformedWord = currWord[:i] + letter + currWord[i + 1:]
                if transformedWord in words:
                    newPath = list(currPath)
                    newPath.append(transformedWord)
                    queue.append(newPath)
    return []

a = findLadders("hit", "cog", ["hot","dot","dog","lot","log","cog"])
print(a)

b = findLadders("hit", "cog", ["hot","dot","dog","lot","log"])
print(b)