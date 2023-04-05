fil = open("/home/ubuntu/environment/data3500_spring2023/data3500/week6/AAPL.csv")

lines = fil.readlines()


prcs = []

for line in lines:
    price = float(line)
    prcs.append(price)
    
    
print(prcs)

for i in range(len(prcs)):
    if i >= 4:
        avg = (prcs[i] + prcs[i-1] + prcs[i-2] + prcs[i-3]) / 4
        print("avg", avg)
    
