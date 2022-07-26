import chess
board = chess.Board()

def player(board):
    if board.turn == False:
        return "b"
    elif board.turn == True:
        return "w"

