class Info:
	def __init__(self,name,phone_no,email_address):
		self.name=name
		self.phone_no=phone_no
		self.email_address=email_address
	def set_name(self,n):
		self.name=n
	def set_phone(self,p):
		self.phone_no=p
	def set_email(self,e):
		self.email_address=e
	def get_name(self):
		return self.name
	def get_phone(self):
		return self.phone_no
	def get_email(self):
		return self.email_address
	def __str__(self):
		return f"Name:{self.name}, Phone_NO.:{self.phone_no}, Email_Address: {self.email_address}"


def main():
	i=Info(input("Enter your name : "),input("Enter your phone_number : "),input("Enter your Email_ id : "))
	i.set_name(input("Enter your name : "))
	i.set_email(input("Enter your Email_ id : "))
	i.set_phone(input("Enter your phone_number : "))
	print("Name is: ",i.get_name())
	print("Email is ",i.get_email())
	print("Phone no. is ",i.get_phone())
	
	print(i)
	

	
	

main()