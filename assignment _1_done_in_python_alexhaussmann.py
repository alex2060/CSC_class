
##interactive average program 

##This program askes the user to askes the user to imput to real numbers 
#caclulats and prints the avererag and prints th numbers 
##alex haussmann 
##program #1 cs 1050 section 1

def get_a_float_F(promt):    									# get a float by user imput
	while 1:
		number=input(promt)
		try:
			test=float(number)
			return float(number)
		except:
			print("not a number try again")

def sum_grose_savings_of_goods_F():
	saving=0												# total saveings
	again="y"
	while again.lower()=="y":
		priceofgood=get_a_float_F("price of good: ")		#geters price of good
		percenttax=get_a_float_F(" percent tax on good: ")	# gets percent tax of good 
		saving=percenttax*priceofgood						# adds percent of tax on good to saving
		again=input("enter another good y/n")   			# askes if another good needs to be added
	print("total savings was"+str(saving)+"")
sum_grose_savings_of_goods_F()


