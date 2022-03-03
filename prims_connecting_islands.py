class Graph:
    def __init__(self) -> None:
        self.nodes = set()  
        self.nodes_names = set()
        pass 
    
    def add_node(self, node):
        self.nodes.add(node) 
        self.nodes_names.add(node.name) 
    
    def get_node_by_name(self, name):
        if name in self.nodes_names:
            for node in self.nodes:
                if node.name == name:
                    return node
        return None 
    
    def __repr__(self) -> str:
        for node in self.nodes:
            node.print_children()
        return '' 

class GraphNode:
    def __init__(self, name) -> None: 
        self.name = name 
        self.children = {}
    
    def add_child(self, name ,distance):
        self.children[name] = distance 
    
    def print_children(self):
        for child in self.children.keys():
            print(self.name,"------>",child) 

def get_graph(num_islands, bridge_config):
    graph = Graph();
    for island in range(num_islands):
        config = bridge_config[island] 
        island_1 = config[0] 
        island_2 = config[1] 
        cost = config[2] 
        if island_1 in graph.nodes_names:
            island_1_node = graph.get_node_by_name(island_1) 
        else:
            island_1_node : GraphNode = GraphNode(island_1)  
            graph.add_node(island_1_node)
        if island_2 in graph.nodes_names:
            island_2_node = graph.get_node_by_name(island_2) 
        else:
            island_2_node : GraphNode = GraphNode(island_2)
            graph.add_node(island_2_node) 
        
        island_1_node.add_child(island_2, cost) 
        island_2_node.add_child(island_1, cost) 
    return graph     

def find_shortest_path(num_islands, bridge_config):  
    graph = get_graph(num_islands, bridge_config) 
    result = {} 
    root_node = list(graph.nodes)[0]   
    current_node: GraphNode = root_node 
    children = current_node.children 
    min_distance = {'dist':9999, 'name':None};
    for child in children.keys():
        if children[child] < min_distance.dist:
            min_distance.dist = children[child]
            min_distance.name = child
    current_node = graph.get_node_by_name(min_distance.name) 
    result[current_node.name] = min_distance.dist
    print(graph) 
        
        
    
    

# test   

num_islands = 4
bridge_config = [[1, 2, 1], [2, 3, 4], [1, 4, 3], [4, 3, 2], [1, 3, 10]] 

find_shortest_path(num_islands, bridge_config)