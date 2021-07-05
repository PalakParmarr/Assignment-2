from implementation.fibonacci import fibonacci
from implementation.primenumber import primenumber
from implementation.amstrong import amstrong
print("1: fibonacci \n2: primenumber\n3: amstrong")
  
choise = int(input("Enter your choise"))
  
if choise == 1:
    
    f=fibonacci().run()
elif choise == 2:
    
    p=primenumber().run()
elif choise == 3:
    
    a=amstrong().run()
else:
    print("incorrect")