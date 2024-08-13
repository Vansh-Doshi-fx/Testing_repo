def printFirstTenNum():
    for i in range(1,11):
        print(i,end=" ")
        
def printStars(n):
    for i in range(n):
        for j in range(i):
            print("*", end=" ")
        print()

from hello_india import print_hello_india

print_hello_india()