id = input()
while id != 'СТОП':
    id = int(id)
    f = open('students.csv', encoding='utf-8-sig')
    f.readline()
    found = 0
    for line in f.readlines():
        a = line.strip().split(',')
        fio = a[1].split()
        if id == int(a[2]):
            print(f'Проект № {id} делал: {fio[1][0]}. {fio[0]} он(а) получил(а) оценку - {a[4]}')
            found = 1
    if found == 0:
        print('Ничего не найдено.')
    id = input()
