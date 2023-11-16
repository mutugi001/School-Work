# Collins Mutugi Wachira
# SCT211-0051/2022
class Calc:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
        
    def add(self):
        sum= self.num1 + self.num2
        print(sum)
    
    def subtract(self):
        diff = self.num1 - self.num2
        print(diff)
    
    def div(self):
        try:
            div = self.num1/self.num2
            print(div)
        except ZeroDivisionError as  Z:
            print("Division by zero error!!!")
    
    def multiply(self):
        prod = self.num1 * self.num2
        print(prod)
    
    
x = Calc(2,0)
y = Calc(10,5)
x.add()
x.subtract()
x.div()
x.multiply() 
y.add()
y.subtract()
y.div()
y.multiply()