#grade=int(input().strip())
n = int(input())

grades = []
for _ in range(n):
    grades_item = int(input())
    grades.append(grades_item)
for i in range(len(grades)):
    diff=5-(grades[i]%5)
    if(diff<3):
        newgrade=grades[i]+diff
    else:
        newgrade=grades[i]
    if (newgrade>=40):
        grades[i]=newgrade

print(grades)


