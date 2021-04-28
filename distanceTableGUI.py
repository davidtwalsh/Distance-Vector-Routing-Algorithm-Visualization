import pygame as pg
from drawText import draw_textLeftToRight

class distanceTableGUIObject:
  def __init__(self,screen,x,y,ID,node):
    self.screen = screen
    self.x = x
    self.y = y
    self.ID = ID
    self.myNode = node

    self.fontNormal = pg.font.SysFont('Arial',32)
    self.colorBlack = (0,0,0)
    self.colorBlue = (45,93,204)
    self.padding = 50
    self.width = 190
    self.height = 190


    self.distanceTable = [[1,2,9999,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
    self.changeMatrix = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]

  def resetChangeMatrix(self):
    self.changeMatrix = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
    
  def setTable(self):
    for row in range(0,4):
      for col in range(0,4):
        self.distanceTable[row][col] = self.myNode.distanceTable[row][col]

  def update(self):
    # if self.ID == 1:
    #   isSame = True
    #   for row in range(0,4):
    #     for col in range(0,4):
    #       if self.distanceTable[row][col] != self.myNode.distanceTable[row][col]:
    #         isSame = False
    #   if isSame == False:
    #     print("change detected")
    
    # self.distanceTable = self.myNode.distanceTable
    for row in range(0,4):
      for col in range(0,4):
        if self.distanceTable[row][col] != self.myNode.distanceTable[row][col]:
          self.changeMatrix[row][col] = 1
        self.distanceTable[row][col] = self.myNode.distanceTable[row][col]

  def draw(self):
    #draw id of obj for table (topLeft of x,y)
    draw_textLeftToRight(str(self.ID),self.fontNormal,self.colorBlack,self.screen,self.x,self.y)
    #draw the header(same for all distanceTableGUIObjects)
    #header left->right
    draw_textLeftToRight("0",self.fontNormal,self.colorBlack,self.screen,self.x + self.padding,self.y)
    draw_textLeftToRight("1",self.fontNormal,self.colorBlack,self.screen,self.x + self.padding*2,self.y)
    draw_textLeftToRight("2",self.fontNormal,self.colorBlack,self.screen,self.x + self.padding*3,self.y)
    draw_textLeftToRight("3",self.fontNormal,self.colorBlack,self.screen,self.x + self.padding*4,self.y)
    #header top->bottom
    draw_textLeftToRight("0",self.fontNormal,self.colorBlack,self.screen,self.x,self.y + self.padding)
    draw_textLeftToRight("1",self.fontNormal,self.colorBlack,self.screen,self.x,self.y + self.padding * 2)
    draw_textLeftToRight("2",self.fontNormal,self.colorBlack,self.screen,self.x,self.y + self.padding * 3)
    draw_textLeftToRight("3",self.fontNormal,self.colorBlack,self.screen,self.x,self.y + self.padding * 4)

    #draw chart lines
    pg.draw.line(self.screen,self.colorBlack,[self.x+self.padding-16,self.y],[self.x+self.padding-16,self.y+self.padding + self.height],5)
    pg.draw.line(self.screen,self.colorBlack,[self.x,self.y+self.padding-8],[self.x+self.padding+self.width,self.y+self.padding-8],5)

    #draw from and to
    draw_textLeftToRight("from",self.fontNormal,self.colorBlack,self.screen,self.x-70,self.y + int(self.height/2) + 20)
    draw_textLeftToRight("to",self.fontNormal,self.colorBlack,self.screen,self.x + int(self.width/2) + 30,self.y - 40)

    #draw dist table values
    for row in range(0,4):
      for col in range(0,4):
        val = self.distanceTable[col][row]
        strVal = ""
        if val == 9999:
          strVal = "inf."
        else:
          strVal = str(val)
        draw_textLeftToRight(strVal,self.fontNormal,self.colorBlack,self.screen,self.x+self.padding + self.padding * row,self.y+self.padding + self.padding * col)

    #draw dist table changed values
    for row in range(0,4):
      for col in range(0,4):
        val = self.distanceTable[col][row]
        strVal = ""
        if val == 9999:
          strVal = "inf."
        else:
          strVal = str(val)
        if self.changeMatrix[col][row] == 1:
          draw_textLeftToRight(strVal,self.fontNormal,self.colorBlue,self.screen,self.x+self.padding + self.padding * row,self.y+self.padding + self.padding * col)

