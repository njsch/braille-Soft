import random
while True:
	print("Hi! Let's play a game of twenty-three bricks.")
	break

message = input("Do you need instructions? Type Y for Yes or N for No.\n")
while message.upper() == "Y" or message.upper() == "N":
	if message.upper() == "Y":
		print("You have a pile of twenty-three bricks.\n")
		print("You and another person, or the computer can take one, two, or three bricks.\n")
		print("Whoever takes the last brick loses!\n")
		break

	elif message.upper() =="N":
		bricks = 23
		while bricks >0:
			print("There are",bricks,"remaining\n")
			bricksInput = int(input("How many bricks do you want? Choose 1, 2, or 3.\n"))
			if  bricksInput >3:
				print("two high! enter a number between 0 and 3")
				bricksInput-= 0
			else:
				bricks -=bricksInput
				print("You take",bricksInput,"leaving",bricks)

				computerBricksInput = random.randint(1,3)
				print("There are",bricks,"remaining\n")
				bricks -= computerBricksInput
				print("I take",computerBricksInput,"leaving",bricks)


			if bricks == 0:				break
				print("Sorry, you took the last brick and lost!\n")
			else:
				print("All right! So you beat me this time.\n")

				playAgain = input("Do you want to play again? Type Y for Yes or N for No.\n")
				if playAgain == "Y":
					continue
				if playAgain == "N":
					break
