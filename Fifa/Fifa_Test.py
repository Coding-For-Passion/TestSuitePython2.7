# Copyright (c) 2018 Alexander Greco All Rights Reserved.

# Import
import os

# Set window size and get rid of Script Terminal Auto-Prints
os.system('clear')
raw_input("type anything to start: ")
os.system('clear')

# Register stored Leaderboard
myfile = open('1_Fifa.txt', 'r')
a = myfile.read()
myfile.close()

myfile = open('2_Fifa.txt', 'r')
b = myfile.read()
myfile.close()

myfile = open('3_Fifa.txt', 'r')
c = myfile.read()
myfile.close()

myfile = open('4_Fifa.txt', 'r')
d = myfile.read()
myfile.close()

myfile = open('5_Fifa.txt', 'r')
e = myfile.read()
myfile.close()

myfile = open('1_Name_Fifa.txt', 'r')
aa = myfile.read()
myfile.close()

myfile = open('2_Name_Fifa.txt', 'r')
bb = myfile.read()
myfile.close()

myfile = open('3_Name_Fifa.txt', 'r')
cc = myfile.read()
myfile.close()

myfile = open('4_Name_Fifa.txt', 'r')
dd = myfile.read()
myfile.close()

myfile = open('5_Name_Fifa.txt', 'r')
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

# Array that stores the teams who won the Fifa World Cup in order
teams = [
"Uraguay",
"Italy",
"Italy",
"Uraguay",
"Germany",
"Brazil",
"Brazil",
"England",
"Brazil",
"Germany",
"Argentina",
"Italy",
"Argentina",
"Germany",
"Brazil",
"France",
"Brazil",
"Italy",
"Spain",
"Germany"
]

# Main Program

while True:

	# Special Effects
	print "Fifa Quiz 1.1.0(2018 Standard Edition)"
	print "By Alexander Greco"

	# Lets the user read status or take the test
	menu = raw_input("What do you want to do? (Take the test, Study, Repitition, Read the leaderboard or Leave)")

	# If the user would like to test themself
	if menu == "Take the test":
		name = raw_input("Name: ")
		# test setting reset
		points = 0
		i = 20;

		# loops through all the teams
		while i > 0:
			QA = raw_input("Who won the " + str(i) + " Fifa World Cup?")
			if QA == teams[i-1]:
				print "Correct!"
				points = points + 1
			else:
				print "WRONG!!!"
				print teams[i-1]
			i = i - 1

		# Scoring

		# Fraction
		print str(points) + "/20"

		# Percent
		percent1 = float(points)/20.0
		percent2 = int((percent1 * 100)+0.5)
		print str(percent2) + "%"

		# Letter grade and funny comment
'''		if points >= 15:
			print "A+"
			print "You are a Genius, or maybe just a cheater."
		elif points >= 13:
			print "A"
			print "You are a Super Star, or did you have a peek for a few?"
		elif points >= 11:
			print "B+"
			print "Awesome Job! You beat the Creater!"
		elif points >= 9:
			print "B"
			print "Great Job!"
		elif points >= 7:
			print "C+"
			print "You did pretty well!"
		elif points >= 5:
			print "C"
			print "You are starting to get the hang of this!"
		elif points >= 3:
			print "D+"
			print "Go Study and you could get a good score!"
		elif points >= 2:
			print "D"
			print "What kind of football do you think this is?"
		elif points >= 0:
			print "F"
			print "What are you, a rock?" '''

		# Update Leaderboard

		if first < points:
			first = points
			myfile = open('1_Fifa.txt', 'w')
			myfile.write(str(first))
			myfile.close()
			first_list[0] = name
			print "You got 1st place!"
		elif second < points:
			second = points
			myfile = open('2_Fifa.txt', 'w')
			myfile.write(str(second))
			myfile.close()
			second_list[0] = name
			print "You got 2nd place!"
		elif third < points:
			third = points
			myfile = open('3_Fifa.txt', 'w')
			myfile.write(str(third))
			myfile.close()
			third_list[0] = name
			print "You got 3rd place!"
		elif fourth < points:
			fourth = points
			myfile = open('4_Fifa.txt', 'w')
			myfile.write(str(fourth))
			myfile.close()
			ffourth_list[0] = name
			print "You got 4th place!"
		elif fifth < points:
			fifth = points
			myfile = open('5_Fifa.txt', 'w')
			myfile.write(str(fifth))
			myfile.close()
			fifth_list[0] = name
			print "You got 5th place!"
	# Lets the user choose when to clear screen and go back to menu
		raw_input("Press anything to continue: ")
		os.system('clear')
	#Same as the regular test, but it doesn't move to the next team if you are wrong and doesn't give the right answer if you are wrong
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
			QA = raw_input("Who won the " + str(i) + " Fifa World Cup?")
			if QA == team[i-1]:
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
			if ggez == "yes":
				target = raw_input("What is your Goal?(How many teams you would like to get correct in this session) ")
				try:
					target = int(target)
					if target < 21:
						if target > 0:
							break
						else:
							if target == 0:
								print "What kind of goal is 0?"
							else:
								print "You can't have a negative goal, Silly!"
					else:
						print "There aren't that many teams, pick an integer value between 1 and 20"
					raw_input("Press anything to continue")
				except ValueError:
					print "Pick a integer, Dumbo!"
					raw_input("Press anything to continue")

			if ggez == "Yes":
				target = raw_input("What is your Goal? (How many teams you would like to get correct in this session) ")
				try:
					target = int(target)
					if target < 21:
						if target > 0:
							break
						else:
							if target == 0:
								print "What kind of goal is 0?"
							else:
								print "You can't have a negative goal, Silly!"
					else:
						print "There are not that many teams, pick a value between 1 and 20"
					raw_input("Press anything to continue")

				except ValueError:
					print "Pick a integer, Dumbo!"
					raw_input("Press anything to continue")
		os.system("clear")
		while True:
			points = 0
			i = 20;
			while i > 0:
				QA = raw_input("Who won the " + str(i) + " Fifa World Cup?")
				if QA == teams[i-1]:
					print "Correct!"
					points = points + 1
				else:
					print "WRONG!!!"
					print teams[i-1]
				i = i - 1
			print str(points) + "/20"
			if int(target) > points:
				raw_input("Try Again :(")
			else:
				print "Success!!!"
				break
		raw_input("Press anything to continue: ")
		os.system('clear')

	#Shows leaderboard
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

	# Saves current Leaderboard and quits program
	if menu == "Leave":

		myfile = open('1_Fifa.txt', 'w')
		myfile.write(str(first))
		myfile.close()

		myfile = open('2_Fifa.txt', 'w')
		myfile.write(str(second))
		myfile.close()

		myfile = open('3_Fifa.txt', 'w')
		myfile.write(str(third))
		myfile.close()

		myfile = open('4_Fifa.txt', 'w')
		myfile.write(str(fourth))
		myfile.close()

		myfile = open('5_Fifa.txt', 'w')
		myfile.write(str(fifth))
		myfile.close()

		myfile = open('1_Name_Fifa.txt', 'w')
		myfile.write(str(first))
		myfile.close()

		myfile = open('2_Name_Fifa.txt', 'w')
		myfile.write(str(second))
		myfile.close()

		myfile = open('3_Name_Fifa.txt', 'w')
		myfile.write(str(third))
		myfile.close()

		myfile = open('4_Name_Fifa.txt', 'w')
		myfile.write(str(fourth))
		myfile.close()

		myfile = open('5_Name_Fifa.txt', 'w')
		myfile.write(str(fifth))
		myfile.close()

		break
