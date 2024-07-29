def print_pattern (x):
	if(x<1) :
		return False;
	else :
		z=int(x);
		if(z-x) :
			return False;
		return True;
k = print_pattern(0);
if(k):
	print("Work in progress")
else :
	print("Enter valid number")