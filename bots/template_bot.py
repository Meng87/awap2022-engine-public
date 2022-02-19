import sys

import random

from src.player import *
from src.structure import *
from src.game_constants import GameConstants as GC

class MyPlayer(Player):

    def __init__(self):
        print("Init")
        self.turn = 0
        return


    def play_turn(self, turn_num, map, player_info):
        self.set_bid(0)
        # self.build(struct_type, x, y)
        # find generator
        G = []
        for i in range(len(map)):
            for j in range(len(map[0])):
                tile = map[i][j]
                st = tile.structure
                if st.team == player_info.team and st.type == StructureType.GENERATOR:
                    G.append(st.x,st.y)
        dists = []
        for g in G:
            g_x, g_y = g
            dists.append(self.dijkstra(map, g_x, g_y))
        # given (tile to get to)
        dest_x, dest_y = len(map[0]) - 1, len(map) - 1
        
        return
    
    # find min distance vertex in the graph
    def minDistance(self, map, dist, sptSet):
        # Initialize minimum distance for next node
        min = sys.maxint
 
        # Search not nearest vertex not in the
        # shortest path tree
        for i in range(len(map)):
            for j in range(len(map[0])): # check all nodes in graph
                if dist[i][j] < min and sptSet[i][j] == False:
                    min = dist[i][j]
                    min_index = (j,i)
        return min_index
    
    # returns a list of nbors
    def getnbors(self, x, y, width, height):
        result = []
        for item in [(x-1,y),(x+1,y),(x,y+1),(x,y-1)]:
            (x1,y1) = item
            if (0 <= x1 && x1 < width && 0 <= y1 && y1 < height):
                result.append((x1,y1))
        return result

    # Function that implements Dijkstra's single source
    # shortest path algorithm for a graph represented
    # using adjacency matrix representation
    # nodes are stored as an int between 0 and total - 1
    def dijkstra(self, map, src_x, src_y):
        rows, cols = len(map), len(map[0])
        total = rows * cols
        dist = [[sys.maxint] * cols] * rows # all distances start out as sys.maxint
        dist[src_x][src_y] = 0 # except dist source
        sptSet = [[False] * cols] * rows # nothing is in the sptset

        for cout in range(total):
 
            # Pick the minimum distance vertex from
            # the set of vertices not yet processed.
            # x is always equal to src in first iteration
            (j, i) = self.minDistance(map, dist, sptSet)
 
            # Put the minimum distance vertex in the
            # shortest path tree
            sptSet[i][j] = True
 
            # Update dist value of the adjacent vertices
            # of the picked vertex only if the current
            # distance is greater than new distance and
            # the vertex in not in the shortest path tree
            nbors = self.getnbors(j, i, cols, rows)
            for y in nbors:
                (a, b) = y
                nbor_tile = map[b][a]
                weight = nbor_tile.passability
                if (spSet[b][a] == False and dist[b][a] > dist[i][j] + weight):
                    dist[b][a] = dist[i][j] + weight
            return dist

    
    def BFS(self, map, tile):
        rows, cols = len(map), len(map[0])
        visited = [False] * rows * cols
        queue = []
 
        # Mark the source node as
        # visited and enqueue it
        queue.append(tile)
        visited[tile] = True
 
        while queue:
            # Dequeue a vertex from queue
            t = queue.pop(0)

            # Get all adjacent vertices of the
            # dequeued vertex v. If a adjacent
            # has not been visited, then mark it
            # visited and enqueue it
            nbors = self.getnbors(t, rows, cols)
            for coord in nbors:
                (x, y) = coord
                if visited[y * cols + x] == False:
                    queue.append(coord)
                    visited[y * cols + x] = True
