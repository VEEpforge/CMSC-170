from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from functools import partial
from math import inf as INFINITY
from random import choice

# -1 empty cell ; 0 O cell ; 1 X cell
global board
# board = [[ "_" for col in range(3)] for row in range(3)]
board = [
    [ '_' , '_' , '_' ],
    [ '_' , '_' , '_' ],
    [ '_' , '_' , '_' ]
]

# Declaration of variables
row, col = 3 , 3
player = [ 'O' , 'X' ]
# human = 0
# ai = 0
current_player = 0
global isMax
window = Tk()

def updateBoard(i,j, t):
    button[i][j].config(text=t, state=DISABLED)
    board[i][j] = t
    print(board)

def checkWinner():
	if ((board[0][0] == human and board[0][1] == human and board[0][2] == human) or
		(board[1][0] == human and board[1][1] == human and board[1][2] == human) or
        (board[2][0] == human and board[2][1] == human and board[2][2] == human) or
		(board[0][0] == human and board[1][0] == human and board[2][0] == human) or
		(board[0][1] == human and board[1][1] == human and board[2][1] == human) or
		(board[0][2] == human and board[1][2] == human and board[2][2] == human) or
		(board[0][0] == human and board[1][1] == human and board[2][2] == human) or
		(board[0][2] == human and board[1][1] == human and board[2][0] == human)):
		return (True, "Player")
        # return human

	elif ((board[0][0] == ai and board[0][1] == ai and board[0][2] == ai) or
        (board[1][0] == ai and board[1][1] == ai and board[1][2] == ai) or
        (board[2][0] == ai and board[2][1] == ai and board[2][2] == ai) or
        (board[0][0] == ai and board[1][0] == ai and board[2][0] == ai) or
        (board[0][1] == ai and board[1][1] == ai and board[2][1] == ai) or
        (board[0][2] == ai and board[1][2] == ai and board[2][2] == ai) or
        (board[0][0] == ai and board[1][1] == ai and board[2][2] == ai) or
        (board[0][2] == ai and board[1][1] == ai and board[2][0] == ai)):
		return (True, "AI")
		
	else: return (False,"none")
	

def gameOver():
	# global window
	meronNaba = checkWinner()
	if(meronNaba[0]):
		print("winner")
		answer = messagebox.showinfo("",meronNaba[1] + " wins!")
		# print(answer)
		if(answer=="ok"): window.destroy()
	elif(noMovesLeft(board)):
		answer2 = messagebox.showinfo("","Draw")
		if(answer2=="ok"): window.destroy()


def evaluate(board, depth, maxx):
    # score = 0
	if ((board[0][0] == human and board[0][1] == human and board[0][2] == human) or
        (board[1][0] == human and board[1][1] == human and board[1][2] == human) or
        (board[2][0] == human and board[2][1] == human and board[2][2] == human) or
        (board[0][0] == human and board[1][0] == human and board[2][0] == human) or
        (board[0][1] == human and board[1][1] == human and board[2][1] == human) or
        (board[0][2] == human and board[1][2] == human and board[2][2] == human) or
        (board[0][0] == human and board[1][1] == human and board[2][2] == human) or
        (board[0][2] == human and board[1][1] == human and board[2][0] == human)):
       	#prevent human from winning; prolong the game
		if(maxx): return (100 + depth)
		else: return (-100 - depth)

	elif ((board[0][0] == ai and board[0][1] == ai and board[0][2] == ai) or
        (board[1][0] == ai and board[1][1] == ai and board[1][2] == ai) or
        (board[2][0] == ai and board[2][1] == ai and board[2][2] == ai) or
        (board[0][0] == ai and board[1][0] == ai and board[2][0] == ai) or
        (board[0][1] == ai and board[1][1] == ai and board[2][1] == ai) or
        (board[0][2] == ai and board[1][2] == ai and board[2][2] == ai) or
        (board[0][0] == ai and board[1][1] == ai and board[2][2] == ai) or
        (board[0][2] == ai and board[1][1] == ai and board[2][0] == ai)):
		if(maxx): return (100 - depth)		#pabilisin yung game
		else: return (-100 + depth)	

	else: return 0

def noMovesLeft(board):
    for i in range(row):
        for j in range(col):
            if(board[i][j] == '_'):
                return False
    return True

def minmax(board, depth, maxx, char):
    global bestMove, ai_switch

    s = evaluate(board, depth, maxx)

    if(s != 0):
        return s

    #no more moves, TIE
    if(noMovesLeft(board) == True):
        return 0
    
    if(maxx):
        best = -INFINITY

        for i in range(row):
            for j in range(col):
                if(board[i][j] == '_'):
                    #move
                    board[i][j] = char

                    if(char == ai):
                        char = human
                    else:
                        char = ai

                    moveValue = minmax(board, depth+1, not maxx, char)
                    
                    # best = max(best, moveValue)
                    if(moveValue > best):
                        best = moveValue
                        # print("BEST MAX: ", best)
                        bestMove = [i,j]
                
                    #undo
                    board[i][j] = '_'
        
        return best

    else:
        best = +INFINITY

        for i in range(row):
            for j in range(col):
                if(board[i][j] == '_'):
                    #move
                    board[i][j] = char

                    if(char == ai):
                        char = human
                    else:
                       char = ai

                    moveValue = minmax(board, depth+1, maxx, char)

                    if(moveValue < best):
                        best = moveValue
                        # print("BEST MIN: ", best)
                        bestMove = [i,j]
                   
                    #undo
                    board[i][j] = '_'

        return best

def start_check(board):
    count = 0
    for i in range(row):
        for j in range(col):
            if(board[i][j] == '_'):
                count = count + 1
    return count

def aiMove():
	global current_player

	if(start_check == 9):	#randomized first move
		x = choice([0,1,2])
		y = choice([0,1,2])
		updateBoard(x, y, ai)
	else:
		if(isMax):
			best = minmax(board, 0, True, ai)
		else:
			best = minmax(board, 0, False, ai)
		print("FINAL: ", best)
		updateBoard(bestMove[0], bestMove[1], ai)

	if(checkWinner()[0] or noMovesLeft(board)):
		gameOver()
	else: current_player = human

def humanMove(i,j):
	global current_player
    
	print(current_player)
	updateBoard(i,j,human)

	if(checkWinner()[0] or noMovesLeft(board)):
		gameOver()
	else:
		current_player = ai
		aiMove()

def gameBoard():
    board_frame = Frame(window, bg="#222222")
    board_frame.pack()

    global button, human
    button = []
    for i in range(row):
        button.append(i)
        button[i] = []
        for j in range(col):
            player_move = partial(humanMove, i, j)
            button[i].append(j)
            button[i][j] = Button(board_frame,
                font="Helvetica 19 bold", bg="white",
                activebackground="#509bb9",
                highlightbackground="#222222",
                width=5, height=3,
                relief="flat", command=player_move
            )
            button[i][j].grid(row=i, column=j)

    #update board
    for i in range(row):
        for j in range(col):
            if board[i][j] == 'X':
                button[i][j].config(text='X', state=DISABLED)
            elif board[i][j] == 'O':
                button[i][j].config(text='O', state=DISABLED)

    # if AI go first
    if current_player == ai:
        aiMove()

def playerOrder() :
    # global isMax
    menu_frame.pack_forget()
    order_frame = Frame(window, bg="#222222", height="300")
    order_frame.pack()

    def play1(): 
        global isMax, current_player
        isMax = False
        current_player = human
        order_frame.pack_forget()
        gameBoard()

    def play2():
        global isMax, current_player
        isMax = True
        current_player = ai
        order_frame.pack_forget()
        gameBoard()


    Label(order_frame,
    text='Choose player order:', font='Helvetica 14 bold',
    height='2', bg="#222222", fg="white"
    ).pack()

    player1_button = Button(order_frame,
        text = "Player 1",
        font="Helvetica 14 bold",
        width="15", height="1",
        bg="#509bb9", fg="white",
        activeforeground="white",
        activebackground="#222222",
        highlightbackground="#509bb9",
        relief="flat", command=play1
    )
    player1_button.pack(pady=8)

    player2_button = Button(order_frame,
        text = "Player 2", 
        font="Helvetica 14 bold",
        width="15", height="1",
        bg="#509bb9", fg="white",
        activeforeground="white",
        activebackground="#222222",
        highlightbackground="#509bb9",
        relief="flat", command=play2
    )
    player2_button.pack(pady=8)

def playX() :
    global human, ai
    human = 'X'
    ai = 'O'
    # current_player = human
    playerOrder()
	# play(current_player)
    
def playO() :
    global human, ai

    human = 'O'
    ai = 'X'
    # current_player = ai
    playerOrder()
    # play(current_player)

def exit():
    window.destroy()


if __name__ == "__main__":
	# global window
	# window = Tk()
	window.title("Tic Tac Toe")
	window.geometry("300x300")
	window.resizable(False, False)
	window.config(background = "#222222")

	menu_frame = Frame(window, bg="#222222")

	Label(menu_frame,
		text='Tic Tac Toe', font='Helvetica 25 bold',
		height='2', bg="#222222", fg="white"
	).pack()

	X_button = Button(menu_frame,
			text = "X", font="Helvetica 14 bold",
			width="15", height="1",
			bg="#509bb9", fg="white",
			activeforeground="white",
			activebackground="#222222",
			highlightbackground="#509bb9",
			relief="flat", command=playX
	)
	X_button.pack(pady=8)

	O_button = Button(menu_frame,
			text = "O", font="Helvetica 14 bold",
			width="15", height="1",
			bg="#509bb9", fg="white",
			activeforeground="white",
			activebackground="#222222",
			highlightbackground="#509bb9",
			relief="flat", command=playO
	)
	O_button.pack(pady=8)

	exit_button = Button(menu_frame,
			text = "Exit", font="Helvetica 14 bold",
			width="15", height="1",
			bg="#509bb9", fg="#222222",
			activeforeground="white",
			activebackground="#222222",
			highlightbackground="#509bb9",
			relief="flat", command=exit
	)
	exit_button.pack(pady=8)

	menu_frame.pack()

	window.mainloop()
