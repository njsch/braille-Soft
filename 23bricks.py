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
			bricks -=bricksInput
			print("You take",bricksInput,"leaving",bricks)
			if bricks == 0:
				print("Sorry, you took the last brick and lost!\n")
				playAgain = input("Do you want to play again? Type Y for Yes or N for No.\n")
				if playAgain == "Y":
					continue

