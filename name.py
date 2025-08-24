class Name:
    def boys(self,x):
        self.x=x
    def girls(self,y):
        self.y=y
    def show_boys(self):
        print(self.x)
    def show_girls(self):
        print(self.y)

i=Name()
i.boys("David")
i.girls("Reeta")
i.show_boys()
i.show_girls()