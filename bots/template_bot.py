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
        #Coordinates of all spaces that have roads & towers on them
        myStructures = []
        possibleTiles = []
        #Determines whether it's players' turn or not
        if player_info.active == True and player_info.dq == False:
            if self.isValidRoad == True and self.isValidTower == False:
                #Need Coordinates
                #Let's Build the road!
                #Len road will depend on weight/distance between 
                # generator & currTile?
                build_type = StructureType.ROAD

                
            elif self.isValidTower == True and self.isValidRoad == False:
                #Need coordinates
                #Let's Build a tower
                buildType = StructureType.TOWER
                towerBaseCost = buildType.get_base_cost()
                #Passability comes from currPosition on the map
                passability = 1.0
                #Population comes from currPosition on the map
                population = 0.0
                buildTowerCost = towerBaseCost * passability
        return
    def isValidRoad(self, turn_num,map,player_info):
        buildType = StructureType.ROAD
        #Passability comes from currPosition on the map
        passability = 1.0
        #Will come from dfs alogrithim
        distance = 1
        #Base Cost of a road
        roadBaseCost = buildType.get_base_cost()
        buildRoadCost = roadBaseCost * passability
        if turn_num == 1: #Defintely building roads, but how long? 
            return True
        elif(turn_num > 1 and buildRoadCost <= player_info.money and 
                self.isValidTower == False):
            return True
        return False

    def isValidTower(self,turn_num,map,player_info): 
        buildType = StructureType.TOWER
        towerBaseCost = buildType.get_base_cost()
        #Passability comes from currPosition on the map
        passability = 1.0
        #Population comes from currPosition on the map
        population = 0.0
        buildTowerCost = towerBaseCost * passability
        #Can't build tower on first turn
        #Naive: Build a tower whenever we see a person
        if population >= 1.0 and buildTowerCost <= player_info.money:
            #figure out if tower can be buildt
            return True
        return False