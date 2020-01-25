class car:
	def __init__(self,color,mileage):
		self.color=color
		self.mileage=mileage
	def __str__(self):
		return f"a {self.color} car gives {self.mileage} mileage."

def main():
	Car=car("Blue",12)
	print(Car)

main()
	