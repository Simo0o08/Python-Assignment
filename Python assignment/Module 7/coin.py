import random
class coin:
	def __init__(self):
		self.sideup="heads"
	def Toss(self):
		if(random.randint(0,1))==1:
			self.sideup="heads"
		else:
			self.sideup="Tails"
	def get_sideup(self):
		return self.sideup

def main():
	my_coin=coin()
	print("This side is up : ",my_coin.get_sideup())
	print("I am Tossing the coin.......!")
	my_coin.Toss()
	print("This side is up : ",my_coin.get_sideup())

main()