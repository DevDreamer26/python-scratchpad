class Computer:
        
    def __init__(self,cpu):
        self.cpu = cpu
            
    def configuration(self):
        print("Configuration is ", self.cpu)
                
comp1 = Computer("i5")
comp2 = Computer("i9")

# Computer.configuration(comp1)
# Computer.configuration(comp2)

comp1.configuration()
comp2.configuration()

# a = 5
# print(a.bit_length())


