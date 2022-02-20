class GraphNode:
    def __init__(self, data) -> None:
        self.data = data
        self.children = []
        pass

    def add_node(self, node):
        self.children.append(node)
        pass

    def remove_child(self, node):
        if node in self.children:
            self.children.remove(node)
        pass


class Graph:
    def __init__(self, nodes_list) -> None:
        self.nodes = nodes_list
        pass

    def add_edge(self, from_node: GraphNode, to_node: GraphNode):
        if from_node in self.nodes and to_node in self.nodes:
            from_node.add_node(to_node)
            to_node.add_node(from_node)
        pass

    def remove_edge(self, from_node: GraphNode, to_node: GraphNode):
        if from_node in self.nodes and to_node in self.nodes:
            from_node.remove_child(to_node)
            to_node.remove_child(from_node)
        pass 
    
    def dfs_search(self, root_node, search_value):
        stack = []

        names = [] 
        
        visited = [] 
        
        stack.append(root_node)
        names.append(root_node.data)
        
        while( len(stack) != 0):
            node : GraphNode = stack.pop()
            names.remove(node.data) 
            visited.append(node.data)
            children = node.children 
            for child in children:
                if child.data == search_value:
                    return child
                else:
                    if child.data not in visited:
                        stack.append(child)
                        names.append(child.data)

            


def depth_first_search():
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
    
    #print(graph1.nodes)

    #assert nodeA == graph1.dfs_search(nodeS, 'A')  
    assert nodeS == graph1.dfs_search(nodeP, 'S')
    #assert nodeR == graph1.dfs_search(nodeH, 'R')

depth_first_search()