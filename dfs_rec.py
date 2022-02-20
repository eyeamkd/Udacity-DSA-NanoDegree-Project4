class GraphNode:
    def __init__(self, data) -> None:
         self.data = data
         self.children = [] 
    
    def add_child(self,node):
        self.children.append(node)
    
    def remove_child(self,node):
        self.children.remove(node) 
    
class Graph:
    
    def __init__(self, root_value) -> None: 
        self.root_node = GraphNode(root_value)
        pass 
    
    def add_edge(self, from_node: GraphNode, to_node: GraphNode):
        from_node.add_child(to_node)
        to_node.add_child(from_node) 
    
    def remove_edge(self, from_node:GraphNode, to_node: GraphNode):
        from_node.remove_child(from_node)
        to_node.remove_child(to_node)
    
    
        