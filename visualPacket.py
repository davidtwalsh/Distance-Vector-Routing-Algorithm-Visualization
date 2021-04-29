import pygame as pg
import math

COLORPACKET = (255,0,0)
colorRed = (255,0,0)
colorGreen = (0,255,0)
colorBlue = (0,0,255)
colorYellow = (255,255,0)

class rtpkt:
  def __init__(self,sourceID,destID,minCost):
    self.sourceID = sourceID
    self.destID = destID
    self.minCost = [minCost[0],minCost[1],minCost[2],minCost[3]]

class VisualPacket:
  def __init__(self,screen,x,y,xSpeed,ySpeed,xDest,yDest,packet,color):
    self.screen = screen
    self.x = x
    self.y = y
    self.xSpeed = xSpeed
    self.ySpeed = ySpeed
    self.xDest = xDest
    self.yDest = yDest
    self.myPacket = packet
    self.hasReachedDest = False
    self.color = color

  def update(self):
    self.x += self.xSpeed
    self.y += self.ySpeed

    if math.sqrt((self.x - self.xDest)**2 + (self.y - self.yDest)**2) < 10:
      self.hasReachedDest = True

  def draw(self):
    pg.draw.circle(self.screen,self.color,(int(self.x),int(self.y)),10,3)
