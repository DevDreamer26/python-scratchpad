class User:
    def __init__(self,name,age,gender):
        self.name = name
        self.age = age
        self.gender = gender
                
    def identity(self):
        print("User details :", self.name,self.gender,self.age)
        
user_1 = User("Bidyasagar",24,"male")

user_1.identity()        
