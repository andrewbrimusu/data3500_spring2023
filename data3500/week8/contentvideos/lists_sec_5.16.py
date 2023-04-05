#2d lists

num1 = 3
num2 = 4
# multiplication table
tab = []
for i in range(num1):
    tab.append([])
    
for i in range(1, num1+1):
    for j in range(1, num2+1):
        tab[i-1].append(i * j)
        

print("tab: ", tab, "\n")




for row in tab:
    print(row)
    


input("press enter")


for i in range(10):
    for j in range(10):
        print(tab[i][j], end=" ")
    print()
    
# list of student scores

jonny = [49, 48, 50]
sally = [49, 50, 50]
jenny = [50, 50, 50]

student_scores = [jonny, sally, jenny]

for student in student_scores:
    print(student)

for student in student_scores:
    for score in student:
        print(score, end=" ")
    print()
    
    
#checkpoint activity
# create 3 lists that represent student's homework scores (like above)
# calculate the average hw score for each student
# calculate the average hw score for all 3 students







# solution
jonny = [21, 22, 23]
sally = [31, 32, 33]
jenny = [51, 52, 53]
student_scores = [jonny, sally, jenny]

# average for each student
score_tot = 0
for student in student_scores:
    score_tot = 0
    for score in student:
        score_tot += score
    print("student average: ", score_tot / len(student))
    
# overall average
tot = 0
num_scores = 0
for student in student_scores:
    score_tot = 0
    for score in student:
        tot += score
        num_scores += 1
print("overall average: ", tot / num_scores)
    