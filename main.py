from implementation.fibonacci import fibonacci
from implementation.primenumber import primenumber
from implementation.amstrong import amstrong
try:
    print("1: fibonacci \n2: primenumber\n3: amstrong")
    choice = int(input("Enter your choice"))
    while choice not in range(1,4):
        print("incorrect choice\n")
        print("1: fibonacci \n2: primenumber\n3: amstrong")
        choice = int(input("enter your choice"))

    if choice == 1:
        f=fibonacci().run()
    elif choice == 2:
       p=primenumber().run()
    elif choice == 3:
        a=amstrong().run()
    
except Exception as ex:
    print("incorrect choice" ,ex)
