print(2 ** 0)
print(2 ** 1)
print(2 ** 2)
print(2 ** 3)
print(2 ** 4)
print(2 ** 5)

print("------")

# 4 parts of a function
# 1 definition
# 2 parameter list (argument list)
# 3 function logic
# 4 return statement
def two_power(exponent):
    var = 2 ** exponent
    return var
    
for i in range(6):
    # function call
    print(two_power(i))
    


def calc_Corvette_Price(name, original_price, year_mfg, current_year):
    current_value = original_price * 1.02 ** (current_year - year_mfg)
    return current_value
    
    
name = "stuart"
orig_price = 30000
year_mfg = 1993
current_year = 2023

print(calc_Corvette_Price(name, orig_price, year_mfg, current_year))


for i in range(100):
    name = "corvette_year_" + str(i)
    orig_price = 1000 * i
    year_mfg = 1923 + i
    current_year = 2023
    
    print("year: ", i, "price: ", calc_Corvette_Price(name, orig_price, year_mfg, current_year))


    
    





