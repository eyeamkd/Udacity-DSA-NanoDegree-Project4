from calendar import c
import math
from operator import ne
from queue import PriorityQueue

# testing data

test_map_intersections = {
    0: [0.7798606835438107, 0.6922727646627362],
    1: [0.7647837074641568, 0.3252670836724646],
    2: [0.7155217893995438, 0.20026498027300055],
    3: [0.7076566826610747, 0.3278339270610988],
    4: [0.8325506249953353, 0.02310946309985762],
    5: [0.49016747075266875, 0.5464878695400415],
    6: [0.8820353070895344, 0.6791919587749445],
    7: [0.46247219371675075, 0.6258061621642713],
    8: [0.11622158839385677, 0.11236327488812581],
    9: [0.1285377678230034, 0.3285840695698353]
}

test_map_roads = [
    [7, 6, 5],
    [4, 3, 2],
    [4, 3, 1],
    [5, 4, 1, 2],
    [1, 2, 3],
    [7, 0, 3],
    [0],
    [0, 5],
    [9],
    [8]
]



    
class A_Star_Search:  
    
    def __init__(self, M, start, goal) -> None: 
        self.intersections = M['intersections'] 
        self.roads = M['roads']  
        self.start_node = self.intersections[start]  
        self.end_node = self.intersections[goal] 
        self.f_scores = {start: 0}  
        self.start = start
        self.end = goal 
        self.path_trace = {} #used to generate the path 
        self.queue = PriorityQueue() 
        self.visited = set()
        pass 
    
    def calculate_h_score(self, node):
        return  self.calculate_euclidean_distance(node, self.end_node)  

    def calculate_g_score(self, current_node, neighbor_node): 
        return self.calculate_euclidean_distance(current_node, neighbor_node)  
    
    def get_node(self, value):
        return self.intersections[value] 

    def get_children(self, value):
        return self.roads[value]
    
    def calculate_f_score(self, current_node, neighbor_node):
        g_score = self.calculate_g_score(current_node, neighbor_node)
        h_score = self.calculate_h_score(current_node)  
        f_score = g_score + h_score 
        return f_score
        
    
    def update_f_scores(self, f_score, node_name):
        if node_name in self.f_scores:
            if self.f_scores[node_name] > f_score:
                self.f_scores[node_name] = f_score   
        else:
            self.f_scores[node_name] = f_score  
    
    def get_path_trace(self, trail_node):
        trace = [trail_node]
        current = trail_node 
        while current != self.start:
            current = self.path_trace[current] 
            trace.append(current) 
        return trace
                 
    
    def calculate_euclidean_distance(self, node1, node2):
        node1_x = node1[0]
        node1_y = node1[1]
        node2_x = node2[0]
        node2_y = node2[1]

        x_distance = (node1_x - node2_x) * (node1_x - node2_x)
        y_distance = (node1_y - node2_y) * (node1_y - node2_y)

        return math.sqrt(x_distance + y_distance); 

    def run_search(self):  
        current_node = self.start_node
        initial_f_score = self.calculate_f_score(current_node, current_node) 
        self.update_f_scores(initial_f_score, self.start) 
        self.queue.put((self.f_scores[self.start], self.start))
        
        while self.queue.not_empty:
            item = self.queue.get()  
            if item[1] == self.end:
                self.get_path_trace(item[1])
                break 
            if item[1] not in self.visited:
                self.visited.add(item[1])
                current_node = self.get_node(item[1]) 
                children = self.get_children(item[1]) 
                
                for child in children: 
                    neighbor_node = self.get_node(child)
                    f_score = self.calculate_f_score(current_node, neighbor_node)
                    self.update_f_scores(f_score,child)   
                    if self.f_scores[child] ==  f_score:
                        self.path_trace[item[1]]=child
                    self.queue.put((self.f_scores[child], child))
        
                
M = { 'intersections': test_map_intersections, 'roads': test_map_roads }            
        
a_star_search = A_Star_Search(M,7,4 ) 
print(a_star_search.run_search())
    



# def shortest_path(self, M, start, goal):
#         node_map = M
#         start_node = test_map_intersections[start]
#         goal_node = test_map_intersections[goal]
#         path_queue = PriorityQueue()
#         node_collection = []
#         visited = set()
#         resultant_path = []

       

        
#         path_queue.put((initial_node.heuristic_cost, start))

#         while path_queue.not_empty:
#             item = path_queue.get()
#             resultant_path.append(item[1])
#             visited.add(item[1])
#             if item[1] == goal:
#                 break
#             else:
#                 children = test_map_roads[item[1]]
#                 for child in children:
#                     if child not in visited:
#                         child_path_cost = self.get_distance(test_map_intersections[start], test_map_intersections[child])
#                         heuristic = self.get_distance(test_map_intersections[goal], test_map_intersections[child])
#                         final_distance = child_path_cost + heuristic
#                         path_queue.put((final_distance, child))

#         print(resultant_path)

#         print("shortest path called")
#         return resultant_path



