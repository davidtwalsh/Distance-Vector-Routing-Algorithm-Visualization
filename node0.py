
#routing packet contains min cost info to neghboring nodes
class rtpkt:
  def __init__(self,sourceID,destID,minCost):
    self.sourceID = sourceID
    self.destID = destID
    self.minCost = [minCost[0],minCost[1],minCost[2],minCost[3]]

class Node0:
  def __init__(self):
    self.id = 0
    self.neighbors = list()
    self.distanceTable = [[9999,9999,9999,9999],[9999,9999,9999,9999],[9999,9999,9999,9999],[9999,9999,9999,9999]]
    self.myPacketsToSend = list()

  def addNeighbors(self,n1,n2,n3):
    self.neighbors.append(n1)
    self.neighbors.append(n2)
    self.neighbors.append(n3)

  #called at beginning, initialize distance table in node 0, add neighbors
  def rtinit0(self):

    self.distanceTable = [
      [0,1,3,7],
      [9999,9999,9999,9999],
      [9999,9999,9999,9999],
      [9999,9999,9999,9999],
    ]
    #create packets to send info for each neighbor
    for n in self.neighbors:
      currentID = n.id
      minCost = []
      minCost.append(self.distanceTable[0][0])
      minCost.append(self.distanceTable[0][1])
      minCost.append(self.distanceTable[0][2])
      minCost.append(self.distanceTable[0][3])
      self.myPacketsToSend.append(rtpkt(0,currentID,minCost))

  #will be called when node0 receives routing packet tht was sent to it by one of its neighbors,
  #rtpkt is packet that was received
  def rtupdate0(self,rtpacket):
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
            minCost.append(self.distanceTable[0][0])
            minCost.append(self.distanceTable[0][1])
            minCost.append(self.distanceTable[0][2])
            minCost.append(self.distanceTable[0][3])
            self.myPacketsToSend.append(rtpkt(0,currentID,minCost))

  def printDistanceTable(self):
    print("***Node 0***")
    print(self.distanceTable)
      
