#Using pass keyword to passing the error we found 
try:
	x = int(input("What the ?: "))
except ValueError:
	pass
else:
	print(f"x is {x}")