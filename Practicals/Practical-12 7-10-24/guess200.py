import random 
def game() :
	num = random.randint(1,200)
	chances = 0
	while chances != 5 :
		guess_num = int(input("guess the number between 1-200 :"))
		if guess_num == num :
			return "You Won!!! yeeee"
		chances += 1
		if guess_num - num < 0 :
			print("You guessed a small number")
		else :
			print("You guessed a big number")
	else :
		print(num)
		return "You Lost! The guess is incorrect"
print(game())