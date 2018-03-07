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

#Register A_Points_Fifa
myfile = open('A_Points_Fifa.txt', 'r')
af = myfile.read()
myfile.close()

#Register O_Points
myfile = open('O_Points_Fifa.txt', 'r')
of = myfile.read()
myfile.close()

#Register J_Points
myfile = open('J_Points_Fifa.txt', 'r')
jf = myfile.read()
myfile.close()

#Register V_Points
myfile = open('V_Points_Fifa.txt', 'r')
vf = myfile.read()
myfile.close()

#Register R_Points
myfile = open('R_Points_Fifa.txt', 'r')
rf = myfile.read()
myfile.close()

#turn string values into usable int values
R_points = int(r) + int(rf)
A_points = int(a) + int(af)
O_points = int(o) + int(of)
J_points = int(j) + int(jf)
V_points = int(v) + int(vf)

#loads the arrays for scoring
alist = [A_points, "Alexander"]
olist = [O_points, "Olivia"]
vlist = [V_points, "Vince"]
rlist = [R_points, "Rebecca"]
jlist = [J_points, "Jonathan"]

while True:
	
	#Special Effects
	print "Quiz Package 2.1.2(2018 Standard Edition)"
	print "By Alexander Greco" 
	
	#Lets the user read status, take a test or leave
	menu = raw_input("What do you want to do? (President test, Fifa Test, Read the leaderboard or Leave)")
	
	#Runs the President Test
	if menu == "President test":
		os.system("python President_Test.py")	
		os.system("clear")
	
	#Runs the Fifa Test
	if menu == "Fifa test":
		os.system("python Fifa_Test.py")
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
		print str(leaderboard2[-1][1]) + " -- " + str(leaderboard2[-1][0])
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
	
	#Quits program
	if menu == "Leave":
		break


