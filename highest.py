a = int (input("enter first value: "))
b = int (input("enter second value: "))
c = int (input("enter third value: "))

if a >= b and a >= c:
	print (str(a) + " is highest value.")
elif b > a and b > c:
	print (str(b) + " is highest value.")
	
elif c > a and c > b:
	print (str(c) + " is highest value.")