# Concept of Inheritance 
# #############################___________________###################

# Single level Inheritence
# Multilevel Inheritence
# Multiple INheritence

class A:
    def feature_1(self):
        print("Feature 1 here ..")

    def feature_2(self):
        print("Feature 2 is working here ....")
        
class B(A):
    def feature_3(self):
        print("Feature 3 here ..")

    def feature_4(self):
        print("Feature 4 is working here ....")

class C(B):
    def feature_5(self):
        print("Feature 5 here ..")

    def feature_6(self):
        print("Feature 6 is working here ....")


        
        
# class C(A,B):
#     def feature_5(self):
#         print("Feature 5 here ..")

#     def feature_6(self):
#         print("Feature 6 is working here ....")


a1 = A()
b1 = B()
c1 = C()

a1.feature_1()
a1.feature_2()
b1.feature_3()
b1.feature_4()
b1.feature_1()
c1.feature_5()
c1.feature_6()
c1.feature_1()

