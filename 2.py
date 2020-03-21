f = open('text2.txt', 'r')
content = f.read()
print(f'Содержимое файла: \n {content}')

f = open('text2.txt', 'r')
content = f.readlines()
print(f'Количество строк: {len(content)}')

f = open('text2.txt', 'r')
content = f.read()
content = content.split()
print(f'количество слов во всем файле: {len(content)}')

f.close()





