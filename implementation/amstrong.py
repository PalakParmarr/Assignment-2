from base import baserun
class amstrong(baserun):
    def run(self):
      self.n=int(input("enter number"))
 
      sum = 0  
      t = self.n 

      while t > 0:  
         sum = sum+((t % 10) ** 3)   
         t //= 10  

      if self.n == sum:  
         print(self.n,"is an Armstrong number")  
      else:  
         print(self.n,"is not an Armstrong number")  