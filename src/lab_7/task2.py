# Aplha and Beta Initial values
MAX, MIN = 10000, -10000


def minimax(depth, nodeIndex, maximizingPlayer, scoreTree, alpha, beta):

    # if leaf node is reached
    if depth == 3:
        return scoreTree[nodeIndex]

    if maximizingPlayer:
        best = MIN
        # Recursion for left and right children
        for i in range(0, 2):
            val = minimax(depth + 1, nodeIndex * 2 + i, False, scoreTree, alpha, beta)
            best = max(best, val)
            alpha = max(alpha, best)
            # Alpha Beta Pruning Condition
            if beta <= alpha:
                break
        return best
    else:
        best = MAX
        # Recursion for left and
        # right children
        for i in range(0, 2):
            val = minimax(depth + 1, nodeIndex * 2 + i, True, scoreTree, alpha, beta)
            best = min(best, val)
            beta = min(beta, best)
            # Alpha Beta Pruning Condition
            if beta <= alpha:
                break

        return best





scoreTree = [5, 3, 6, 7, 4, 9, 18, 14]

print("The optimal value is :", minimax(0, 0, True, scoreTree, MIN, MAX))