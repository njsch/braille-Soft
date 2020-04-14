import random
def main():
	print("welcome To BlackJak!\n")
	money = 30000
	line = 1
	playing = True
	while playing == True:
		card = 0
		ds = 0
		us = 0
		dn = 0
		un = 0
		bet = 0
		while line == 1:
			print("\nYou have $" + str(money) + ".00.\n")
			try:
				betstr = input("How much is your wager?\n")
				bet = int(betstr)
				line = 2
				break
			except EOFError:
				print("Please don't terminate your input with a CONTROL-Z character.\n")
			except ValueError:
				print("SYNTAX ERROR! JUST ENTER A NUMBER!\n")
		while line == 2:
			if bet == 0:
				print("DON'T BE A WISE ASS!\n")
				line = 1
				break
			elif bet > money:
				print("COME ON NOW! YOU DON'T HAVE THAT MUCH MONEY!\n")
				line = 1
				break
			line = 3
		while line == 3:
			card = random.randint(1, 10)
			ds = card
			print("The Dealer's first card is the Down Card.\n")
			card = random.randint(1, 10)
			us = card
			print("Your first card has " + str(card) + " showing.\n")
			card = random.randint(1, 10)
			ds += card
			dn = 2
			print("The Dealer's second card has " + str(card) + " showing.\n")
			card = random.randint(1, 10)
			un = 2
			us += card
			print("Your second card has " + str(card) + " showing.\n")
			if us == 21:
				print("You are lucky! You have BLACKJAK!\n")
				line = 5
				break
			elif us > 21:
				print("BUSTED!\n")
				line = 5
				break
			line = 4
		while line == 4:
			print("You have " + str(us) + " in " + str(un) + " cards.\n")
			key = input("Do you want another card? Type Y for Yes or N for No.\n")
			if key.upper() == "Y":
				card = random.randint(1, 10)
				us += card
				un += 1
				print("\nYour next card has " + str(card) + " showing.\n")
				if us == 21:
					print("You have blackjak!\n")
					line = 5
					break
				elif us > 21:
					print("BUSTED!\n")
					us = 0
					line = 5
					break
			elif key.upper() == "N":
				line = 5
				print("Let's see what I can do!\n")
				break
			if us > 21:
				print("BUSTED!\n")
				us = 0
				line = 5
				break
		while line == 5:
			card = random.randint(1, 10)
			ds += card
			dn += 1
			print("My next card has " + str(card))
			if ds > 17:
				print("I have " + str(ds) + " in " + str(dn) + " cards.\n")
				line = 6
				break
		while line == 6:
			if ds > 21:
				print("BUSTED\n")
				ds = 0
			if ds == us:
				print("It's a tie! We push!\n")
				line = 7
				break
			elif ds > us:
				money -= bet
				if money < 0 or money == 0:
					print("Sorry, you lost all your money and you are now out of the game.\n")
					print("Better luck next time!\n")
					playing = False
					break
				print("The Dealer wins!\n")
				line = 7
				break
			money += bet
			print("Congradulations, you won!\n")
			line = 7
			break
		while line == 7:
			print("You now have $" + str(money) + ".00.\n")
			key = input("Do you want to play again? Type Y for Yes or N for No.\n")
			if key.upper() == "N":
				playing = False
				break
			elif key.upper() == "Y":
				line = 1
				break

main()
