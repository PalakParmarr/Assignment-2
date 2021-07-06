from base import baserun
import base
class fibonacci(baserun):
    
    def run(self):
        self.n= int(input("enter a number"))
        a = 0
        b = 1
        
        if self.n == 0:
            print(0)
        elif self.n == 1:
            print(1)
        else:
            for i in range(2, self.n):
                c = a + b
                a = b
                b = c
            print(b)
     
        