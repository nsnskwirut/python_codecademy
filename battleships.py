#!/opt/ute/python/bin/python


from random import randint

WIN = -1

def print_board(board):
	for row in board:
		print " ".join(row)


def random_row(board):
	return randint(0, len(board) - 1)


def random_col(board):
	return randint(0, len(board[0]) - 1)


def Main():
	global WIN

	# Board print, ship location set, set attempts aviable
	board = []
	for x in range(5):
		board.append(["O"] * 5)
	ship_row = random_row(board)
	ship_col = random_col(board)
	attempts = 5

	# Start the game
	print('Ship location: ({0},{1})'.format(ship_row, ship_col))

	for turn in range(attempts):
		print("Turn {}/{}".format(str(turn + 1), attempts))
		guess_row = int(raw_input("Guess Row: "))
		guess_col = int(raw_input("Guess Col: "))
		if turn != attempts + 1:
			# Winning condition
			if guess_row == ship_row and guess_col == ship_col:
				print("Congratulations! You sunk my battleship!")
				board[guess_row][guess_col] = "s"
				print_board(board)
				WIN = 1
				break
			else:
				# Guess out of board
				if (guess_row < 0 or guess_row > 4) or (guess_col < 0 or guess_col > 4):
					print("Out of board!")
				# Guessed the same c,r again
				elif (board[guess_row][guess_col] == "X"):
					print("You guessed that one already.")
				#Miss
				else:
					print("You missed my battleship!")
					board[guess_row][guess_col] = "X"
	if WIN != 1:
		print("Game over! Ship was located r:{1} c:{0}".format(ship_col, ship_row))
		board[ship_row][ship_col] = "@"
		print_board(board)



if __name__ == '__main__':
	Main()
