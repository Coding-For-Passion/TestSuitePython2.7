#Import
import os

#Set window size and get rid of Script Terminal Auto-Prints
os.system('clear')
raw_input("type anything to start: ")
os.system('clear')

# Register stored Leaderboard
myfile = open('1_Prez.txt', 'r')
a = myfile.read()
myfile.close()

myfile = open('2_Prez.txt', 'r')
b = myfile.read()
myfile.close()

myfile = open('3_Prez.txt', 'r')
c = myfile.read()
myfile.close()

myfile = open('4_Prez.txt', 'r')
d = myfile.read()
myfile.close()

myfile = open('5_Prez.txt', 'r')
e = myfile.read()
myfile.close()

myfile = open('1_Name_Prez.txt', 'r')
aa = myfile.read()
myfile.close()

myfile = open('2_Name_Prez.txt', 'r')
bb = myfile.read()
myfile.close()

myfile = open('3_Name_Prez.txt', 'r')
cc = myfile.read()
myfile.close()

myfile = open('4_Name_Prez.txt', 'r')
dd = myfile.read()
myfile.close()

myfile = open('5_Name_Prez.txt', 'r')
ee = myfile.read()
myfile.close()
#turn string values into usable int values
first = int(a)
second = int(b)
third = int(c)
fourth = int(d)
fifth = int(e)

# loads the arrays for Leaderboard
first_list = [aa, first]
second_list = [bb, second]
third_list = [cc, third]
fourth_list = [dd, fourth]
fifth_list = [ee, fifth]

#Array that stores U.S. president's names in order
presidents = [
"George Washington",
"John Adams",
"Thomas Jefferson",
"James Madison",
"James Monroe",
"John Adams",
"Andrew Jackson",
"Martin Van Buren",
"William Harrison",
"John Tyler",
"James Polk",
"Zachary Taylor",
"Millard Fillmore",
"Franklin Pierce",
"James Buchanan",
"Abraham Lincoln",
"Andrew Johnson",
"Ulysses Grant",
"Ruthford Hayes",
"James Garfield",
"Chester Arthur",
"Grover Cleveland",
"Benjamin Harrison",
"Grover Cleveland",
"William McKinley",
"Theodore Roosevelt",
"William Taft",
"Woodrow Wilson",
"Warren Harding",
"Calvin Coolidge",
"Herbert Hoover",
"Franklin Roosevelt",
"Harry Truman",
"Dwight Eisenhower",
"John Kennedy",
"Lyndon Johnson",
"Richard Nixon",
"Gerald Ford",
"Jimmy Carter",
"Ronald Reagan",
"George Bush",
"Bill Clinton",
"George Bush",
"Barack Obama",
"Donald Trump"
]

#Main Program
while True:
	
	#Special Effects
	print "President Quiz 4.5.2(2018 Standard Edition)"
	print "By Alexander Greco" 
	
	#Lets the user read status or take the test
	menu = raw_input("What do you want to do? (Take the test, Study, Repitition, Read the leaderboard or Leave)")
	
	#If the user would like to test themself
	if menu == "Take the test":
		name = raw_input("Please enter your name: ")
			
		#test setting reset
		points = 0
		i = 45;
			
		#loops through all the presidents
		while i > 0:
			QA = raw_input("Who is the " + str(i) + " President?")
			if QA == presidents[i-1]:
				print "Correct!"
				points = points + 1
			else:
				print "WRONG!!!"	
				print presidents[i-1]
			i = i - 1
			
		#Scoring
			
		#Fraction
		print str(points) + "/45"
			
		#Percent
		percent1 = float(points)/45.0
		percent2 = int((percent1 * 100)+0.5)
		print str(percent2) + "%"
			
		#Letter grade and funny comment
'''		if points >= 40:
			print "A+"
			print "You are a Genius, or maybe just a cheater."
		elif points >= 35:
			print "A"
			print "You are a Super Star, or did you have a peek for a few?"
		elif points >= 30:
			print "B+"
			print "Awesome Job! You beat the Creater!"
		elif points >= 25:
			print "B"
			print "Great Job!"
		elif points >= 20:
			print "C+"
			print "You did pretty well!"
		elif points >= 15:
			print "C"
			print "You are starting to get the hang of this!"
		elif points >= 10:
			print "D+"
			print "Slightly Smarter than the average American"
		elif points >= 5:
			print "D"
			print "You are an average American, try studying who the leaders of your own country were instead of watching TV!"
		elif points >= 0:
			print "F"
			print "What are you, a rock?" '''
			
		#Lets the user choose when to clear screen and go back to menu
		raw_input("Press anything to continue: ")
		os.system('clear')
		
		#Update scores
		if first < points:
			first = points
			myfile = open('1_Prez.txt', 'w')
			myfile.write(str(first))
			myfile.close()
			first_list[0] = name
			print "You got 1st place!"
		elif second < points:
			second = points
			myfile = open('2_Prez.txt', 'w')
			myfile.write(str(second))
			myfile.close()
			second_list[0] = name
			print "You got 2nd place!"
		elif third < points:
			third = points
			myfile = open('3_Prez.txt', 'w')
			myfile.write(str(third))
			myfile.close()
			third_list[0] = name
			print "You got 3rd place!"
		elif fourth < points:
			fourth = points
			myfile = open('4_Prez.txt', 'w')
			myfile.write(str(fourth))
			myfile.close()
			ffourth_list[0] = name
			print "You got 4th place!"
		elif fifth < points:
			fifth = points
			myfile = open('5_Prez.txt', 'w')
			myfile.write(str(fifth))
			myfile.close()
			fifth_list[0] = name
			print "You got 5th place!"
	#Same as the regular test, but it doesn't move to the next president if you are wrong and doesn't give the right answer if you are wrong
	#Also doesn't affect leaderboard 
	if menu == "Repetition":
		while True:
			ggez = raw_input("Are you ready? ")
			if ggez == "yes":
				break
			if ggez== "Yes":
				break
		points = 0
		i = 45;
		while i > 0:
			QA = raw_input("Who is the " + str(i) + " President?")
			if QA == presidents[i-1]:
				print "Correct!"
				i = i - 1
			else:
				print "WRONG!!!"	
	
		os.system('clear')
	
	#Same as the regular test, but it loops back through the test if the user do not reach a user set goal
	#Also doesn't affect leaderboard 
	if menu == "Study":
		
		while True:
			os.system("clear")
			ggez = raw_input("Are you ready? ")
			#Sets a goal based on user input and confirms it is int type
			if ggez == "yes" or ggez == "Yes" :
				target = raw_input("What is your Goal?(How many presidents you would like to get correct in this session) ")
				try:
					target = int(target)
					if target < 46:
						if target > 0: 
							break	
						else:
							if target == 0: 
								print "What kind of goal is 0?"
							else:	
								print "You can't have a negative goal, Silly!"
					else:
						print "There aren't that many teams, pick an integer value between 1 and 45"	
					raw_input("Press anything to continue")
				except ValueError:
					print "Pick a integer, Dumbo!"
					raw_input("Press anything to continue")
		os.system("clear")	

		while True:
			points = 0
			i = 45;
			while i > 0:
				QA = raw_input("Who is the " + str(i) + " President?")
				if QA == presidents[i-1]:
					print "Correct!"
					points = points + 1
				else:
					print "WRONG!!!"	
					print presidents[i-1]
				i = i - 1
			print str(points) + "/45"
			if int(target) > points:
				raw_input("Try Again :(")
			else:
				print "Success!!!"
				break
		raw_input("Press anything to continue: ")
		os.system('clear')
	
	#Shows all of the scores in order
	if menu == "Read the leaderboard": #Set the stats
		first_list[1] = [first]
		second_list[1] = [second]
		third_list[1] = [third]
		fourth_list[1] = [fourth]
		fifth_list[1] = [fifth]

		#Combine the Leaderboard
		leaderboard = [first_list,
		second_list,
		third_list, fourth_list,
		 fifth_list]

		#Print out the Leaderboard
		print "1. " + str(leaderboard[0][0]) + " -- " + str(leaderboard[0][1])
		print "2. " + str(leaderboard[1][0]) + " -- " + str(leaderboard[1][1])
		print "3. " + str(leaderboard[2][0]) + " -- " + str(leaderboard[2][1])
		print "4. " + str(leaderboard[3][0]) + " -- " + str(leaderboard[3][1])
		print "5. " + str(leaderboard[4][0]) + " -- " + str(leaderboard[4][1])
		#Moves on when user is ready
		raw_input("Press anything to continue: ")
		os.system('clear')
	
	#Saves current scores and quits program
	if menu == "Leave":

		myfile = open('1_Prez.txt', 'w')
		myfile.write(str(first))
		myfile.close()

		myfile = open('2_Prez.txt', 'w')
		myfile.write(str(second))
		myfile.close()

		myfile = open('3_Prez.txt', 'w')
		myfile.write(str(third))
		myfile.close()

		myfile = open('4_Prez.txt', 'w')
		myfile.write(str(fourth))
		myfile.close()

		myfile = open('5_Prez.txt', 'w')
		myfile.write(str(fifth))
		myfile.close()

		myfile = open('1_Name_Prez.txt', 'w')
		myfile.write(str(first))
		myfile.close()

		myfile = open('2_Name_Prez.txt', 'w')
		myfile.write(str(second))
		myfile.close()

		myfile = open('3_Name_Prez.txt', 'w')
		myfile.write(str(third))
		myfile.close()

		myfile = open('4_Name_Prez.txt', 'w')
		myfile.write(str(fourth))
		myfile.close()

		myfile = open('5_Name_Prez.txt', 'w')
		myfile.write(str(fifth))
		myfile.close()
		break
