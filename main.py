from node0 import Node0
from node1 import Node1
from node2 import Node2
from node3 import Node3
import time

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

def printNodes():
  print("****************************************************")
  node0.printDistanceTable()
  node1.printDistanceTable()
  node2.printDistanceTable()
  node3.printDistanceTable()
  print("****************************************************")
  # time.sleep(1)

################ MAIN ##################
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

# print(node0.distanceTable[0][3]) # prints 7
# print(node1.distanceTable)

isProgramRunning = True
while (isProgramRunning):

  if len(node0.myPacketsToSend) != 0:
    while len(node0.myPacketsToSend) > 0:
      packet = node0.myPacketsToSend.pop(0)
      tolayer2(packet)
      printNodes()
  elif len(node1.myPacketsToSend) != 0:
    while len(node1.myPacketsToSend) > 0:
      packet = node1.myPacketsToSend.pop(0)
      tolayer2(packet)
      printNodes()

  elif len(node2.myPacketsToSend) != 0:
    while len(node2.myPacketsToSend) > 0:
      packet = node2.myPacketsToSend.pop(0)
      tolayer2(packet)
      printNodes()

  elif len(node3.myPacketsToSend) != 0:
    while len(node3.myPacketsToSend) > 0:
      packet = node3.myPacketsToSend.pop(0)
      tolayer2(packet)
      printNodes()
  else:
    break

print("-------------------Program done------------------")