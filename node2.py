
#routing packet contains min cost info to neghboring nodes
class rtpkt:
  def __init__(self,sourceID,destID,minCost):
    self.sourceID = sourceID
    self.destID = destID
    self.minCost = [minCost[0],minCost[1],minCost[2],minCost[3]]

class Node2:
  def __init__(self):
    self.id = 2
    self.neighbors = list()
    self.distanceTable = [[9999,9999,9999,9999],[9999,9999,9999,9999],[9999,9999,9999,9999],[9999,9999,9999,9999]]
    self.myPacketsToSend = list()

  def addNeighbors(self,n0,n1,n3):
    self.neighbors.append(n0)
    self.neighbors.append(n1)
    self.neighbors.append(n3)

  def rtinit2(self):

    self.distanceTable = [
      [9999,9999,9999,9999],
      [9999,9999,9999,9999],
      [3,1,0,2],
      [9999,9999,9999,9999],
    ]
    #create packets to send info for each neighbor
    for n in self.neighbors:
      currentID = n.id
      minCost = []
      minCost.append(self.distanceTable[2][0])
      minCost.append(self.distanceTable[2][1])
      minCost.append(self.distanceTable[2][2])
      minCost.append(self.distanceTable[2][3])
      self.myPacketsToSend.append(rtpkt(2,currentID,minCost))

  def rtupdate2(self,rtpacket):
    #unpack packet
    sourceID = rtpacket.sourceID
    destID = rtpacket.destID
    minCost = rtpacket.minCost

    row = sourceID
    for col in range(0,4): #copy over new values from packet
      self.distanceTable[row][col] = minCost[col]

    otherRows = list()
    if destID != 0: otherRows.append(0)
    if destID != 1: otherRows.append(1)
    if destID != 2: otherRows.append(2)
    if destID != 3: otherRows.append(3)
    #now check and see if theres a better path
    for col in range(0,4):
      for otherR in otherRows:
        if self.distanceTable[destID][otherR] + self.distanceTable[otherR][col] < self.distanceTable[destID][col]: #then replace
          self.distanceTable[destID][col] = self.distanceTable[destID][otherR] + self.distanceTable[otherR][col]

          #create packets to send info for each neighbor
          for n in self.neighbors:
            currentID = n.id
            minCost = []
            minCost.append(self.distanceTable[2][0])
            minCost.append(self.distanceTable[2][1])
            minCost.append(self.distanceTable[2][2])
            minCost.append(self.distanceTable[2][3])
            self.myPacketsToSend.append(rtpkt(2,currentID,minCost))

  def printDistanceTable(self):
    print("***Node 2***")
    print(self.distanceTable)