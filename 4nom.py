from random import choice

f = open('students.csv', encoding='utf-8-sig')
lst = []
for line in f.readlines():
    a = line.strip().split(',')
    lst.append(a)

chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789'
for i in range(len(lst)):
    if i == 0:
        lst[i].append('login')
        lst[i].append('password')
    else:
        fio = lst[i][1].split()
        login = f'{fio[0]}_{fio[1][0]}{fio[2][0]}'
        pwd = ''
        for _ in range(8):
            pwd += choice(chars)
        lst[i].append(login)
        lst[i].append(pwd)

f2 = open('students_password.csv', 'w', encoding='utf-8-sig')
for a in lst:
    print(','.join(a), file=f2)
