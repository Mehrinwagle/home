class Student:
    def __init__(self,name,roll_no,marks,a):
        self.name=name
        self.roll_no=roll_no
        self.marks=marks
        self.a=a
    def display(self):
        print("Here is your output:")
    def dis_list(self):
        print(self.a)
    def details(self):
        print("Name :",self.name)
        print("Roll No :",self.roll_no)
        print("Marks :",self.marks)
        if marks >= 40:
            print("Result : Pass")
        else:
            print("Result : Fail")

a=[]
enter=int(input("enter number of students : "))
for i in range(enter):
    name=input("enter name: ")
    roll_no = int(input("Enter Roll Number: "))
    marks = int(input("Enter Marks: "))
    a.append([name,roll_no,marks])


t=Student(name,roll_no,marks,a)
t.display()
t.dis_list()
t.details()