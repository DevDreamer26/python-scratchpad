class Student:
    
    
    school =  'Xyz'
    
    def __init__(self,m1,m2,m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3
        
    def avg(self):
        return (self.m1 + self.m2 + self.m3)/3
    
    #Accessors
    def get_m1(self):
        return self.m1
    
    # Mutators
    def set_m1(self,value):
        self.m1 = value
        
    # Work with class variable
    # def info(cls):
    #     return cls.school
    
    
    # Class method
    @classmethod
    def getSchool(cls):
        return cls.school
    
    # Static method
    @staticmethod
    def info():
        print('This is a student class ..  in abc module')
    
        
s1 = Student(34,67,54)
s2 = Student(78,56,62)


print(s1.get_m1())
print(s2.avg())
print(Student.getSchool())

# print(s1.info()) will return None