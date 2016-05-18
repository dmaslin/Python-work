from WeightedNineTailModel import WeightedNineTailModel
from NineTailModel import NineTailModel

node = 511

tree1 = WeightedNineTailModel()
depth1 = tree1.getShortestPath(node)
tree2 = NineTailModel()
depth2 = tree2.getShortestPath(node)

if depth1 != depth2:
    print("They are not the same")
else:
    print("They are the same")
