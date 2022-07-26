import chess
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
        # AI move function will go here
        # Be careful will cause infinite loop for now
        move = minimax(board, 3)
        board.push(move)
    else:
        while True:
            human_move = input("Move: ")
            try:
                board.push_san(human_move)
            except:
                continue
            break
        
