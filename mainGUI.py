import pygame as pg
from drawText import draw_text
from drawText import draw_textLeftToRight
from maths import getMidpoint
from distanceTableGUI import distanceTableGUIObject

def getMidpoint(x1,y1,x2,y2):
  return (int((x1+x2)/2),int((y1+y2)/2))


pg.init()
WIDTH = 1200
HEIGHT = 700
screen = pg.display.set_mode((WIDTH,HEIGHT))
pg.display.set_caption("Distance Vector Routing Algorithm Visualization")

#fonts and colors
fontNormal = pg.font.SysFont('Arial',32)
colorBG = (235,224,216)
colorBlack = (0,0,0)

isProgramRunning = True
clock = pg.time.Clock()
fps = 30

#init distanceTableGUIObjects
distanceTableNode0 = distanceTableGUIObject(screen,80,80,0)
distanceTableNode3 = distanceTableGUIObject(screen,80,400,1)
distanceTableNode1 = distanceTableGUIObject(screen,930,80,1)
distanceTableNode2 = distanceTableGUIObject(screen,930,400,1)

while isProgramRunning:

  for event in pg.event.get():
    if event.type == pg.QUIT:
      isProgramRunning = False
      break

  #UPDATE BEGIN----------------------------
  distanceTableNode0.update()
  distanceTableNode3.update()
  distanceTableNode2.update()
  distanceTableNode1.update()

  #DRAW BEGIN------------------------------
  screen.fill(colorBG)

  #draw the graph
  xOffset = 200
  yOffset = 100
  nodeRadius = 30
  nodeThickness = 5

  #first draw nodes
  #node 0
  topLeftCircleX = int(WIDTH/2 - xOffset)
  topLeftCircleY = int(HEIGHT/2 - yOffset)
  pg.draw.circle(screen,colorBlack,(topLeftCircleX,topLeftCircleY),nodeRadius,nodeThickness)

  #node 3
  bottomLeftCircleX = int(WIDTH/2 - xOffset)
  bottomLeftCircleY = int(HEIGHT/2 + yOffset)
  pg.draw.circle(screen,colorBlack,(bottomLeftCircleX,bottomLeftCircleY),nodeRadius,nodeThickness)

  #node 2
  bottomRightCircleX = int(WIDTH/2 + xOffset)
  bottomRightCircleY = int(HEIGHT/2 + yOffset)
  pg.draw.circle(screen,colorBlack,(bottomRightCircleX,bottomRightCircleY),nodeRadius,nodeThickness)

  #node 1
  topRightCircleX = int(WIDTH/2 + xOffset)
  topRightCircleY = int(HEIGHT/2 - yOffset)
  pg.draw.circle(screen,colorBlack,(topRightCircleX,topRightCircleY),nodeRadius,nodeThickness)

  #now draw node connections
  connectionThickness = 5
  connectionOffset = nodeRadius
  #node 0-> 1
  pg.draw.line(screen,colorBlack,[topLeftCircleX + connectionOffset,topLeftCircleY],[topRightCircleX-connectionOffset,topRightCircleY],connectionThickness)
  #node 0->3
  pg.draw.line(screen,colorBlack,[topLeftCircleX,topLeftCircleY+connectionOffset],[bottomLeftCircleX,bottomLeftCircleY - connectionOffset],connectionThickness)
  #node 0->2
  pg.draw.line(screen,colorBlack,[topLeftCircleX+int(connectionOffset/2)+5,topLeftCircleY+int(connectionOffset/2)],[bottomRightCircleX - int(connectionOffset/2)-5,bottomRightCircleY - int(connectionOffset/2)],connectionThickness)
  #node 1->2
  pg.draw.line(screen,colorBlack,[topRightCircleX,topRightCircleY+connectionOffset],[bottomRightCircleX,bottomRightCircleY - connectionOffset],connectionThickness)
  #node 3->2
  pg.draw.line(screen,colorBlack,[bottomLeftCircleX + connectionOffset,bottomLeftCircleY],[bottomRightCircleX-connectionOffset,bottomRightCircleY],connectionThickness)

  #lastly draw node numbers and connection weights
  #node0
  draw_text("0",fontNormal,colorBlack,screen,topLeftCircleX,topLeftCircleY)
  #node1
  draw_text("1",fontNormal,colorBlack,screen,topRightCircleX,topRightCircleY)
  #node2
  draw_text("2",fontNormal,colorBlack,screen,bottomRightCircleX,bottomRightCircleY)
  #node3
  draw_text("3",fontNormal,colorBlack,screen,bottomLeftCircleX,bottomLeftCircleY)
  #0->1
  tempX,tempY = getMidpoint(topLeftCircleX + connectionOffset,topLeftCircleY,topRightCircleX-connectionOffset,topRightCircleY)
  draw_text("1",fontNormal,colorBlack,screen,tempX,tempY-18)
  #0->3
  tempX,tempY = getMidpoint(topLeftCircleX,topLeftCircleY+connectionOffset,bottomLeftCircleX,bottomLeftCircleY - connectionOffset)
  draw_text("7",fontNormal,colorBlack,screen,tempX+18,tempY)
  #0->2
  tempX,tempY = getMidpoint(topLeftCircleX+int(connectionOffset/2)+5,topLeftCircleY+int(connectionOffset/2),bottomRightCircleX - int(connectionOffset/2)-5, bottomRightCircleY - int(connectionOffset/2) )
  draw_text("3",fontNormal,colorBlack,screen,tempX+10,tempY-13)
  #1->2
  tempX,tempY = getMidpoint(topRightCircleX,topRightCircleY+connectionOffset,bottomRightCircleX,bottomRightCircleY - connectionOffset)
  draw_text("1",fontNormal,colorBlack,screen,tempX+18,tempY)
  #3->2
  tempX,tempY = getMidpoint(bottomLeftCircleX + connectionOffset,bottomLeftCircleY,bottomRightCircleX-connectionOffset,bottomRightCircleY)
  draw_text("2",fontNormal,colorBlack,screen,tempX,tempY+18)

  #DONE DRAWING BASIC VISUAL
  #now draw distanceTableGUIObjects
  distanceTableNode0.draw()
  distanceTableNode3.draw()
  distanceTableNode2.draw()
  distanceTableNode1.draw()



  #end
  pg.display.flip()
  clock.tick(fps)

pg.quit()
