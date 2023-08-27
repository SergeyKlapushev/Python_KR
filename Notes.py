import json
import os, os.path
import glob

note_list = []

work = True

#Показать меню
def showMenu():
    print("Введите цифру: ")
    print(" 1. Создать заметку")
    print(" 2. Прочитать список заметок")
    print(" 3. Отредактировать заметку")
    print(" 4. Удалить заметку")
    print(" 5. Завершить работу")    

#Выбрать функцию
def makeSelect():
    return int(input())

#Выбрать действие
def SaveOrChance():
    return str(input())

#Вводим имя файла
def inputNameFile():
    print("Введите имя файла: ")
    file_name = input()
    file_name = file_name + ".json"
    return file_name

#Уведомление о повторяющемся файле
def existingFile(notification, file_name, title, body):
    print(notification)
    chance = input()
    if(chance == "Y"):
        saveFile(file_name, title, body)
    if(chance == "N"):
        preliminaryNote(title, body)

#Сохраняем файл
def saveFile(file_name, title, body):

    note = {'title': title,
            'body': body}
    
    note = json.dumps(note)
    note = json.loads(str(note))
    note_list.append(note)
    with open(file_name, 'w', encoding='utf-8') as file:
        json.dump(note, file, indent= 4)

#Сохранение в файл
def saveProcess(title, body):
    file_name = inputNameFile()

    if(os.path.exists(file_name) == True):
        existingFile("Файл с таким именем уже существует, хотите перезаписать файл?(Y/N)", file_name, title, body)
    else:
        saveFile(file_name, title, body)

#Вводим Заголовок и тело
def dataInput():
    print("Введите заголовок заметки: ")
    title_note = input()
    print("Введите тело заметки: ")
    body_note = input()
    preliminaryNote(title_note, body_note)

#Предпоказ заметки
def preliminaryNote(title, body):
    print("| Заголовок: " + title + " |")
    print("| Тело: " + body + " |")
    print("Чтобы сохранить заметку, введите S, чтобы изменить, введите C")
    chance = SaveOrChance()

    if (chance == "S"):
        saveProcess(title, body)

    if (chance == "C"):
        dataInput()

#Смотрим список заметок
def ShowListNotes():
    print("------Ваши заметки--------")
    for x in os.listdir():
        if x.endswith(".json"):
            print(x)
    print("--------------------------")

#Редактируем заметку
def RequestNoteName(mess):
    print(mess)
    file_name = input() + ".json" 
    SearchFile(file_name)

#Поиск файла
def SearchFile(file_name):
    if(os.path.exists(file_name) == True):
        with open(file_name, "r+") as jsonFile:
            data = json.load(jsonFile)
            lastTile = data["title"]
            lastBody = data["body"]
            print("Введите заголовок: ")
            data["title"] = input()
            print("Введите текст заметки: ")
            data["body"] = input()
            print("---Заголовок---\n Было: " + lastTile + "; \n Стало: " + data["title"] + "\n---------------")
            print("---Тело---\n Было: " + lastBody + "; \n Стало: " + data["body"] + "\n---------------")
        with open(file_name, "w", encoding='utf-8') as jsonFile:
            json.dump(data, jsonFile)
    else:
        RequestNoteName("Заметка не найдена, введите название файла ещё раз: ")

#Удаление файла
def DeliteNote(mess):
    print(mess)
    print("Введите имя файла который хотите удалить: ")
    fileName = input() + ".json"
    os.remove(fileName)

while (work == True):

    showMenu()
    select = makeSelect()

    if(select == 1):
        dataInput()

    if(select == 2):
        ShowListNotes()
    
    if(select == 3):
        RequestNoteName("Введите название файла который хотите редактировать: ")

    if(select == 4):
        DeliteNote("Удалить заметку")

    if(select == 5):
        work = False

    