def printFirstTenNum():
    for i in range(1,11):
        print(i,end=" ")
        
def printStars(n):
    for i in range(n):
        for j in range(i):
            print("*", end=" ")
        print()

import os

def create_joke_file(filename):
    joke = "Why don't scientists trust atoms? Because they make up everything!"
    with open(filename, 'w') as file:
        file.write(joke)

create_joke_file('joke.txt')