def printFirstTenNum():
    for i in range(1,11):
        print(i,end=" ")

def printStars(n):
    for i in range(n):
        for j in range(i):
            print("*", end=" ")
        print()

def printReverseStarPyramid(n):
    for i in range(n, 0, -1):
        for j in range(i):
            print("*", end=" ")
        print()

printReverseStarPyramid(10)