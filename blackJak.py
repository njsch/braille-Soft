import random

def main():
	computerScore = 0
	userScore = 0
	totalUserMoney = 30000

	while True:
		print("Welcome to BlackJak!\n")
		print("you have","$",totalUserMoney,"\n")
		bet = int(input("How much is your wager?\n"))

		if bet < 0:
			print("Your bet needs to be more than 0.\n")

		elif bet == 0:
			print("DON'T BE A WISE ASS!\n")
		break



main()
