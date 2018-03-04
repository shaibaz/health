sugar_fast = int(input("Please Enter Your Sugar Level While Fasting: "))
sugar_post = int(input("Please Enter Your Sugar Level After Eating: "))

def diabetes_check(sugar_fast, sugar_post):
	if sugar_fast > 109 and sugar_post > 140:
		print ("You are suffering from Diabetes with the values {} and {}".format(sugar_fast, sugar_post))
	else:
		print ("You are NOT suffering from Diabetes with the values {} and {}".format(sugar_fast, sugar_post))

diabetes_check(sugar_fast, sugar_post)
