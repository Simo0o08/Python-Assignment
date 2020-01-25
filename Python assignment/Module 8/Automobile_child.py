from Automobile_parent import Automobile

class car(Automobile):
	def __init__(self,__doors,__make,__model,__mileage,__price):
		Automobile.__init__(self,__make,__model,__mileage,__price)
		self.__doors=__doors
	def set_doors(self,d):
		self.__doors=d
	def get_doors(self):
		return self.__doors
class Truck(Automobile):
	def __init__(self,__drive_type,__make,__model,__mileage,__price):
		Automobile.__init__(self,__make,__model,__mileage,__price)
		self.__drive_type=__drive_type
	def set_drive_type(self,d):
		self.__drive_type=d
	def get_drive_type(self):
		return self.__drive_type

class SUV(Automobile):
	def __init__(self,__pass_cap,__make,__model,__mileage,__price):
		Automobile.__init__(self,__make,__model,__mileage,__price)
		self.__pass_cap=__pass_cap
	def set_pass_cap(self,pc):
		self.__pass_cap=pc
	def get_pass_cap(self):
		return self.__pass_cap	



def main():
	c=car("A","B","C","D","E")
	print(f"Car has doors= {c.get_doors()},make= {c.get_make()} ,model= {c.get_model()} mileage = {c.get_mileage()} and price = {c.get_price()}")

	t=Truck("1","2","3","4","5")
	print(f"Truck has drive_type= {t.get_drive_type()},make={t.get_make()} , model= {t.get_model()} , mileage={t.get_mileage()} and price={t.get_price()}")
	s=SUV("p","q","r","s","t")
	print(f"SUV has pass_cap={s.get_pass_cap()},make= {c.get_make()} ,model= {c.get_model()} mileage = {c.get_mileage()} and price = {c.get_price()} ")
	
main()

	
