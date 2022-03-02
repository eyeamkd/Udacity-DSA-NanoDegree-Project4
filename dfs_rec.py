from unittest import result


class GraphNode:
    def __init__(self, data) -> None:
        self.data = data
        self.children = []

    def add_child(self, node):
        self.children.append(node)

    def remove_child(self, node):
        self.children.remove(node)


class Graph:

    def __init__(self, nodes) -> None:
        self.nodes = nodes
        self.dfs_rec_stack = []
        self.dfs_visited = []
        pass

    def add_edge(self, from_node: GraphNode, to_node: GraphNode):
        if from_node in self.nodes and to_node in self.nodes:
            from_node.add_child(to_node)
            to_node.add_child(from_node)

    def remove_edge(self, from_node: GraphNode, to_node: GraphNode):
        if from_node in self.nodes and to_node in self.nodes:
            from_node.remove_child(from_node)
            to_node.remove_child(to_node)

    def recursive_search(self, node: GraphNode, search_value: str):  
        if node.data == search_value: 
            found = True 
            self.dfs_visited = []
            return node
        else: 
            found = False 
            res = None 
            if node.data not in self.dfs_visited: 
                self.dfs_visited.append(node.data)
            if len(node.children) == 0:
                return None
            else: 
                for child in node.children:
                    if child.data not in self.dfs_visited:
                        self.dfs_visited.append(child.data)
                        res = self.recursive_search(child, search_value)  
                        if res!=None:
                            break
                return res
              
                


# Creating a graph as above.
nodeG = GraphNode('G')
nodeR = GraphNode('R')
nodeA = GraphNode('A')
nodeP = GraphNode('P')
nodeH = GraphNode('H')
nodeS = GraphNode('S')

graph1 = Graph([nodeS, nodeH, nodeG, nodeP, nodeR, nodeA])

graph1.add_edge(nodeG, nodeR)
graph1.add_edge(nodeA, nodeR)
graph1.add_edge(nodeA, nodeG)
graph1.add_edge(nodeR, nodeP)
graph1.add_edge(nodeH, nodeG)
graph1.add_edge(nodeH, nodeP)
graph1.add_edge(nodeS, nodeR)


for each in graph1.nodes:
    print('parent node = ', each.data, end='\nchildren\n')
    for each in each.children:
        print(each.data, end=' ')
    print('\n')

# print(graph1.recursive_search(nodeP, 'S').data)
#
# print(graph1.recursive_search(nodeG, 'A').data)
assert nodeA.data == graph1.recursive_search(nodeG, 'A').data
# # # # #assert nodeA == graph1.recursive_search(nodeS, 'A')
assert nodeS.data == graph1.recursive_search(nodeP, 'S').data
assert nodeR.data == graph1.recursive_search(nodeH, 'R').data
