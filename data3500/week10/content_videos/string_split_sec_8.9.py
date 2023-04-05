# split
data_str = "1,2,3,4,5,6"
lst = data_str.split(",")
print("data_str: ", data_str)
print("lst: ", lst)

# join
new_str = ",".join(lst)
print("new_str: ", new_str)


new_str = ";".join(lst)
print("new_str: ", new_str)

# join with list comprehension
lst = []
for i in range(1,101):
    lst.append(str(i))
    
print(lst)

print(",".join(lst))

str_lst = ",".join([str(i) for i in range(1,101) ])

print("str_lst: ", str_lst)





# checkpoint activity
# Start with a string "1 2 3 4 5 6 7 8 9 10"
# split the string into a list
# Using a list comprehension convert the list 
# from a list of strings to a list of ints













# solution
string = "1 2 3 4 5 6 7 8 9 10"
lst = string.split(" ")
ints = [int(i) for i in lst]
print("ints: ", ints)

# Could you do that all on one line?
# sure...
print([int(i) for i in "1 2 3 4 5 6 7 8 9 10".split(" ")])