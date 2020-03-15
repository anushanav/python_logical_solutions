class Rectangle:
    #  length = 0
    #  breadth =0
    
    def __init__(self,length,breadth):
        self.length= length
        self.breadth = breadth
        
    def area(self):
        return self.length*self.breadth
        
    def perimeter(self):
        return 2*(self.length +self.breadth)
        
rectangle1= Rectangle(6,4)

x =rectangle1.area()
print(x)