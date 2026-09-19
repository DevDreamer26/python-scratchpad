
# Class inside a class (inner class)


class Student:
    
    def __init__(self,name,roll_no):
        self.name = name 
        self.roll_no = roll_no
        self.lap = self.Laptop()
        
    def show(self):
        print(self.name,self.roll_no)
        self.lap.show()
        
        
    class Laptop:
        def __init__(self):
            self.cpu = 'i5'
            
        def show(self):
            print(self.cpu)
        
        
s1 = Student('Bidyasagar','22/172')
s2 = Student('Kim', '234')


# print(s1.name,s1.roll_no)
# print(s2.name,s2.roll_no)
        
s1.show()
s2.show()


lap1 = s1.lap
lap2 =s2.lap

# print(id(lap1))
# print(id(lap2))

# lap1 =Student.Laptop()