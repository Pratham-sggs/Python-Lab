import random 
def game() :
	num = random.randint(1,20)
	guess_num = int(input("guess the number between 1-20 :"))
	return "You Won!!! yeeee" if num == guess_num else "You Lost! The guess is incorrect"
print(game())
	