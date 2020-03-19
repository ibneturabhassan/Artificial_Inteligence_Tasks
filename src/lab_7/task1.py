import math

def minimax(CurrentPosition, nodeIndex, maximizingPlayer, scoreTree, targetDepth):
    # base case
    if (CurrentPosition == targetDepth):
        return scoreTree[nodeIndex]

    # recursive case
    if (maximizingPlayer):
        return max(minimax(CurrentPosition + 1, nodeIndex * 2,
                           False, scoreTree, targetDepth),
                   minimax(CurrentPosition + 1, nodeIndex * 2 + 1,
                           False, scoreTree, targetDepth))

    else:
        return min(minimax(CurrentPosition + 1, nodeIndex * 2,
                           True, scoreTree, targetDepth),
                   minimax(CurrentPosition + 1, nodeIndex * 2 + 1,
                           True, scoreTree, targetDepth))


scoreTree = [5, 3, 6, 7, 4, 9, 18, 14]
treeDepth = math.log(len(scoreTree), 2)
print("The optimal value is : ", end="")
print(minimax(0, 0, True, scoreTree, treeDepth))
