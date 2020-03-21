with open ('text3.txt', 'r') as f:
    sal = []
    low_sal = []
    list = f.read().split('\n')
    for i in list:
        i = i.split()
        if int(i[1]) < 20000:
            low_sal.append(i[0])
        sal.append(i[1])
print(f'Оклад меньше 20 000 руб {low_sal}, средний оклад {sum(map(int,sal)) / len(sal)}')