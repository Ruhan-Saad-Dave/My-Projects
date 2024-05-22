"""
A trial project for a game
"""

import numpy as np
import pandas as pd

class World():
    def __init__(self):
        '''
        Generates a world of 4 x 4 x 4 spaces with 16 wood, 14 sand, 12 stone, 10 obsidian, 12 emerald
        '''
        wood = np.array(["wood"] * 16)
        sand = np.array(["sand"] * 14)
        stone = np.array(["stone"] * 12)
        obsidian = np.array(["obsidian"] * 10)
        emerald = np.array(["emerald"] * 12)
        blocks = np.concatenate((wood, sand, stone, obsidian, emerald))
        self.world = np.random.permutation(blocks).reshape(4, 4, -1)
        #print(self.world)

    def dig(self, player, x, y, z):
        '''
        Removes a block from a specified coordinate and add it into the player's bag. And the removed block is replaced with air.
        '''
        block = self.world[x, y, z]
        player.add_block(block)
        self.world[x, y, z] = "air"
        #print(self.world)
    
    def show_top(self):
        '''
        Shows the world box from the top.
        '''
        print(self.world[:, :, 0])

class Player():
    def __init__(self, color):
        '''
        Creating a player of specified color 
        '''
        self.color = color
        self.bag_blocks = pd.Series({"wood": 0, "sand": 0, "stone": 0, "obsidian": 0, "emerald":0})

    def add_block(self, block):
        '''
        Upon destorying a block from the world box, add it into the player's bag.
        '''
        self.bag_blocks[block] = self.bag_blocks[block] + 1
        print("Player:", self.color)
        print(self.bag_blocks)

game = World()
player1 = Player("blue")
game.show_top()
game.dig(player1, 0, 0, 0)
game.show_top()