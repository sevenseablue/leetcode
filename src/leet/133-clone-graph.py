# coding: utf8
"""
---------------------------------------------
    File Name: 133-clone-graph
    Description: 
    Author: wangdawei
    date:   2018/5/7
---------------------------------------------
    Change Activity: 
                    2018/5/7
---------------------------------------------    
"""


# Definition for a undirected graph node
class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []

class Solution:
    def __init__(self):
        self.nodeMap = {}
    # @param node, a undirected graph node
    # @return a undirected graph node
    def cloneGraph(self, node):
        if node is None: return None
        if node.label in self.nodeMap:
            return self.nodeMap.get(node.label)
        nodeclone = UndirectedGraphNode(node.label)
        self.nodeMap[node.label] = nodeclone
        for nodetmp in node.neighbors:
            nodeclone.neighbors.append(self.cloneGraph(nodetmp))
        return nodeclone
        pass

from collections import deque
class Solution:
    def cloneGraph(self, node):
        if node is None: return None
        que = deque()
        que.append(node)
        nodeCopy = UndirectedGraphNode(node.label)
        dic = {node:nodeCopy}
        while que:
            node = que.popleft()
            for neighbor in node.neighbors:
                if neighbor not in dic:
                    neighborCopy = UndirectedGraphNode(neighbor.label)
                    dic[neighbor] = neighborCopy
                    dic[node].neighbors.append(neighborCopy)
                    que.append(neighbor)
                else:
                    dic[node].neighbors.append(dic[neighbor])

        return nodeCopy


class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def cloneGraph(self, node):
        if not node:
            return None
        root = node
        stack = [root]
        newGraph = {}
        newGraph[root.label] = UndirectedGraphNode(root.label)
        while stack:
            node = stack.pop()
            for neighbor in node.neighbors:
                if neighbor.label not in newGraph:
                    stack.append(neighbor)
                    newGraph[neighbor.label] = UndirectedGraphNode(neighbor.label)
                newGraph[node.label].neighbors.append(newGraph[neighbor.label])
        return newGraph[root.label]
