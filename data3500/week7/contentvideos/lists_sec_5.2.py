#lists
class_ages = [41, 54, 21, 22, 23, 20, 19]

# class_ages = [[41], [22, 21], [20, 23, 21, 22, 19]]

ages1 = 41
ages2 = 54
ages3 = 21

print(class_ages)

print(class_ages[0])
print(class_ages[1])
print(class_ages[2])
print(class_ages[3])
print(class_ages[4])

for age in class_ages:
    print("age: ", age)
    
    
    
    
favorite_colors = ["aggie blue", "fighting white", "navy", "red"]

for color in favorite_colors:
    print("color: ", color)
    for letter in color:
        print("letter: ", letter)

















name = "andy brim"

for letter in name:
    print("letter: ", letter)
    
print(name[0]) # prints a

print(name[-1])
print(name[8])









ages = [40, 27, 21, 22, 25, 42, 20, 21, 19]

total = 0
ct = 0
for age in ages:
    total += age
    ct += 1
avg = total / ct
print(total)
print(ct)
print(avg)


print( sum(ages) / len(ages))


prices = [148.1, 147.5, 146.25, 144.8, 145.5]


print("prices average: ", sum(prices) / len(prices))


three_day_avg = (prices[0] + prices[1] + prices[2]) / 3 
print("three_day_avg: ", three_day_avg)

three_day_avg = (prices[1] + prices[2] + prices[3]) / 3 
print("three_day_avg: ", three_day_avg)

three_day_avg = (prices[2] + prices[3] + prices[4]) / 3 
print("three_day_avg: ", three_day_avg)


