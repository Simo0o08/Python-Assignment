import random
class card:
	def __init__(self,faces,suit):
		self.faces=faces
		self.suit=suit
	def add_card(self):
		return cards.append([self.face,self.suit,self.value])
	def __str__():
		return face,suit,value

faces={'Ace':1,"king":13,"Queen":12,"Jack":11}
suit=["Heart","Spade","Diamond","Club"]
value=[2,3,4,5,6,7,8,9,10]

cards={}
class Deck:
	def remove(self,f1,num1):
		cards={"Heart":[1,2,3,4,5,6,7,8,9,10,11,12,13],"Spade":[1,2,3,4,5,6,7,8,9,10,11,12,13],"Diamond":[1,2,3,4,5,6,7,8,9,10,11,12,13],"Club":[1,2,3,4,5,6,7,8,9,10,11,12,13]}
		
		del(cards[f1][num1-1])
		
		return cards
		
	

t=0


class Hand():

	def Draw_card(self,d):
		self.d=d
		total=int(input("Enter Total sum : "))
		input("Press enter to Select first card : ")
		num1=random.randint(1,13)
		f1=random.choice(suit)
		print(f1,num1)
		
		d.remove(f1,num1)
	
		sum=num1
		def select():
			nonlocal sum
			num2=random.randint(1,13)
			f2=random.choice(suit)
			input("Press enter to Select another one : ")
			
			print(f2,num2)
			d.remove(f2,num2)
		
			if(num2==num1 and f1==f2):	
				select()
		
			sum=sum+num2
			
			p=sum
			return p
		s=select()
		t=0
		while(True):
			if(s<total and t<total):
				print("Your sum is smaller than" , total )
				t=select()
			else: 
				print("You WOn")
				break
	
			if(t>total):
				print("You won")
				break
			
		
		return t


	
		

		



def main():
	hand=Hand()
	deck=Deck()
	print(hand.Draw_card(deck))



	

main()
	
			
	
	


