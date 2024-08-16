def printFirstTenNum():
    for i in range(1,11):
        print(i,end=" ")
        
def printStars(n):
    for i in range(n):
        for j in range(i):
            print("*", end=" ")
        print()

from star_pattern_generator import print_star_pattern