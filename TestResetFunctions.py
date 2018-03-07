#President Test Score Reset:
def aPrezReset():
	#Reset A_Points
	myfile = open('A_Points_Prez.txt', 'w')
	myfile.write("30")
	myfile.close()

def oPrezReset():	
	#Reset O_Points
	myfile = open('O_Points_Prez.txt', 'w')
	myfile.write("0")
	myfile.close()

def jPrezReset():	
	#Reset J_Points
	myfile = open('J_Points_Prez.txt', 'w')
	myfile.write("5")
	myfile.close()
	
def rPrezReset():	
	#Reset R_Points
	myfile = open('R_Points_Prez.txt', 'w')
	myfile.write("18")
	myfile.close()
	
def vPrezReset():	
	#Reset V_Points
	myfile = open('V_Points_Prez.txt', 'w')
	myfile.write("14")
	myfile.close()

def prezReset(): 
	aPrezReset()
	oPrezReset()
	jPrezReset()
	rPrezReset()
	vPrezReset()
	
#Fifa Test Score Reset:
def aFifaReset():
	#Reset A_Points_Fifa
	myfile = open('A_Points_Fifa.txt', 'w')
	myfile.write("0")
	myfile.close()
	
def oFifaReset():	
	#Reset O_Points_Fifa
	myfile = open('O_Points_Fifa.txt', 'w')
	myfile.write("0")
	myfile.close()
	
def jFifaReset():
	#Reset J_Points_Fifa
	myfile = open('J_Points_Fifa.txt', 'w')
	myfile.write("0")
	myfile.close()

def rFifaReset():	
	#Reset R_Points_Fifa
	myfile = open('R_Points_Fifa.txt', 'w')
	myfile.write("0")
	myfile.close()
	
def vFifaReset():	
	#Reset V_Points_Fifa
	myfile = open('V_Points_Fifa.txt', 'w')
	myfile.write("0")
	myfile.close()

def fifaReset():
	aFifaReset()
	oFifaReset()
	jFifaReset()
	rFifaReset()
	vFifaReset()
def allReset():
	fifaReset()
	prezReset()
def aAllReset():
	aFifaReset()
	aPrezReset()
def jAllReset():
	jFifaReset()
	jPrezReset()
def oAllReset():
	oFifaReset()
	oPrezReset()
def rAllReset():
	rFifaReset()
	rPrezReset()	
def vAllReset():
	vFifaReset()
	vPrezReset()		
