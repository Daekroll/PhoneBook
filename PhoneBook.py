def work_phoneBook():
    filename = 'phonebook.txt'
    print('Список возможных действий: \n'
          '1. Открыть весь справочник\n'
          '2. Найти контакт по ФИО/номеру телефона\n'
          '3. Изменить контакт\n'
          '4. Удалить контакт\n'
          '5. Добавить новый контакт\n'
          '6. Завершить работу\n')
    print()
    work = 0
    work = int(input('Введите номер действия: '))
    if work == 1:
        read_txt(filename)
        print('\n')
    elif work == 2:
        find_contact(filename)
        print('\n')
    elif work == 3:
        correct_contact(filename)
        print('\n')
    elif work == 4:
        Delete_Contact(filename)
    elif work == 5:
        ContactAdd(filename)   

def read_txt(filename):
    phone_book = []
    with open(filename, 'r', encoding='utf-8') as i:
        for line in i:
            record = list(line.split(','))
            phone_book.append(record)
    for i in phone_book:
        print(*i, end='')
    work_phoneBook()

def find_contact(filename):
    info = input('Введите имя, фамилию или номер телефона: ')
    print('\n')
    phone_book = []
    find = []
    with open(filename, 'r', encoding='utf-8') as i:
        for line in i:
            record = list(line.split(','))
            phone_book.append(record)
    for i in phone_book:
        if info in i:
            find.append(i)
    if len(find) == 0:
        print('Такого контакта нет')
    else:
        for i in find:
            print(*i, end='')
    Replay = input('Хотите найти другой контакт? y/n')
    if Replay == y:
        find_contact(filename)
    else:
        work_phoneBook()

def correct_contact(filename):
    info = input('Введите имя, фамилию или номер телефона контакта который хотите изменить: ')
    phone_book = []
    find = []
    with open(filename, 'r', encoding='utf-8') as i:
        for line in i:
            record = list(line.split(','))
            phone_book.append(record)
    for i in range(0, len(phone_book)):
        if info in phone_book[i]:
            correct1 = i
            for j in phone_book[i]:
                find.append(j)
    if len(find) == 0:
        print('Такого контакта нет')
    else:
        correct = int(input('Введите номер пункта который хотите изменить: \n'
                            '1.Фамилия \n'
                            '2.Имя \n'
                            '3.Номер телефона \n'
                            '4.Описание \n'
                            '5.Не изменять \n'))
        if correct < 4:
            find[correct-1] = input('Введите новое значение: ')
            print('Контакт после изменения: ')
            print(find)
        elif correct == 4:
            find[correct-1] = input('Введите новое значение: ')+'\n'
        phone_book[correct1] = find
        data = open(filename,'w', encoding='utf-8')
        for i in phone_book:
            s = ''
            for j in range(0, 4):
                if j < 3:
                    s+=i[j]+','
                else:
                    s+=i[j]
            data.write(s)
    work_phoneBook()

def Delete_Contact(filename):
    info = input('Введите имя, фамилию или номер телефона контакта который хотите удалить: ')
    phone_book = []
    with open(filename, 'r', encoding='utf-8') as i:
        for line in i:
            record = list(line.split(','))
            phone_book.append(record)
    for i in range(0, len(phone_book)):
        if info in phone_book[i]:
            phone_book.pop(i)
    with open(filename,'w', encoding='utf-8') as data:
        for i in phone_book:
            s = ''
            for j in range(0, 4):
                if j < 3:
                    s+=i[j]+','
                else:
                    s+=i[j]
            data.write(s)
    work_phoneBook()

def ContactAdd(filename):
    info = input('Введите фамилию имя номер и комментарий через пробел для добавления: ')+'\n'
    file = list(info.split())
    with open(filename,'a', encoding='utf-8') as data:
            s = '\n'
            for j in range(0, 4):
                if j < 3:
                    s+=file[j]+','
                else:
                    s+=file[j]
            data.write(s)
    work_phoneBook()
