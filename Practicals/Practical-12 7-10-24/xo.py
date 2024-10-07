import random

def display (grid,size) :
	print(" --- " + "--- "*(size-1))
	for i in range(size) :
		truth_val = True
		for k in range (1,size+1) :
			print("|"*truth_val +" " + str(grid[i][k]) + " "+ "|",end ="")
			truth_val = False
		print(" ")
		print(" --- " + "--- "*(size-1))


def make_grid(size) : #Pratham
	result = []
	for _ in range(size) :
		result.append(dict(zip(range(1,size+1)," "*(size+1))))
	return result


def start(size,grid) :
	names = ["",""]
	names[0] = (input("Enter Name Of Player 1 : ")).upper()
	names[1] = (input("Enter Name Of Player 2 : ")).upper()
	player1 = names[0][0]
	player2 = names[1][0]
	if player1 == player2 :
		names[1] = (input("Enter Pet Name Of Player 2 : ")).upper()
	first_chance = random.randint(0,1)
	if first_chance :
		names[0],names[1] = names[1],names[0]
		player1,player2 = player2,player1
	chance = 0 
	while chance < (size*size) :
		move = input()