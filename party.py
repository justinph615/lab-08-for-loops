
userinput = input("Let's party! How long 'til the party? (Gimme a number)")
usernum = int(userinput)

if usernum < 1:

	print("PARTY NOW!!!")


elif usernum > 1:

	for usernum in reversed(range(1, usernum + 1)):

		print (usernum)

	print ("PARTY TIME!!!!")
