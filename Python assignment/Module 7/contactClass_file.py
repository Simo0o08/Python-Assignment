class Info:
	
	def __init__(self,name,phone_no,email_address):
		self.name=name
		self.phone_no=phone_no
		self.email_address=email_address
		
	def set_name(self,n,f):
 		f.write(n+"\n")
		
	def set_phone(self,p,f):
		f.write(p+"\n")
		
	def set_email(self,e,f):
		f.write(e+"\n")
		
	def get_name(self,f):
		f.seek(0)
		return f.readline()
	def get_email(self,f):
		return f.readline()
		
	def get_phone(self,f):
		return f.readline()
		

		

	def __str__(self):

		return f"Name:{self.name}, Phone_NO.:{self.phone_no}, Email_Address: {self.email_address}"


def main():
	f=open("contactClass.txt","r+")
	i=Info("sim","3456","@gmail.com")
	i.set_name(input("Enter your name : "),f)
	i.set_email(input("Enter your Email_ id : "),f)
	i.set_phone(input("Enter your phone_number : "),f)
	
	print("Name is: ",i.get_name(f),end="")

	print("Email is :",i.get_email(f),end="")
	print("Phone no. is :",i.get_phone(f),end="")

	print(f.read())
	f.close()

	

	
	

main()