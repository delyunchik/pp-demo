f = open('students.csv', encoding='utf-8-sig')
f.readline()
srt = []
for line in f.readlines():
    a = line.strip().split(',')
    if "None" not in a[4]:
        a[4] = int(a[4])
    else:
        a[4] = 0
    i = 0
    while i < len(srt):
        if srt[i][4] < a[4]:
            break
        i += 1
    srt.insert(i, a)
k = 0
print('10 класс:')
for a in srt:
    if '10' in a[3]:
        k += 1
        fio = a[1].split()
        print(k, 'место:', fio[1][0] + '. ' + fio[0])
        if k == 3:
            break
