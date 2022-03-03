class A_star:
    def _init(self, map, start, goal, debug) -> None:

        # dict: {0:(x,y), 1:(x,y)...,n-1:(x,y)}
        self.states_dict = map.intersections
        # list: [[neigbors node 0], [neigbors node 1]...,[neigbors node n-1]]
        self.neighbors_list = map.roads
        self.start = start
        self.goal = goal
        self.fscore_dict = {}  # {node_ind: fscore}
        self.gscore_dict = {start: 0}  # {node_ind: gscore}
        self.openSet = set(self.get_neighbors(start))
        self.visitedNodes = set([start])
        self.camefrom = {}  # {current_node_ind: came_from_node_id}
        [self.update_fScores(start, neighbor) for neighbor in self.get_neighbors(start)]
        self.debug = debug

    def get_neighbors(self, node_id):
        """ 
            @inputs:
                node_id: index of node we want to get its neighbors from
            @output:
                list of node indexes that are neighbors
        """
        return self.neighbors_list[node_id]

    def euclidean_distance(self, node_1, node_2):
        """ 
            Calculates the euclidean distance between node_1 and node_2
        """
        x1, y1 = node_1
        x2, y2 = node_2
        return ((x1-x2)**2+(y1-y2)**2)**(1/2)

    def calculate_heuristicScore(self, node_id):
        """ 
            Calculates the heuristic for node_id
        """
        node_1 = self.states_dict[node_id]
        node_2 = self.states_dict[self.goal]
        return self.euclidean_distance(node_1, node_2)

    def calculate_gScore(self, curr_node, neighbor_node):
        """
            Calculates the gScore between the curr_node and neighbor node
        """
        state_curr_node = self.states_dict[curr_node]
        state_neighbor_node = self.states_dict[neighbor_node]
        neighbor_gscore = self.euclidean_distance(state_curr_node, state_neighbor_node) + self.gscore_dict[curr_node]
        if self.gscore_dict.get(neighbor_node) is not None:
            if neighbor_gscore < self.gscore_dict[neighbor_node]:
                self.gscore_dict[neighbor_node] = neighbor_gscore
        else:
            self.gscore_dict[neighbor_node] = neighbor_gscore
        return self.gscore_dict[neighbor_node]

    def update_fScores(self, curr_node, neighbor_node):
        """
            updates fscore_dict with the f scores of the neighbors 
        """
        h = self.calculate_heuristicScore(neighbor_node)
        g = self.calculate_gScore(curr_node, neighbor_node)
        f = g+h
        previous_f = self.fscore_dict.get(neighbor_node)
        if previous_f is not None:
            if previous_f > f:
                self.fscore_dict[neighbor_node] = f
                self.record_node(neighbor_node, curr_node)
        else:
            self.fscore_dict[neighbor_node] = f
            self.record_node(neighbor_node, curr_node)

    def get_node(self):
        return min(self.fscore_dict, key=self.fscore_dict.get)

    def generate_path(self, id_node):
        """
            Reconstructs path from start to the id_node
        """
        curr_node = id_node
        path = [curr_node]
        while curr_node != self.start:
            curr_node = self.camefrom[curr_node]
            path.append(curr_node)
        return path[::-1]

    def record_node(self, curr_node, camefrom_node):
        self.camefrom[curr_node] = camefrom_node

    def run(self):
        while len(self.openSet) != 0:
            curr_node = self.get_node()
            if self.debug:
                print(f'curr_node: {curr_node}, f_scores: {self.fscore_dict}, \n g_scores: {self.gscore_dict} \
                    \n openset: {self.openSet}, visited nodes: {self.visitedNodes}, came_from: {self.camefrom} \n')
            if curr_node == self.goal:
                return self.generate_path(curr_node)
            else:
                self.openSet.remove(curr_node)
                self.visitedNodes.add(curr_node)
                del self.fscore_dict[curr_node]

            for neighbor in self.get_neighbors(curr_node):
                # Ingore neighbor already visited
                if neighbor in self.visitedNodes:
                    continue
                # New node discovered
                if not neighbor in self.openSet:
                    self.openSet.add(neighbor)

                self.update_fScores(curr_node, neighbor)

        print("no path found")
        return 
    
    
def shortest_path(M,start,goal, debug=False):
        if start == goal:
            return [start]
        a_star = A_star(M, start, goal, debug)
        return a_star.run()