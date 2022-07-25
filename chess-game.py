import chess
board = chess.Board()

# Getting AI chess color
while True:
    ai_color = input("AI Color (w or b): ").lower()
    if ai_color == "w":
        ai_color = True
        break
    elif ai_color == "b":
        ai_color = False
        break

while board.is_checkmate() == False:
    print(board)
    if board.turn == ai_color:
        # AI move function will go here
        # Be careful will cause infinite loop for now
        continue
    else:
        while True:
            human_move = input("Move: ")
            try:
                board.push_san(human_move)
            except:
                continue
            break
        
