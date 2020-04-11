def main():
	computerScore = 0
	userScore = 0
	while True:
		print("Welcome to BlackJak!")
		bet = int(input("How much is your wager?"))
		if bet < 0:
			print("Your bet needs to be more than 0.\n")
		break
main()
