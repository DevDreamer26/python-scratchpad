# Duck typing ..........

class PyCharm: 
    def execeute(self):
        print("Compiling")
        print("Running....")
        
class MyEditor:
    
    def execute(self):
        print("Spell check..@..$..%")
        print("Convention Check...#...#...#")
        print("Compiling...x...x...x...x")
        print("Running...........")
 

class Laptop:
    
    def code(self,ide):
        ide.execute()
        
        
        
ide = MyEditor()

lap1= Laptop()

lap1.code(ide)