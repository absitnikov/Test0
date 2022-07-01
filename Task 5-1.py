documents = [
    {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
    {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
    {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
]
directories = {
    '1': ['2207 876234', '11-2', '5455 028765'],
    '2': ['10006'],
    '3': []
}


def search_people():
    num_doc = input('Введите N документа: ')
    for num in documents:
        if num['number'] == num_doc:
            print(num['name'])
            return
    print('Документ в базе не найден')


def search_shelf():
    num_doc = input('Введите № документа: ')
    for dir_key, dir_val in directories.items():
        if num_doc in dir_val:
            print('Полка №: ', dir_key)
            return
    print('Документ в базе не найден')


def list_documents():
    for my_list in documents:
        print(('{} "{}" "{}"').format(my_list['type'], my_list['number'], my_list['name']))


def add_documents():
    num_doc = input('Введите № документа: ')
    type_doc = input('Введите тип документа: ')
    name_doc = input('Введите имя владельца: ')
    num_shelf = input('Введит № полки: ')
    if num_shelf in directories:
        directories[num_shelf].append(num_doc)
        documents.append({'number': num_doc, 'type': type_doc, 'name': name_doc})
    else:
        directories[num_shelf] = []
        directories[num_shelf].append(num_doc)
        documents.append({'number': num_doc, 'type': type_doc, 'name': name_doc})
    print(documents)
    print(directories)


def delete_documents():
    num_doc = input('Введите № документа: ')
    for document in documents:
        if document['number'] == num_doc:
            documents.remove(document)
    for dir_value in directories.values():
        if num_doc in dir_value:
            dir_value.remove(num_doc)
            return
    print('Документ в базе не найден')


def mov_documents():
    num_doc = input('Введите № документа: ')
    num_shelf = input('Введит № полки: ')
    for dir_value in directories.values():
        if num_doc in dir_value:
            dir_value.remove(num_doc)
    for dir_key in directories.keys():
        if num_shelf in dir_key:
            directories[dir_key].append(num_doc)
            return
    print('Полки или документа в базе не обнаружено')


def add_shelf():
    num_shelf = input('Введит № новой полки: ')
    for dir_key in directories.keys():
        if num_shelf == dir_key:
            print('Полка уже стоздана')
            return
    directories[num_shelf] = []


def command():
    while True:
        user_commands = input('\nВведите название команды: '
                              '\np - вывод имени человека по № документа; '
                              '\ns - вывод № полки по № документа; '
                              '\nl - вывод всех документов; '
                              '\na - ввод нового документа; '
                              '\nd - удаление документа; '
                              '\nm - перемещение документа; '
                              '\nas - добавить новую полку. '
                              '\n')
        if user_commands == 'p':
            search_people()
        elif user_commands == 's':
            search_shelf()
        elif user_commands == 'l':
            list_documents()
        elif user_commands == 'a':
            add_documents()
        elif user_commands == 'd':
            delete_documents()
        elif user_commands == 'm':
            mov_documents()
        elif user_commands == 'as':
            add_shelf()
        else:
            print('Ошибка, введите команду из списка')
command()