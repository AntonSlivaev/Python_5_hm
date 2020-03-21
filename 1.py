f = open ('text.txt', 'w')
str_list = input('Введите текст: \n')
while str_list:
    f.writelines(str_list)
    str_list = input('Введите текст: \n')
    if not str_list:
        break
f.close()

with open ('text.txt') as f:
    for line in f:
        print(line)
f.close()