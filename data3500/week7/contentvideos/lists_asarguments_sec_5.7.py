# define a function which takes a list
def sum_all_values(lst):
    for i in range(len(lst)):
        lst[i] += 1
        
    tot = 0
    for l in lst:
        tot += l
    return tot

# call function
list_fun = [1,2,3,4,5]
total = sum_all_values(list_fun)
print("total: ", total)

print("total: ", list_fun)















# create function that takes an int
def changeInt(x):
    x = 99999999

# create function that takes a list
def changeList(lst):
    lst[0] = 99999999
    
# show that ints (and float and strings)
# are not changed in a function
# Lists can be changed in a function

value = 10
changeInt(value)
print("value: ", value)

lst = [1,2,3,4,5]
changeList(lst)
print("lst: ", lst)

# checkpoint activity
# create a list that stores 5 numbers (any numbers)
# define a function called avg_list
# which calculates the average of all the values
# in a list
# have the function return the average
# call the function to verify it works

def avg_list(lst):
    sum = 0
    for l in lst:
        sum += l
    return sum / len(lst)
    
print(avg_list([1,2,3,4,5]))
