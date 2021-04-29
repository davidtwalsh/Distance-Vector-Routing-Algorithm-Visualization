import pygame as pg
from drawText import draw_text
from drawText import draw_textLeftToRight
from distanceTableGUI import distanceTableGUIObject

from node0 import Node0
from node1 import Node1
from node2 import Node2
from node3 import Node3
import time

def getMidpoint(x1,y1,x2,y2):
  return (int((x1+x2)/2),int((y1+y2)/2))

def tolayer2(rtpkt):
  #unpack the packet
  sourceID = rtpkt.sourceID
  destID = rtpkt.destID
  minCost = rtpkt.minCost

  #call the appropriate rtupdate function
  if destID == 0:
    node0.rtupdate0(rtpkt)
  elif destID == 1:
    node1.rtupdate1(rtpkt)
  elif destID == 2:
    node2.rtupdate2(rtpkt)
  elif destID == 3:
    node3.rtupdate3(rtpkt)


pg.init()
WIDTH = 1200
HEIGHT = 700
screen = pg.display.set_mode((WIDTH,HEIGHT))
pg.display.set_caption("Distance Vector Routing Algorithm Visualization")

#fonts and colors
fontNormal = pg.font.SysFont('Arial',32)
fontSmall = pg.font.SysFont('Arial',24)
colorBG = (235,224,216)
colorBlack = (0,0,0)
colorButton = (140,135,135)
colorWhite = (255,255,255)
colorBlue = (45,93,204)

isProgramRunning = True
clock = pg.time.Clock()
fps = 30

#create nodes
node0 = Node0()
node1 = Node1()
node2 = Node2()
node3 = Node3()

#set up node neighbors
node0.addNeighbors(node1,node2,node3)
node1.addNeighbors(node0,node2)
node2.addNeighbors(node0,node1,node3)
node3.addNeighbors(node0,node2)

#init the nodes
node0.rtinit0()
node1.rtinit1()
node2.rtinit2()
node3.rtinit3()

#init distanceTableGUIObjects
distanceTableNode0 = distanceTableGUIObject(screen,80,80,0,node0)
distanceTableNode3 = distanceTableGUIObject(screen,80,400,3,node3)
distanceTableNode1 = distanceTableGUIObject(screen,930,80,1,node1)
distanceTableNode2 = distanceTableGUIObject(screen,930,400,2,node2)

distanceTableNode0.setTable()
distanceTableNode3.setTable()
distanceTableNode1.setTable()
distanceTableNode2.setTable()

mx = 0
my = 0
click = False #for keeping track of mouse clicks
isAlgorithmDone = False
highlightedConnection = ""
messageReceiverID = None
while isProgramRunning:

  mx,my = pg.mouse.get_pos()

  for event in pg.event.get():
    if event.type == pg.QUIT:
      isProgramRunning = False
      break
    if event.type == pg.MOUSEBUTTONDOWN:
      if event.button == 1:
        click = True

  #UPDATE BEGIN----------------------------
  advanceButton = pg.Rect(500,25,200,50)

  if advanceButton.collidepoint((mx,my)) and isAlgorithmDone == False:
    if click:
        distanceTableNode0.resetChangeMatrix()
        distanceTableNode3.resetChangeMatrix()
        distanceTableNode1.resetChangeMatrix()
        distanceTableNode2.resetChangeMatrix()
        gotPacket = False
        packet = None
        if len(node0.myPacketsToSend) != 0:
            packet = node0.myPacketsToSend.pop(0)
            tolayer2(packet)
            gotPacket = True

        elif len(node1.myPacketsToSend) != 0:
            packet = node1.myPacketsToSend.pop(0)
            tolayer2(packet)
            gotPacket = True

        elif len(node2.myPacketsToSend) != 0:
            packet = node2.myPacketsToSend.pop(0)
            tolayer2(packet)
            gotPacket = True

        elif len(node3.myPacketsToSend) != 0:
            packet = node3.myPacketsToSend.pop(0)
            tolayer2(packet)
            gotPacket = True
        else:
          isAlgorithmDone = True
        if gotPacket == True:
          srcID = packet.sourceID
          destID = packet.destID
          # print("SRC ID: " + str(srcID) + " DEST ID: " + str(destID))
          #cnxs: 0->1 0->3 0->2 1->2 3->2
          if srcID == 0 and destID == 1 or srcID == 1 and destID == 0:
            highlightedConnection = "0->1"
          elif srcID == 0 and destID == 3 or srcID == 3 and destID == 0:
            highlightedConnection = "0->3"
          elif srcID == 0 and destID == 2 or srcID == 2 and destID == 0:
            highlightedConnection = "0->2"
          elif srcID == 1 and destID == 2 or srcID == 2 and destID == 1:
            highlightedConnection = "1->2"
          elif srcID == 3 and destID == 2 or srcID == 2 and destID == 3:
            highlightedConnection = "3->2"
          # messageSenderID = srcID
          messageReceiverID = destID


  distanceTableNode0.update()
  distanceTableNode3.update()
  distanceTableNode2.update()
  distanceTableNode1.update()

  #DRAW BEGIN------------------------------
  screen.fill(colorBG)

  if isAlgorithmDone == False:
    pg.draw.rect(screen,colorButton,advanceButton)
    draw_textLeftToRight("Advance",fontNormal,colorWhite,screen,550,30)
  else:
    draw_textLeftToRight("Algorithm Complete",fontNormal,colorBlack,screen,475,30)

  #draw the graph
  xOffset = 200
  yOffset = 100
  nodeRadius = 30
  nodeThickness = 5

  #first draw nodes
  #node 0
  topLeftCircleX = int(WIDTH/2 - xOffset)
  topLeftCircleY = int(HEIGHT/2 - yOffset)
  if messageReceiverID != 0:
    pg.draw.circle(screen,colorBlack,(topLeftCircleX,topLeftCircleY),nodeRadius,nodeThickness)
  else:
    pg.draw.circle(screen,colorBlue,(topLeftCircleX,topLeftCircleY),nodeRadius,nodeThickness)

  #node 3
  bottomLeftCircleX = int(WIDTH/2 - xOffset)
  bottomLeftCircleY = int(HEIGHT/2 + yOffset)
  if messageReceiverID != 3:
    pg.draw.circle(screen,colorBlack,(bottomLeftCircleX,bottomLeftCircleY),nodeRadius,nodeThickness)
  else:
    pg.draw.circle(screen,colorBlue,(bottomLeftCircleX,bottomLeftCircleY),nodeRadius,nodeThickness)

  #node 2
  bottomRightCircleX = int(WIDTH/2 + xOffset)
  bottomRightCircleY = int(HEIGHT/2 + yOffset)
  if messageReceiverID != 2:
    pg.draw.circle(screen,colorBlack,(bottomRightCircleX,bottomRightCircleY),nodeRadius,nodeThickness)
  else:
    pg.draw.circle(screen,colorBlue,(bottomRightCircleX,bottomRightCircleY),nodeRadius,nodeThickness)

  #node 1
  topRightCircleX = int(WIDTH/2 + xOffset)
  topRightCircleY = int(HEIGHT/2 - yOffset)
  if messageReceiverID != 1:
    pg.draw.circle(screen,colorBlack,(topRightCircleX,topRightCircleY),nodeRadius,nodeThickness)
  else:
    pg.draw.circle(screen,colorBlue,(topRightCircleX,topRightCircleY),nodeRadius,nodeThickness)

  #now draw node connections
  connectionThickness = 5
  connectionOffset = nodeRadius
  #node 0-> 1
  connectionColor = colorBlack
  if highlightedConnection == "0->1":
    connectionColor = colorBlue
  else:
    connectionColor = colorBlack
  pg.draw.line(screen,connectionColor,[topLeftCircleX + connectionOffset,topLeftCircleY],[topRightCircleX-connectionOffset,topRightCircleY],connectionThickness)
  #node 0->3
  if highlightedConnection == "0->3":
    connectionColor = colorBlue
  else:
    connectionColor = colorBlack
  pg.draw.line(screen,connectionColor,[topLeftCircleX,topLeftCircleY+connectionOffset],[bottomLeftCircleX,bottomLeftCircleY - connectionOffset],connectionThickness)
  #node 0->2
  if highlightedConnection == "0->2":
    connectionColor = colorBlue
  else:
    connectionColor = colorBlack
  pg.draw.line(screen,connectionColor,[topLeftCircleX+int(connectionOffset/2)+5,topLeftCircleY+int(connectionOffset/2)],[bottomRightCircleX - int(connectionOffset/2)-5,bottomRightCircleY - int(connectionOffset/2)],connectionThickness)
  #node 1->2
  if highlightedConnection == "1->2":
    connectionColor = colorBlue
  else:
    connectionColor = colorBlack
  pg.draw.line(screen,connectionColor,[topRightCircleX,topRightCircleY+connectionOffset],[bottomRightCircleX,bottomRightCircleY - connectionOffset],connectionThickness)
  #node 3->2
  if highlightedConnection == "3->2":
    connectionColor = colorBlue
  else:
    connectionColor = colorBlack
  pg.draw.line(screen,connectionColor,[bottomLeftCircleX + connectionOffset,bottomLeftCircleY],[bottomRightCircleX-connectionOffset,bottomRightCircleY],connectionThickness)

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

  draw_textLeftToRight("The receiving node is highlighted in ",fontSmall,colorBlack,screen,420,500)
  draw_textLeftToRight("BLUE",fontSmall,colorBlue,screen,730,500)

  #DONE DRAWING BASIC VISUAL
  #now draw distanceTableGUIObjects
  distanceTableNode0.draw()
  distanceTableNode3.draw()
  distanceTableNode2.draw()
  distanceTableNode1.draw()



  #end
  click = False
  pg.display.flip()
  clock.tick(fps)

pg.quit()
