from base import baserun
class primenumber(baserun):
    def run(self):
        self.n= int(input("enter a number"))
            
        if self.n <= 1:
            print(self.n, "is not a prime number")
        elif self.n==2:
            print(self.n, "is a prime number")
        else:
            for i in range(1, int(float(self.n/2)+1)):
                # If num is divisible by any number between
                # 2 and n / 2, it is not prime
                if (self.n % i) != 0:
                    print(self.n, "is not a prime number")
                    break
                else:
                    print(self.n, "is a prime number")
        
