from queue import Queue


class GraphNode:
    def __init__(self, data) -> None:
        self.data = data
        self.children = []

    def add_child(self, node):
        self.children.append(node)

    def remove_child(self, node):
        self.children.remove(node)   
        
class Graph: 
    
    def __init__(self, nodes ) -> None: 
         self.nodes = nodes
         pass 
     
    def add_edge(self, from_node:GraphNode, to_node:GraphNode):
        if from_node in self.nodes and to_node in self.nodes:
            from_node.add_child(to_node)
            to_node.add_child(from_node)
    
    def bfs_search(self, root_node, search_value): 
        queue = Queue()  
        queue.put(root_node)
        res = self.bfs(search_value,queue)
        pass   
    
    def bfs(self, search_value, queue:Queue):
        while(not queue.empty()):
            node:GraphNode = queue.get()
            if node.data == search_value:
                return node 
            else:
                for child in node.children:
                    queue.put(child) 
        return None
      
     
     
# test 

nodeG = GraphNode('G')
nodeR = GraphNode('R')
nodeA = GraphNode('A')
nodeP = GraphNode('P')
nodeH = GraphNode('H')
nodeS = GraphNode('S')

graph1 = Graph([nodeS,nodeH,nodeG,nodeP,nodeR,nodeA] ) 
graph1.add_edge(nodeG,nodeR)
graph1.add_edge(nodeA,nodeR)
graph1.add_edge(nodeA,nodeG)
graph1.add_edge(nodeR,nodeP)
graph1.add_edge(nodeH,nodeG)
graph1.add_edge(nodeH,nodeP)
graph1.add_edge(nodeS,nodeR) 

print(graph1.bfs_search(nodeS, 'A'))

#assert nodeA == graph1.bfs_search(nodeS, 'A')


 
