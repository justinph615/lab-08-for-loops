
average = 0
sum = 0


for i in range (0, 4):

	
	userinput = input("Number please ")
	usernum = int((userinput))
	sum = (sum + usernum)

	print("User number is: " , usernum , "current sum is: " , sum)
	

average = (sum / 4)

print("The average is ", average)
		
