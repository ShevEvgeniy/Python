
from model import get_info as info

def read_contact():
    with open('Phonebook/Phonebook.csv', 'r', encoding='utf=8') as f:
        return f.read()

def writing_scv (info):
    file = 'Phonebook/phonebook.csv'
    with open (file, 'a', encoding= 'utf-8') as data:
        data.write(f'фамилия: {info[0]}; Имя: {info[1]}; Номер телефона: {info[2]}; Описание: {info[3]}\n')

def writing_txt (info):
    file = 'Phonebook/phonebook.txt'
    with open (file, 'a', encoding= 'utf-8') as data:
        data.write(f'фамилия: {info[0]}\nИмя: {info[1]}\nНомер телефона: {info[2]}\nОписание: {info[3]}\n\n')
