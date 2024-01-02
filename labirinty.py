import pygame as pg
import math
import random
UP = 0
RIGTH = 1
DOWN = 2
LEFT = 3
DEAD= 5
class Player:
    def __init__(self,position,size,color):
        self.position = position
        self.size = size
        self.color = color
        self.info = []

class Labirynth:
    def __init__(self,screen,lab,start,end):
        #players
        self.players = []
        #labyrinth characteristics
        self.len_lab = len(lab)
        self.start = start
        self.end = end
        self.lab = lab
        #screen characteristics
        self.width_screen, self.height_screen = screen.get_size()
        self.screen = screen
        #blocks lengths
        self.width_rect, self.height_rect = self.width_screen//self.len_lab , self.height_screen//self.len_lab

    def draw_labyrinth(self):
        self.screen.fill('black')
        for i in range(self.len_lab):
            for j in range(self.len_lab):
                pg.draw.rect(self.screen,"white",pg.Rect(self.width_rect*j,self.height_rect*i,self.width_rect*self.lab[i][j],self.height_rect*self.lab[i][j]),0)
        i,j = self.end
        pg.draw.rect(self.screen,"green",pg.Rect(self.width_rect*j,self.height_rect*i,self.width_rect*self.lab[i][j],self.height_rect*self.lab[i][j]),0)

    def start_new_player(self):
        player_initial_position = self.to_cordinated(self.start)
        player_size = (self.width_rect,self.height_rect)
        player_color = (0,255,0)
        self.players.append(Player(player_initial_position,player_size,player_color))

    def move_player(self,n,direction):
        current_position = self.players[n].position
        new_position = self.new_position(current_position,direction)
        is_free = self.free(new_position)
        if is_free:
            self.players[n].position = new_position
        info = {"is_move_valid":is_free,"current_position":self.players[n].position,"end_game": self.end_game(self.players[n].position)}
        self.players[n].info.append({"is_move_valid":is_free,"current_position":self.players[n].position,"end_game": self.end_game(self.players[n].position)})
        return info
    
    def draw_player(self,n):
        pg.draw.rect(self.screen,
                    self.players[n].color,
                    pg.Rect(self.players[n].position,self.players[n].size),
                    0
                    )
    def to_index(self,position):
        x,y = position
        return(y//self.height_rect,x//self.width_rect)
    def to_cordinated(self,position):
        i, j = position
        return (self.width_rect*j,self.height_rect*i)
    def new_position(self,position,direction):
        x,y = position
        if direction == UP:
            y -= self.height_rect
        elif direction == RIGTH:
            x += self.width_rect
        elif direction == DOWN:
            y += self.height_rect
        elif direction == LEFT:
            x -= self.width_rect
        return (x,y)

    def free(self,position):
        valid = self.is_free_index(self.to_index(position))
        return valid
    
    def is_free_index(self,position):
        i, j = position
        between = lambda x,y,z: (y >= x and y < z)
        return True if (between(0,i,self.len_lab) and between(0,j,self.len_lab) and self.lab[i][j] == 1) else False
    
    def end_game(self,position):
        i,j = self.to_index(position)
        is_end_game = True if (i,j) == self.end else False
        return is_end_game
    
    def move_index(self,position,direction):
        i, j = position
        if direction == UP:
            i -= 1
        elif direction == RIGTH:
            j += 1
        elif direction == DOWN:
            i += 1
        elif direction == LEFT:
            j -= 1
        return (i,j)
    
    def free_directions(self,position):
        free= []
        i, j = position
        if self.is_free_index((i,j+1)): free.append(RIGTH)
        if self.is_free_index((i,j-1)): free.append(LEFT)
        if self.is_free_index((i+1,j)): free.append(DOWN)
        if self.is_free_index((i-1,j)): free.append(UP)
        return free
    
    def reverse(self,direction):
        if direction == UP:
            return DOWN
        elif direction == RIGTH:
            return LEFT
        elif direction == DOWN:
            return UP
        elif direction == LEFT:
            return RIGTH
    def clear_players(self):
        self.players.clear()


def create_labyrinth(N,start,end):
    NotImplemented

