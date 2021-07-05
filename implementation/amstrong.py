from base import baserun
class amstrong(baserun):
    def run(self):
         if self.n < 0:
            print("Incorrect input")
         elif self.n == 0:
            return 0
         elif self.n == 1 or self.n == 2:
            return 1
         else:
            return run(self.n-1) + run(self.n-2)
    
