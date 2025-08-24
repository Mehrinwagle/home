class Employee:
    def __init__(self,name,age,salary,gender):
        self.name=name
        self.age=age
        self.salary=salary
        self.gender=gender
    def emp_details(self):
        print("name: ",self.name)
        print("age: ",self.age)
        print("salary: ",self.salary)
        print("gender: ",self.gender)


name=input("Enter Name: ")
age=int(input("Enter age: "))
salary=int(input("Enter salary: "))
gender=input("Enter gender: ")
c=Employee( name , age , salary , gender )
c.emp_details()