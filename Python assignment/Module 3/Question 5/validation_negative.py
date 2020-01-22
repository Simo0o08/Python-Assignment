num=int(input("Enter number of items "))
i=0
while(i<num):
    wholesale=float(input("Enter wholesale price "))
    if(wholesale<0):  
          print("Cannot Enter Negative Wholesale Price")
          continue
    retail=wholesale*0.5
    print("retail price of item {0} is {1}".format(i,retail))
    i=i+1
