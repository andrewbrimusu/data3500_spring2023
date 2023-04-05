import random

randoms = []
for i in range(1000):
    randoms.append(random.randint(1,256))
    
    
    
print(randoms)

randoms2 = [random.randint(1,256) for i in range(1000)]


print(randoms2)

str_nums = [ str(x) for x in range(2,11,2) ]

print(str_nums)



prices = [ float(line) for line in open("/home/ubuntu/environment/data3500_spring2023/data3500/week10/content_videos/AAPL.txt").readlines() ]

print(prices)



input("pause")























# Adding values to a list with a for loop
lst = []
for i in range(100):
    lst.append(i)
    
print("lst: ", lst)

# list comprehension
lst = [i for i in range(50)]
print("lst: ", lst)

# updating each value in a list comprehension
lst = [str(i) for i in range(25)]
print("lst: ", lst)

# list comprehension example
file = open("/home/ec2-user/environment/week10/content_videos/AAPL.txt")
lines = file.readlines()
print("lines: ", lines)
prices = [float(line) for line in lines]
print("prices: ", prices)

# checkpoint 
# create a list of even numbers 2 through 100 using a list comprehension













# solution
evens = [i for i in range(2,101,2)]
print("evens: ", evens)