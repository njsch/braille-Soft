import random

def main():
	bet()

def bet():
	totalUserMoney = 30000
	while True:
		print("Welcome to BlackJak!\n")
		print("you have","$",totalUserMoney,"\n")
		bet = int(input("How much is your wager?\n"))

		if bet < 0:
			print("Your bet needs to be more than 0.\n")

		elif bet > totalUserMoney:
			print("COME ON NOW! YOU DON'T HAVE THAT MUCH MONEY!\n")

		elif bet == 0:
			print("DON'T BE A WISE ASS!\n")
		else:
			game(bet)


def game(bet):
	userScore = 0
	while True:
		userCard1 = random.randint(1,10)
		userCard2 = random.randint(1,10)
		userScore = userCard1+userCard2
		print(userScore)


		break

main()
