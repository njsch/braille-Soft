import random

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


	card = 0
	while card < 21:
		finalUser =2
		card = random.randint(1,10)
		user = card
		user += card
		print(user)
	if user == "21":
		print("cool")
		break

game()