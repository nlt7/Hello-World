class Person():
    
    def __init__(self, myName, mySurname, myStudentnumber, myCourse):
        
        self.name = myName
        self.surename = mySurname                  
        self.studentnumber = myStudentnumber
        self.course = myCourse

    def showdetails(self):
        
        print(self, name, surename, studentnumber, course)
        
    def printinfo(self):

        print("My name is "+self.name)
        print("My surename "+self.surename)
        print("My studentnumber "+self.studentnumber)
        print("My course is "+self.course)
        
    def setName(self, myName):
        self.name = myName
        
    def setSurname(self, mySurname):
        self.surename = mySurname

    def setStudentnumber(self, myStudentnumber):
        self.studentnumber = myStudentnumber

    def setCourse(self, myCourse):
        self.course = myCourse

    def getName(self):
        return self.name
    
    def getSurname(self):
        return self.surname

    def getStudentnumber(self):
        return self.studentnumber

    def getCourse(self):
        return self.course

student = Person("mike", "smith", "324561789", "history")
student.printinfo()

print("I study"+ student.getCourse())

student.setName("joe")
student.printinfo()
