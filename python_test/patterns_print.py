def printFirstTenNum():
    for i in range(1,11):
        print(i,end=" ")
        
def printStars(n):
    for i in range(n):
        for j in range(i):
            print("*", end=" ")
        print()

def is_valid_phone_number(phone_number):
    pattern = re.compile(r'^\+?1?\d{10}$')
    return bool(pattern.match(phone_number))