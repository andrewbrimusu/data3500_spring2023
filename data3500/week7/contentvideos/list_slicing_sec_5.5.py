# slicing operator
scores = [45, 39, 50, 49, 49, 44]

for i in range(1,5):
    print(scores[i])
    
scores_sliced = scores[1:5]

print(scores_sliced)

    
    
input("press enter")
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
# slice from beginning
print(scores[:4])

# slice to end
print(scores[2:])

# checkpoint activity
# create a list storing the ages of the individuals
# in your family (feel free to make them up)
# use the slice operator to pull out the first 3 values in the list
# use the slice operator to pull out the last 3 values in the list
# use the slice operator to pull out the second and third values
# in the list
ages = [39, 38, 14, 12, 10, 2]

print(ages[:3]) 
print(ages[3:])
print(ages[1:3])


name = "andy"
print("name: ", name)
print("name[::-1]: ", name[::-1])

name = "bob"
print(name == name[::-1])


def palindrome(strng):
    return strng == strng[::-1]
    
print(palindrome("racecar"))
print(palindrome("racecar2"))
print(palindrome("gohangasalamiimalasagnahog"))

print(palindrome("amanaplanacanalpanama"))
print(palindrome("ratsliveonnoevilstar"))