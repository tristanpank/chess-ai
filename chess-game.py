import chess
import time

board = chess.Board()

from chessai import player, actions, result, evaluation, minimax, max_value, min_value


# Getting AI chess color
while True:
    ai_color = input("AI Color (w or b): ").lower()
    if ai_color == "w" or ai_color == "b":
        break

while board.is_checkmate() == False:
    print()
    print(board)
    if player(board) == ai_color:
        start_time = time.time()
        move = minimax(board, 3)
        board.push(move)
        end_time = time.time()
        total_time = round(end_time - start_time, 2)
        print("Time: " + str((total_time)))
    else:
        while True:
            human_move = input("Move: ")
            try:
                board.push_san(human_move)
            except:
                continue
            break

print("Checkmate")
print(board)
