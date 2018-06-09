#President Test Score Reset:
def prezReset(): 
	
	myfile = open('1_Prez.txt', 'w')
	myfile.write("0")
	myfile.close()
	
	myfile = open('1_Name_Prez.txt', 'w')
	myfile.write("Nobody")
	myfile.close()
	
	myfile = open('2_Prez.txt', 'w')
	myfile.write("0")
	myfile.close()
	
	myfile = open('2_Name_Prez.txt', 'w')
	myfile.write("Nobody")
	myfile.close()

	myfile = open('3_Prez.txt', 'w')
	myfile.write("0")
	myfile.close()
	
	myfile = open('3_Name_Prez.txt', 'w')
	myfile.write("Nobody")
	myfile.close()
	
	myfile = open('4_Prez.txt', 'w')
	myfile.write("0")
	myfile.close()
	
	myfile = open('4_Name_Prez.txt', 'w')
	myfile.write("Nobody")
	myfile.close()
	
	myfile = open('5_Prez.txt', 'w')
	myfile.write("0")
	myfile.close()
	
	myfile = open('5_Name_Prez.txt', 'w')
	myfile.write("Nobody")
	myfile.close()


	
#Fifa Test Score Reset:
def fifaReset(): 
	
	myfile = open('1_Fifa.txt', 'w')
	myfile.write("0")
	myfile.close()
	
	myfile = open('1_Name_Fifa.txt', 'w')
	myfile.write("Nobody")
	myfile.close()
	
	myfile = open('2_Fifa.txt', 'w')
	myfile.write("0")
	myfile.close()
	
	myfile = open('2_Name_Fifa.txt', 'w')
	myfile.write("Nobody")
	myfile.close()

	myfile = open('3_Fifa.txt', 'w')
	myfile.write("0")
	myfile.close()
	
	myfile = open('3_Name_Fifa.txt', 'w')
	myfile.write("Nobody")
	myfile.close()
	
	myfile = open('4_Fifa.txt', 'w')
	myfile.write("0")
	myfile.close()
	
	myfile = open('4_Name_Fifa.txt', 'w')
	myfile.write("Nobody")
	myfile.close()
	
	myfile = open('5_Fifa.txt', 'w')
	myfile.write("0")
	myfile.close()
	
	myfile = open('5_Name_Fifa.txt', 'w')
	myfile.write("Nobody")
	myfile.close()

def AllReset():
	fifaReset()
	prezReset()		
