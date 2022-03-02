import math
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

class Node:
    def __init__(self, node, goal_node, start_node, children):
        heuristic_cost = get_distance(goal_node, node)
        path_cost = get_distance(start_node, node)
        children = children
        pass


def get_distance(goal_node, node):
    goal_node_x = goal_node[0]
    goal_node_y = goal_node[1]
    node_x = node[0]
    node_y = node[1]

    x_distance = (goal_node_x - node_x) * (goal_node_x - node_x)
    y_distance = (goal_node_y - node_y) * (goal_node_y - node_y)

    return math.sqrt(x_distance + y_distance)


def shortest_path(M, start, goal):
    node_map = M
    start_node = start
    end_node = goal
    path_queue = PriorityQueue()

    nodes = node_map.intersections



    # calculate the heuristic distance
    # take the initial start node
    # expand each node, and for each node calculate the final path = cost_path + heuristic_path
    # arrange the nodes that are expanded according to the final path
    # keep expanding the final path until the result is reaached
    print("shortest path called")
    return