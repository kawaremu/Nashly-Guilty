def find_nash_equilibrium(matrix):
    player1_strategies = len(matrix)
    player2_strategies = len(matrix[0])

    player1_best_strategy = 0
    player2_best_strategy = 0
    max_payoff = -float('inf')

    for i in range(player1_strategies):
        for j in range(player2_strategies):
            if matrix[i][j] > max_payoff:
                max_payoff = matrix[i][j]
                player1_best_strategy = i
                player2_best_strategy = j

    for i in range(player1_strategies):
        payoff_i = matrix[i][player2_best_strategy]
        best_for_i = True
        for j in range(player2_strategies):
            if matrix[i][j] > payoff_i:
                best_for_i = False
                break
        if best_for_i:
            for j in range(player2_strategies):
                payoff_j = matrix[player1_best_strategy][j]
                best_for_j = True
                for i in range(player1_strategies):
                    if matrix[i][j] > payoff_j:
                        best_for_j = False
                        break
                if best_for_j:
                    return (player1_best_strategy, player2_best_strategy)

    return None