
class Student:
    roll_no = "FA17-BSCS-00XX"
    name = "Muzammil"



class Person(Student):
    # pass

    x = 5
    # roll_no = "XXXXXX" #Overriding the Student class roll_no

    def __init__(self, name, age):
        self.name = name
        self.age = age


    
    # print(Student.roll_no)


p1 = Person("Muzammil", 24)
print(p1.name)
print(p1.roll_no)



