class students:
    def __init__(self, name, rollnum):
        self.name = name
        self.rollnum = rollnum
        
    def set_age(self,age):
        self.age = age
        
    def set_marks(self,marks):
        self.marks = marks
        
    def display(self):
        print (self.name,self.rollnum,self.set_age,self.set_marks)
        
s1 = students("Anusha",19)
s1.set_age = 20
s1.set_marks = 98
s1.display()