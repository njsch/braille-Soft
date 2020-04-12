def welcome():
	print("Hi! Let's play a game of twenty-three bricks.")

	message = input("Do you need instructions? Type Y for Yes or N for No.\n")
	if message.upper() == "Y":
		print("You have a pile of twenty-three bricks.\n")
		print("You and another person, or the computer can take one, two, or three bricks.\n")
		print("Whoever takes the last brick loses!\n")


welcome()