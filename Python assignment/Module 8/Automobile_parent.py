class Automobile:
	def __init__(self,__make,__model,__mileage,__price):
		self.__make=__make
		self.__model=__model
		self.__mileage=__mileage
		self.__price=__price
	def set_make(self,m):
		self.__make=m	
	def get_make(self):
		return self.__make
	def set_model(self,model):
		self.__model=model
	def get_model(self):
		return self.__model
	def set_mileage(self,mileage):
		self.__mileage=mileage
	def get_mileage(self):
		return self.__mileage
	def set_price(self,p):
		self.__price=p
	def get_price(self):
		return self.__price

"""
def main():
	a=Automobile("make","model","mileage","price")
	#a.set_mileage("sim")
	print(a.get_mileage())
main()
"""
