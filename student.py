class Student:
    def __init__(self,name,roll_no,marks):
        self.name=name
        self.roll_no=roll_no
        self.marks=marks
    def details(self):
        print("Name",self.name)
        print("Roll No:", self.roll_no)
        print("Marks:", self.marks)


name=input("Enter Student Name: ")
roll_no = int(input("Enter Roll Number: "))
marks = int(input("Enter Marks: "))
if marks >= 40:
    print("Result: Pass")
else:
    print("Result: Fail")
t=Student(name,roll_no,marks)
t.details()

