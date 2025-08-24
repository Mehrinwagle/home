class Two:
    def get_data(self,a,b):
        self.a=a
        self.b=b
    def display_data(self):
        print(self.b)
    def dis_index_data(self):
        print(b[dis])
        

a=Two()
b=[]
enter=int(input("enter how many times you want to enter in list: "))
for i in range(enter):
    name=input("enter name: ")
    b.append(name)
dis=int(input("enter which index data you want to know : "))
a.get_data(name,b)
a.display_data()
a.dis_index_data()
