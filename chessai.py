import chess
board = chess.Board()

def player(board):
    if board.turn == False:
        return "b"
    elif board.turn == True:
        return "w"

def actions(board):
    total_actions = []
    for move in board.legal_moves:
        total_actions.append(move)
    return total_actions

