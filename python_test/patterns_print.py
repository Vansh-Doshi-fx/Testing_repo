def printFirstTenNum():
    for i in range(1,11):
        print(i,end=" ")
        
def printStars(n):
    for i in range(n):
        for j in range(i):
            print("*", end=" ")
        print()

def validatePhoneNumber(phone_number):
    import re
    pattern = re.compile(r'^\+?1?\d{9,15}$')
    return bool(pattern.match(phone_number))