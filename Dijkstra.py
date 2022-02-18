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

    node_d.join(node_a, 2)
    node_d.join(node_c, 1)

    unvisited.add('B')
    unvisited.add('C')
    unvisited.add('D')
    unvisited.add('E')
    unvisited.add('F') 
    
    to_visit = set()

    source_node = node_a 
    
    to_visit.add(source_node) 
    
    while len(to_visit) > 0:
        current_node = to_visit.pop()
        for child in current_node.children:  
            if child not in result.keys():
                result[child] = current_node.children[child]['distance'] 
                to_visit.add(current_node.children[child]['node'])   
            else:
                if result[child] > current_node.children[child]['distance']:
                    result[child] = current_node.children[child]['distance'] 
         
             

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