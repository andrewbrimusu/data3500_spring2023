def add2nums(num1, num2):
    #write something
    return num1 + num2

def mult2nums(num1, num2):
    total = 0 
    for i in range(num2):
        total = add2nums(total, num1)
    return total
    
def exponent(num1, num2):
    total = 1
    for i in range(num2):
        total = mult2nums(total, num1)
    return total
    
        
print(1024 ** 256)

print("------------")

print(exponent(1024,256))

