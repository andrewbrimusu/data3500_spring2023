ages = []
ages.append(41)
ages.append(21)
ages.append(22)
ages.append(20)
ages.append(23)

print(ages)

print(ages[0], ages[-1])



andy = {}
andy["name"] = "andy brim"
andy["age"] = 41
andy["major"] = ["CS BS", "MSFE", "CS PHD"]
andy["kid"] = {"name" : "jack", "age" : 16}

print(andy)

betsy_car = {}
betsy_car["make"] = "mazda"
betsy_car["model"] = "mazda3"
betsy_car["year"] = 2007
betsy_car["lock_type"] = "manual"
betsy_car["transmission_type"] = "semi automatic"
betsy_car["engine"] = {"num_cylinders" : 4, "turbo" : False, "size" : "2.3L"}

betsy_car_make = "mazda"
betsy_car_model = "mazda3"
betsy_car_year = 2007


for age in ages:
    print("age: ", age)

for key in betsy_car.keys():
    print("key: ", key, end=' ')
    print("value: ", betsy_car[key])
    


age = eval(input("enter your age: "))
fav_color = input("favorite color")

person_info = {}
person_info["age"] = age
person_info["fav_color"] = fav_color

for key in person_info.keys():
    print(key, person_info[key])
    
