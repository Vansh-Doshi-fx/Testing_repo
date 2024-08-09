```python
from create import print_reverse_star_pyramid

def printFirstTenNum():
    for i in range(1,11):
        print(i,end=" ")
        
def printStars(n):
    for i in range(n):
        for j in range(i):
            print("*", end=" ")
        print()

if __name__ == "__main__":
    print_reverse_star_pyramid(10)
```