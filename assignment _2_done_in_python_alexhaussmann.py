
##interactive average program 

##This program askes the user to askes the user to imput to real numbers 
#caclulats and prints the avererag and prints th numbers 
##alex haussmann 
##program #1 cs 1050 section 1

def get_a_float_F(promt):    # get a float by user imput
	while 1:
		number=input(promt)
		try:
			test=float(number)
			return float(number)
		except:
			print("not a number try again")

def promt_for_average():
	number1=get_a_float_F("enter the frist number:")
	number2=get_a_float_F("enter the second number:")
	print("the average is "+str((number1+number2)/2)+"")
promt_for_average()


