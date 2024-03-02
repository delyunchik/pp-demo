f = open('students.csv', encoding='utf-8-sig')
lst = []
for line in f.readlines():
    a = line.strip().split(',')
    lst.append(a)

p = 67
m = 10**9 + 9

for i in range(len(lst)):
    if i == 0:
        lst[i][0] = 'hash'
    else:
        fio = lst[i][1]
        hash = 0
        for j in range(len(fio)):
            if 'а' <= fio[j] <= 'я':
                sj = ord(fio[j])-ord('а')+1
            elif 'А' <= fio[j] <= 'Я':
                sj = ord(fio[j])-ord('А')+34
            else:  # пробел
                sj = 67
            hash += sj * (p ** j % m)
        lst[i][0] = str(hash)

f2 = open('students_with_hash.csv', 'w', encoding='utf-8-sig')
for a in lst:
    print(','.join(a), file=f2)
