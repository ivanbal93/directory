import json


enter = '\n'
text_1 = (f'{enter}Нажмите "1", чтобы вывести все строки справочника.{enter}'
        f'Нажмите "2", чтобы добавить в справочник новую запись. {enter}'
        f'Нажмите "3", чтобы редактировать запись в справочнике. {enter}'
        f'Нажмите "4", чтобы использовать поиск по ключевому слову. {enter}'
        f'Нажмите "0", чтобы выйти.{enter}'
        f'Введите цифру и нажмите "Enter": ')
text_2 = (f'Для сохранения нажмите "1".{enter}'
        f'Для выхода из режима ввода без сохранения, нажмите "2".{enter}'
        f'Для редактирования введёной информации нажмите "Enter":{enter}')


def get_data_from_file(filename: str) -> dict:
    '''
    Функция получения информации из файла
    '''
    with open(filename, 'r', encoding='UTF-8') as file:
        data = json.load(file)
        if not data:
            return {"response": "Справочник пока пуст!"}
        return data


def write_data_to_file(filename: str, data: dict) -> None:
    '''
    Функция записи информации в файл
    '''
    with open(filename, 'w', encoding='UTF-8') as file:
        json.dump(data, file, indent=4, ensure_ascii=False)
    print('Файл обновлён успешно!')


def add_new_info(filename: str, data: dict) -> None:
    '''
    Функция добавления новой информации
    '''
    i = int(list(data.keys())[-1]) + 1 if data.keys() else 1
    while True:
        info = {
            "Номер строки": str(i),
            "Фамилия": input("Введите Фамилию: "),
            "Имя": input("Введите Имя: "),
            "Отчество": input("Введите Отчество: "),
            "Компания": input("Введите Название компании: "),
            "Рабочий телефон": input("Введите Рабочий телефон: "),
            "Мобильный телефон": input("Введите Мобильный телефон: ")
        }
        write_data_to_file(filename, data)
        print('Новые значения:')
        print(info)
        answer = input(text_2)
        if answer == '1':
            data[i] = info
            write_data_to_file(filename, data)
            break
        elif answer == '2':
            break


def edit_info(filename: str, data: dict) -> None:
    '''
    Функция редактирования информации
    '''
    i = input('Введите номер строки, которую необходимо отредактировать: ')
    while i not in data.keys():
        i = input('Строки с таким номером нет. Попробуйте ещё раз: ')
    line = data[i]
    while True:
        for key, value in list(line.items())[1:]:
            change = input(f'Старое значение: {key} - {value}. '
                           f'Введите новое или нажмите "=", чтобы оставить его: ')
            if change != '=':
                line[key] = change
        print(f'Новые значения:{enter}{line}')
        answer = input(text_2)
        if answer == '1':
            data[i] = line
            write_data_to_file(filename, data)
            break
        elif answer == '2':
            break


def search(filename: str, data: dict) -> list:
    '''
    Функция поиска записи
    '''
    while True:
        result = []
        word = input('Введите ключевое слово для поиска: ')
        for value in data.values():
            for val in value.values():
                if word.lower() in val.lower():
                    result.append(value)
        if not result:
            return [f"{enter}По Вашему запросу ничего не найдено!"]
        break
    return result


def main(filename: str):
    '''
    Основная логика программы
    '''
    print('---Телефонный справочник---')
    while True:
        answer = input(text_1)
        data = get_data_from_file(filename)

        if answer not in '01234':
            answer = input(f'{enter}Некорректный ввод. Попробуйте ещё раз.'
                           f'{enter}{text_1}')

        elif answer == '0':
            break

        elif answer == '1':
            print('---Телефонный справочник---')
            [print(line) for line in data.values()]

        elif answer == '2':
            add_new_info(filename, data)

        elif answer == '3':
            edit_info(filename, data)

        elif answer == '4':
            [print(line) for line in search(filename, data)]


main("data.json")
