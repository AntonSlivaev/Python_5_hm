my_dict = {'One' : 'Один', 'Two' : 'Два', 'Three' : 'Три', 'Four' : 'Четыре', 'Five': 'Пять', 'Six' : 'Шесть',
'Seven': 'Семь', 'Eight' : 'Восемь', 'Nine' : 'Девять'}
new_file =[]
with open ('text4.txt', 'r') as file_obj:
    for i in file_obj:
        i = i.split(' ', 1)
        new_file.append(my_dict[i[0]] + ' ' + i[1])
    print(new_file)
with open('text4_new.txt', 'w') as file_obj_2:
    file_obj_2.writelines(new_file)

