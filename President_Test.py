#Import
import os

#Set window size and get rid of Script Terminal Auto-Prints
os.system('clear')
raw_input("type anything to start: ")
os.system('clear')

#Register A_Points
myfile = open('A_Points_Prez.txt', 'r')
a = myfile.read()
myfile.close()

#Register O_Points
myfile = open('O_Points_Prez.txt', 'r')
o = myfile.read()
myfile.close()

#Register J_Points
myfile = open('J_Points_Prez.txt', 'r')
j = myfile.read()
myfile.close()

#Register V_Points
myfile = open('V_Points_Prez.txt', 'r')
v = myfile.read()
myfile.close()

#Register R_Points
myfile = open('R_Points_Prez.txt', 'r')
r = myfile.read()
myfile.close()

#turn string values into usable int values
R_points = int(r)
A_points = int(a)
O_points = int(o)
J_points = int(j)
V_points = int(v)

#loads the arrays for scoring
alist = [A_points, "Alexander"]
olist = [O_points, "Olivia"]
vlist = [V_points, "Vince"]
rlist = [R_points, "Rebecca"]
jlist = [J_points, "Jonathan"]

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
		
		#Tests the individuals separately so they can have there own scores
		
		if name == "Olivia" or "Alexander" or "Jonathan" or "Rebecca" or "Vince":
			while True:
				ggez = raw_input("Are you ready? ")
				if ggez == "yes" or "Yes":
					break
			
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
			if points >= 40:
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
				print "What are you, a rock?"
			
			#Lets the user choose when to clear screen and go back to menu
			raw_input("Press anything to continue: ")
			os.system('clear')
			
			#Update scores
			if name == "Alexander":
				if A_points < points:
					A_points = points
					myfile = open('A_Points.txt', 'w')
					myfile.write(str(A_points))
					myfile.close()
			elif name == "Olivia":
				if O_points < points:
					O_points = points
					myfile = open('O_Points.txt', 'w')
					myfile.write(str(O_points))
					myfile.close()
			elif name == "Jonathan":
				if J_points < points:
					J_points = points	
					myfile = open('J_Points.txt', 'w')
					myfile.write(str(J_points))
					myfile.close()
			elif name == "Vince":
				if V_points < points:
					V_points = points
					myfile = open('V_Points.txt', 'w')
					myfile.write(str(V_points))
					myfile.close()
			elif name == "Rebecca":
				if R_points < points:
					R_points = points	
					myfile = open('R_Points.txt', 'w')
					myfile.write(str(R_points))
					myfile.close()
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
		alist = [A_points, "Alexander"]
		olist = [O_points, "Olivia"]
		vlist = [V_points, "Vince"]
		rlist = [R_points, "Rebecca"]
		jlist = [J_points, "Jonathan"]
		#Combine the stats
		leaderboard = [alist,
		olist,
		jlist, vlist,
		 rlist]
		#Order the stats
		leaderboard2 = sorted(leaderboard)
		#Print out the stats([-*] goes backwards in the stats because it is in asending order)
		print "1. "
		print str(leaderboard2[-1][1]) + " -- " + strleaderboard2[-1][0])
		print "2. "
		print str(leaderboard2[-2][1]) + " -- " + str(leaderboard2[-2][0])
		print "3. "
		print str(leaderboard2[-3][1]) + " -- " + str(leaderboard2[-3][0])
		print "4. "
		print str(leaderboard2[-4][1]) + " -- " + str(leaderboard2[-4][0])
		print "5. "
		print str(leaderboard2[-5][1]) + " -- " + str(leaderboard2[-5][0])
		#Moves on when user is ready
		raw_input("Press anything to continue: ")
		os.system('clear')
	
	#Saves current scores and quits program
	if menu == "Leave":
		
		myfile = open('A_Points_Prez.txt', 'w')
		myfile.write(str(A_points))
		myfile.close()

		myfile = open('O_Points_Prez.txt', 'w')
		myfile.write(str(O_points))
		myfile.close()

		myfile = open('J_Points_Prez.txt', 'w')
		myfile.write(str(J_points))
		myfile.close()

		myfile = open('V_Points_Prez.txt', 'w')
		myfile.write(str(V_points))
		myfile.close()

		myfile = open('R_Points_Prez.txt', 'w')
		myfile.write(str(R_points))
		myfile.close()
		
		break
