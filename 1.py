numberone = 1
ageofqueen = 78

# define some functions
def printhello():
    print "hello"
    
def timesfour(input):
    print input * 4
    
# define a class
class Piano:
    def __init__(self):
        self.type = raw_input("What type of piano? ")
        self.height = raw_input("What height (in feet)? ")
        self.price = raw_input("How much did it cost? ")
        self.age = raw_input("How old is it (in years)? ")
	
    def printdetails(self):
        print "This piano is a/an " + self.height + " foot",
        print self.type, "piano, " + self.age, "years old and costing\
 " + self.price + " dollars."
	
	
Result <- c(0.5,0.4,0.45,0.6,0.6,0.55,0.55,0.65,0.7,0.4,0.44,0.88,0.54,0.44,0.41,0.49,0.61,0.32,0.41,0.3,0.66,0.4,0.32,0.21,0.27,0.6,0.44,0.5,0.44,0.56,0.66,0.32,0.59,0.68,0.77,0.68,0.4,0.69,0.66,0.7,0.5,0.48)
Total <- c(68,61,66,77,75,68,66,79,71,60,64.5,90.5,68,66.5,66,69.6,75,64,63,58.5,70.5,64,52.5,49,61,76,65.5,69,54,69,75,59,75,79,81,79.5,60.5,77,70,75,68,64)
GHR <- c(14,17.5,16,21,19,13,16,20,18,11,17.5,22,13,17,17,17,18,14,12,13,20,17,14.5,10,8,19,17.5,18,16,14,18.5,13,18.5,19,21,19,8,18,19,19,16,15)

