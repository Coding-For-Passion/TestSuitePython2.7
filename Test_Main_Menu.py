#Import
import os

#Set window size and get rid of Script Terminal Auto-Prints
os.system('clear')
raw_input("type anything to start: ")
os.system('clear')

while True:
	
	#Special Effects
	print "Quiz Package 2.1.2(2018 Standard Edition)"
	print "By Alexander Greco" 
	
	#Lets the user read status, take a test or leave
	menu = raw_input("What do you want to do? (President test, Fifa Test, or Leave)")
	
	#Runs the President Test
	if menu == "President test":
		os.system("python Prez/President_Test.py")	
		os.system("clear")
	
	#Runs the Fifa Test
	if menu == "Fifa test":
		os.system("python Fifa/Fifa_Test.py")
		os.system('clear')
	
	#Quits program
	if menu == "Leave":
		break


