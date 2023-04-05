# rounds down
print(-5 // 2) # 
print(5 // 2) # 



#dynamic typing
# var = 2
# for i in range(2, 20):
#     var = var ** i
#     print(var,"---")
    
input("pause")
    

print("andy" + "brim")
print("twenty" + "20")

age = 39

if age > 30:
    print("you are old")
    
# while age > 30:
#     print("you are old") # logic error, needs something to end the loop
    
for i in range(1,6):
    print(i, ",", i+10, sep="", end="\n")
    
    
    
    
    
print()
print(1,2,3,4,5,sep=",")
    
# 4 parts to a function: name, parameter list, logic, return statement
def sum(one, two, three): # name and parameter list
    tot = one + two + three # logic
    return tot # return statement

    
print(sum(1,2,3))
print(sum("andrew", "william", "brim"))
print(sum([1,2,3], [2,3,4], [3,4,5]))


# palindrome in Python

string = "racecar"
if string == string[::-1]:
    print("palindrome")
    
def isPalindrome(strn):
    return strn == strn[::-1]
    
print(isPalindrome("racecar"))
print(isPalindrome("amanaplanacanalpanama"))
print(isPalindrome("ilovethisguy"))


lst = [1,2,3,4,5]
print(lst[1:4]) # start idx 1, end idx 3

lst.insert(2, 1000000)

len(lst)


print(lst)

thisdict = {}
thisdict["brand"] = "Ford"
thisdict["model"] = "Mustang"
thisdict["year"] = 1964
thisdict["color"] = "red"

# thisdict.append(5)
     
for i in range(1,101):
    if i != 100:
        print(7*i, end=",")
    else:
        print(7*i)
        
def avg(lst):
    tot = 0
    for num in lst:
        tot += num
    avg = tot / len(lst)
    return avg
    
print(avg([1,2,3,4,5]))

        

    
    

