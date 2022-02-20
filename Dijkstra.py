class Node:
    def __init__(self, name):
        self.name = name
        self.children = {}

    def join(self, node, distance):
        self.children[node.name] = {'distance': distance, 'node': node}


def find_shortest_path():
    result = {}
    unvisited = set()

    node_a = Node('A')
    node_b = Node('B')
    node_c = Node('C')
    node_d = Node('D')
    node_e = Node('E')
    node_f = Node('F')

    node_a.join(node_d, 2)
    node_a.join(node_c, 4)
    node_a.join(node_b, 5)

    node_b.join(node_a, 5)
    node_b.join(node_c, 2)
    node_b.join(node_f, 2)

    node_f.join(node_b, 2)
    node_f.join(node_e, 2)
    node_f.join(node_c, 3)

    node_c.join(node_b, 2)
    node_c.join(node_e, 1)
    node_c.join(node_d, 1) 
    node_c.join(node_a,4)
    node_c.join(node_f,3)

    node_d.join(node_a, 2)
    node_d.join(node_c, 1) 
    
    node_e.join(node_c,1)
    node_e.join(node_f,2)

    unvisited.add('B')
    unvisited.add('C')
    unvisited.add('D')
    unvisited.add('E')
    unvisited.add('F') 
    
    to_visit = set() 
    visited = set()

    source_node = node_a  
    result[node_a.name] = 0
    visited.add(source_node)
    to_visit.add(source_node) 
    
    while len(to_visit) > 0:
        current_node : Node = to_visit.pop()  
        visited.add(current_node.name)
        current_node_children = current_node.children 
        least_distance = 9999;  
        least_distance_node = None;
        for child in current_node_children: 
            if child not in visited:
                if current_node_children[child]['distance'] < least_distance:
                    least_distance = current_node_children[child]['distance'] 
                    least_distance_node = current_node_children[child]['node'] 
            
                if least_distance_node.name in result.keys(): 
                    if result[least_distance_node.name] > least_distance + result[current_node.name] :
                        result[least_distance_node.name] = least_distance + result[current_node.name]  
                else:
                    result[least_distance_node.name] = least_distance + result[current_node.name] 
            
        if least_distance_node is not None:
            to_visit.add(least_distance_node)
        
        # for child in current_node_children:   
        #     # child node is already present in the result dict  
        #     if child in result.keys():
        #         if result[child] > current_node_children[child]['distance'] + result[current_node.name]:
        #             result[child] = current_node_children[child]['distance'] + result[current_node.name]
        #     else:
        #     # child node is not present in the result dict  
        #         print("child is", child)
        #         result[child] = current_node_children[child]['distance'] + result[current_node.name] 
        #     if child not in visited:  
        #         to_visit.add(current_node.children[child]['node'])
            
         
             

    # while len(unvisited) > 0:
    #     current_node_name = unvisited.pop()

    #     if current_node_name in source_node.children:
    #         current_node = source_node.children[current_node_name]['node']
    #         result[current_node_name] = source_node.children[current_node_name]['distance']
    #         current_node_distance = result[current_node_name]
    #         current_node_children = current_node.children
    #         for child in current_node_children:
    #             if child in result:
    #                 if result[child] > current_node_distance + current_node_children[child]['distance']:
    #                     result[child] = current_node_distance + current_node_children[child]['distance']
    #             else:
    #                 result[child] = current_node_distance + current_node_children[child]['distance']

    print(result)

find_shortest_path()