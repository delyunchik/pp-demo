f = open('students.csv', encoding='utf-8-sig')
head = f.readline()
sm = 0
k = 0
data = f.readlines()
for line in data:
    a = line.strip().split(',')
    if "None" not in a[4]:
        sm += int(a[4])
        k += 1
    if 'Хадаров Владимир' in a[1]:
        print('Ты получил: ' + a[4] + ', за проект - ' + a[2])
sm = round(sm/k, 3)
print(sm)
f = open('student_new.csv', 'w', encoding='utf-8-sig')
print(head, end='', file=f)
for line in data:
    a = line.strip().split(',')
    if "None" in a[4]:
        a[4] = str(sm)
    print(','.join(a), file=f)
