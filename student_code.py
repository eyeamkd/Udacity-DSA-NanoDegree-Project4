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

test_map_intersections_2={0: [0.7801603911549438, 0.49474860768712914], 1: [0.5249831588690298, 0.14953665513987202], 2: [0.8085335344099086, 0.7696330846542071], 3: [0.2599134798656856, 0.14485659826020547], 4: [0.7353838928272886, 0.8089961609345658], 5: [0.09088671576431506, 0.7222846879290787], 6: [0.313999018186756, 0.01876171413125327], 7: [0.6824813442515916, 0.8016111783687677], 8: [0.20128789391122526, 0.43196344222361227], 9: [0.8551947714242674, 0.9011339078096633], 10: [0.7581736589784409, 0.24026772497187532], 11: [0.25311953895059136, 0.10321622277398101], 12: [0.4813859169876731, 0.5006237737207431], 13: [0.9112422509614865, 0.1839028760606296], 14: [0.04580558670435442, 0.5886703168399895], 15: [0.4582523173083307, 0.1735506267461867], 16: [0.12939557977525573, 0.690016328140396], 17: [0.607698913404794, 0.362322730884702], 18: [0.719569201584275, 0.13985272363426526], 19: [0.8860336256842246, 0.891868301175821], 20: [0.4238357358399233, 0.026771817842421997], 21: [0.8252497121120052, 0.9532681441921305], 22: [0.47415009287034726, 0.7353428557575755], 23: [0.26253385360950576, 0.9768234503830939], 24: [0.9363713903322148, 0.13022993020357043], 25: [0.6243437191127235, 0.21665962402659544], 26: [0.5572917679006295, 0.2083567880838434], 27: [0.7482655725962591, 0.12631654071213483], 28: [0.6435799740880603, 0.5488515965193208], 29: [0.34509802713919313, 0.8800306496459869], 30: [0.021423673670808885, 0.4666482714834408], 31: [0.640952694324525, 0.3232711412508066], 32: [0.17440205342790494, 0.9528527425842739], 33: [0.1332965908314021, 0.3996510641743197], 34: [0.583993110207876, 0.42704536740474663], 35: [0.3073865727705063, 0.09186645974288632], 36: [0.740625863119245, 0.68128520136847], 37: [0.3345284735051981, 0.6569436279895382], 38: [0.17972981733780147, 0.999395685828547], 39: [0.6315322816286787, 0.7311657634689946]}

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

test_map_roads2 =[[36, 34, 31, 28, 17], [35, 31, 27, 26, 25, 20, 18, 17, 15, 6], [39, 36, 21, 19, 9, 7, 4], [35, 20, 15, 11, 6], [39, 36, 21, 19, 9, 7, 2], [32, 16, 14], [35, 20, 15, 11, 1, 3], [39, 36, 22, 21, 19, 9, 2, 4], [33, 30, 14], [36, 21, 19, 2, 4, 7], [31, 27, 26, 25, 24, 18, 17, 13], [35, 20, 15, 3, 6], [37, 34, 31, 28, 22, 17], [27, 24, 18, 10], [33, 30, 16, 5, 8], [35, 31, 26, 25, 20, 17, 1, 3, 6, 11], [37, 30, 5, 14], [34, 31, 28, 26, 25, 18, 0, 1, 10, 12, 15], [31, 27, 26, 25, 24, 1, 10, 13, 17], [21, 2, 4, 7, 9], [35, 26, 1, 3, 6, 11, 15], [2, 4, 7, 9, 19], [39, 37, 29, 7, 12], [38, 32, 29], [27, 10, 13, 18], [34, 31, 27, 26, 1, 10, 15, 17, 18], [34, 31, 27, 1, 10, 15, 17, 18, 20, 25], [31, 1, 10, 13, 18, 24, 25, 26], [39, 36, 34, 31, 0, 12, 17], [38, 37, 32, 22, 23], [33, 8, 14, 16], [34, 0, 1, 10, 12, 15, 17, 18, 25, 26, 27, 28], [38, 5, 23, 29], [8, 14, 30], [0, 12, 17, 25, 26, 28, 31], [1, 3, 6, 11, 15, 20], [39, 0, 2, 4, 7, 9, 28], [12, 16, 22, 29], [23, 29, 32], [2, 4, 7, 22, 28, 36]]

    
class A_Star_Search:  
    
    def __init__(self, M, start, goal) -> None: 
        self.intersections = M.intersections
        self.roads = M.roads
        self.start_node = self.intersections[start]  
        self.end_node = self.intersections[goal] 
        self.f_scores = {start: 0}  
        self.start = start
        self.end = goal  
        self.g_scores =  {start:0}
        self.path_trace = {} #used to generate the path 
        self.queue = PriorityQueue() 
        self.visited = set()
        pass 
    
    def calculate_h_score(self, node):
        return  self.calculate_euclidean_distance(node, self.end_node)  

    def calculate_g_score(self, current_node_name, neighbor_node_name):  
        current_node = self.get_node(current_node_name)
        neighbor_node = self.get_node(neighbor_node_name)
        distance =  self.calculate_euclidean_distance(current_node, neighbor_node)    
        tentative_g_score = distance + self.g_scores[current_node_name]
        if neighbor_node_name in self.g_scores.keys(): 
            if self.g_scores[neighbor_node_name] > tentative_g_score :
                self.g_scores[neighbor_node_name] = tentative_g_score  
        else:
            self.g_scores[neighbor_node_name] = tentative_g_score 
            
        return self.g_scores[neighbor_node_name]
                
                
    
    def get_node(self, value):
        return self.intersections[value] 

    def get_children(self, value):
        return self.roads[value]
    
    def calculate_f_score(self, current_node_name, neighbor_node_name):  
        current_node = self.get_node(current_node_name)
        neighbor_node = self.get_node(neighbor_node_name)
        g_score = self.calculate_g_score(current_node_name, neighbor_node_name)
        h_score = self.calculate_h_score(current_node)  
        f_score = g_score + h_score  
        if neighbor_node_name in self.f_scores.keys():
            if f_score < self.f_scores[neighbor_node_name]:
                self.f_scores[neighbor_node_name] = f_score 
        else:
            self.f_scores[neighbor_node_name] = f_score 
        return self.f_scores[neighbor_node_name]
        
    
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
        trace.reverse()
        return trace
                 
    # I have used Euclidean distance here but this can also be solved using 
    # Manhattan distance heuristic which in this case would be abs(x1 - y1) + abs(x2 - y2) 
    # since heuristic is just a abstract relative measurement it doesn't need to be something accurate 
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
        initial_f_score = self.calculate_f_score(self.start, self.start) 
        self.update_f_scores(initial_f_score, self.start) 
        self.queue.put((self.f_scores[self.start], self.start))
        
        while self.queue.not_empty:
            item = self.queue.get()  
            if item[1] == self.end:
                return self.get_path_trace(item[1]) 
                 
            if item[1] not in self.visited:
                self.visited.add(item[1])
                current_node = self.get_node(item[1]) 
                children = self.get_children(item[1]) 
                
                for child in children: 
                    neighbor_node = self.get_node(child)
                    f_score = self.calculate_f_score(item[1], child)
                    self.update_f_scores(f_score,child) 
                    if child in self.path_trace.keys():
                        if self.path_trace[child] == f_score:
                            self.path_trace[child] = item[1]  
                    else:    
                        self.path_trace[child] = item[1]   
                    self.queue.put((self.f_scores[child], child))


# testing         
                
M = { 'intersections': test_map_intersections, 'roads': test_map_roads }   

M2 =  {'intersections': test_map_intersections_2, 'roads': test_map_roads2}          
        
a_star_search = A_Star_Search(M,7,4 )  
a_star_search2 = A_Star_Search(M2, 5, 34)
print(a_star_search.run_search()) 
print(a_star_search2.run_search())

    



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



