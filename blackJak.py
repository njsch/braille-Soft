def main():
	print("welcome To BlackJak!\n")
	money = 30000
	line = 1
	while True:
		card = 0
		ds = 0
		us = 0
		dn = 0
		un = 0
		bet = 0
		while line == 1:
			print("\nYou have $" + str(money) + ".00.\n")
			bet = int(input("How much is your wager?\n"))
			line = 2
			break
		while line == 2:
			if bet == 0:
				print("DON'T BE A WISE ASS!\n")
				line = 1
				break

main()
