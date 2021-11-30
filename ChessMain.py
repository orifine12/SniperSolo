#this is youre main driver file - user input

import pygame as p
from ChessEngineTry import GameState


WIDTH = HEIGHT = 512 #res
DIMENSIONS = 8 #8x8
MAX_FPS = 15 #animations
SQ_SIZE = HEIGHT // DIMENSIONS
IMAGES = {}

def loadImages():
    pieces = ['WP', 'WR', 'WN', 'Wb','WK','WQ', 'BP', 'BR', 'BN', 'Bb','BK','BQ']
    for piece in pieces:
      IMAGES[piece] = p.transform.scale(p.image.load("Images/"+ piece + ".png"),(SQ_SIZE, SQ_SIZE))
    # we can access pictures by wrtiting IMAGES['WP']
   
   # CODE FOR handling user input and graphics

def maine():
    p.init()
    screen = p.display.set_mode((WIDTH, HEIGHT))
    clock = p.time.Clock()
    white = (255, 255, 255)
    screen.fill(white)
    gs = GameState()
    #loadImages()
    running = True
    while running:
       for e in p.event.get():
         if e.type == p.QUIT:
           running == False
    drawGameState(screen,gs)
    clock.tick(MAX_FPS)
    p.display.update()



def drawGameState(screen, gs):
  drawBoard(screen) #draw squares on the board
  drawPieces(screen, gs.board) #draw pieces on the squares


def drawBoard(screen):
 colors = [p.color("white"), p.color("green")]
 for r in range [DIMENSIONS]:
    for c in range [DIMENSIONS]:
       color = colors[((r+c)%2)]
       p.draw.rect (screen, color, p.Rect(c*SQ_SIZE, r*SQ_SIZE, SQ_SIZE, SQ_SIZE))


def drawPieces(screen, board):
    pass

maine()
