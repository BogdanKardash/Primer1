#1 задание выполнял вместе с Даниилом Кардаш, проверил Эвелина Иманбаева
from sympy import *
k,T,C,L = symbols('k T C L')
#1-й способ 100000
Am_lst=[]
C_ost_lst=[]
print ('Индивидуальное задание 5 вариант')
C_ost = 20000
Am_lst=[]
C_ost_lst=[]
for i in range (6):
  Am=(C-L)/T  
  C_ost -= Am.subs({C:20000, T:6, L:0})
  Am_lst.append(round(Am.subs({C:20000, T:6, L:0}),2))
  C_ost_lst.append(round(C_ost,2))
print('Am_lst: ', Am_lst)
print('C_ost_lst: ',C_ost_lst)
#2-й способ
Aj=0
C_ost=20000
Am_lst_2=[]
C_ost_lst_2=[]
for i in range (6):
  Am= k*1/T*(C-Aj)
  C_ost-= Am.subs({C:20000, T:6, k:2})
  Am_lst_2.append(round(Am.subs({C:20000, T:6, k:2}),2))
  Aj+=Am.subs({C:20000, T:6, k:2})
  C_ost_lst_2.append(round(C_ost,2))
print ('Am_lst_2: ', Am_lst_2)
print ('C_ost_lst_2: ',C_ost_lst_2)
#Представление в таблице
import pandas as pd
Y= range(1,7)
table1=list(zip(Y,Am_lst,C_ost_lst)) #Что мы делаем через zip? zip объединяет несколько списков в кортежи
table2=list(zip(Y,Am_lst_2,C_ost_lst_2))
tframe=pd.DataFrame(table1,columns=['Y','Am_lst','C_ost_lst'])
tframe2=pd.DataFrame(table2,columns=['Y','Am_lst_2','C_ost_lst_2'])
print(tframe)
print(tframe2)

#Контейнер визуализации
import numpy as np 
import matplotlib.pyplot as plt
plt.figure()
plt.plot(tframe['Y'],tframe['C_ost_lst'],label='Am_lst')
plt.savefig('chart7.png')
plt.figure() 
plt.plot(tframe2['Y'],tframe2['C_ost_lst_2'],label='Am_lst_2')
plt.savefig('chart8.png')
#Круговая диаграмма по 1 способу
vals=Am_lst
labels=[str(x) for x in range(1,7)]
explode =(0.1,0.1,0.1,0.1,0.1,0.1)
fig,ax=plt.subplots()
ax.pie(vals,explode=explode,labels=labels,autopct='%1.1f%%',shadow=True,wedgeprops={'lw':1,'ls':'--','edgecolor': "k"},rotatelabels=True)
ax.axis("equal")
plt.savefig('chart9.png')
#Круговая диаграмма по 2 способу
vals=Am_lst_2
labels=[str(x) for x in range(1,7)]
explode =(0.1,0.1,0.1,0.1,0.1,0.1)
fig,ax=plt.subplots() # Что это означает? fig  — это контейнер для всех элементов графика, ax  — это область, где непосредственно строится график 
ax.pie(vals,explode=explode,labels=labels,autopct='%1.1f%%',shadow=True,wedgeprops={'lw':1,'ls':'--','edgecolor': "k"},rotatelabels=True)
ax.axis("equal")
plt.savefig('chart10.png')

table1 = list(zip(Y, Am_lst))
table2 = list(zip(Y, Am_lst_2))
tframe = pd.DataFrame(table1, columns=['Y', 'Am_lst']) 
tframe2 = pd.DataFrame(table2, columns=['Y', 'Am_lst_2'])  
plt.figure()
plt.bar(tframe['Y'], tframe['Am_lst']) #Что это означает? Это построение столбчатой диаграммы, где каждому значению X соответствует один столбец высотой, равной значению амортизации
plt.savefig('chart11.png')
plt.close()
plt.figure()
plt.bar(tframe2['Y'], tframe2['Am_lst_2'])
plt.savefig('chart12.png')
plt.close()

#Ошибок не найдено 5/5
#На вопросы ответила Эвелина Иманбаева
#Задание 5 работа с Shell
#Задание 6 подключен аккаунт на GitHub и подвязаны файла на Github 




import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import json
import os

#КОНТЕЙНЕР 1: ЗАГРУЗКА ДАННЫХ

def load_data(source):
    """Загружает данные, при неизвестном формате использует резервные"""
    try:
        if isinstance(source, str) and os.path.exists(source):
            if source.endswith('.json'):
                with open(source, 'r') as f:
                    data = json.load(f)
                print(f"Данные успешно загружены из файла: {source}")
            elif source.endswith('.csv'):
                data = pd.read_csv(source).to_dict('records')
                print(f"Данные успешно загружены из файла: {source}")
            else:
                print(f"Неизвестный формат файла: {source}")
                print("Использую резервные данные")
                data = {
                    "Период": [1, 2, 3, 4, 5, 6],
                    "Показатель_1": [100, 150, 200, 250, 300, 350],
                    "Показатель_2": [50, 75, 100, 125, 150, 175]
                }
        else:
            print(f"Файл не найден: {source}")
            print("Использую резервные данные")
            data = {
                "Период": [1, 2, 3, 4, 5, 6],
                "Показатель_1": [100, 150, 200, 250, 300, 350],
                "Показатель_2": [50, 75, 100, 125, 150, 175]
            }
    except Exception as e:
        print(f"Ошибка загрузки: {e}")
        print("Использую резервные данные")
        data = {
            "Период": [1, 2, 3, 4, 5, 6],
            "Показатель_1": [100, 150, 200, 250, 300, 350],
            "Показатель_2": [50, 75, 100, 125, 150, 175]
        }
    return data

#КОНТЕЙНЕР 2: ПОДГОТОВКА ДАННЫХ 

def prepare_data(data):
    """Подготавливает данные для таблиц и графиков"""
    if isinstance(data, list):
        years = list(range(1, len(data) + 1))
        values1 = [d.get(list(d.keys())[0], 0) for d in data]
        values2 = [d.get(list(d.keys())[1], 0) for d in data] if len(data[0]) > 1 else values1
    else:
        years = data.get("Период", list(range(1, 7)))
        values1 = data.get("Показатель_1", [100, 150, 200, 250, 300, 350])
        values2 = data.get("Показатель_2", [50, 75, 100, 125, 150, 175])
    return years, values1, values2

#КОНТЕЙНЕР 3: ТАБЛИЦЫ И ВИЗУАЛИЗАЦИЯ 

def show_results(years, values1, values2):
    """Таблицы и визуализация (строго по шаблону)"""

    Y = years
    data1 = values1
    data2 = values2

    # Создание таблиц с результатами
    table1 = list(zip(Y, data1, data2))
    table2 = list(zip(Y, data2, data1))

    tfame = pd.DataFrame(table1, columns=["Y", "Показатель_1", "Показатель_2"])
    tfame2 = pd.DataFrame(table2, columns=["Y", "Показатель_2", "Показатель_1"])

    print("РЕЗУЛЬТАТЫ ОБРАБОТКИ ДАННЫХ")
    print("\nТаблица 1")
    print(tfame)
    print("\nТаблица 2")
    print(tfame2)

    # График изменения показателя 1 по годам
    plt.plot(tfame["Y"], tfame["Показатель_1"], label="Показатель_1")
    plt.savefig("chart7.png")
    plt.clf()

    # График изменения показателя 2 по годам
    plt.plot(tfame2["Y"], tfame2["Показатель_2"], label="Показатель_2")
    plt.savefig("chart8.png")
    plt.clf()

    # Круговая диаграмма для показателя 1
    vals = data1
    labels = [f"{x} год" for x in Y]
    explode = (0.15, 0.15, 0.15, 0.15, 0.15, 0.15)
    fig, ax = plt.subplots()
    ax.pie(
        vals,
        labels=labels,
        autopct="%1.1f%%",
        shadow=True,
        explode=explode,
        wedgeprops={"lw": 0.5, "ls": "--", "edgecolor": "white"},
        rotatelabels=True,
    )
    ax.axis("equal")
    plt.savefig("chart9.png")
    plt.clf()

    # Круговая диаграмма для показателя 2
    vals = data2
    labels = [f"{x} год" for x in Y]
    explode = (0.15, 0.1, 0.05, 0.05, 0.05, 0.05)
    fig, ax = plt.subplots()
    ax.pie(
        vals,
        labels=labels,
        autopct="%1.1f%%",
        shadow=True,
        explode=explode,
        wedgeprops={"lw": 0.5, "ls": "--", "edgecolor": "k"},
        rotatelabels=True,
    )
    ax.axis("equal")
    plt.savefig("chart10.png")
    plt.clf()

    # Столбчатые диаграммы (гистограммы)
    table1 = list(zip(Y, data1))
    table2 = list(zip(Y, data2))
    tfame = pd.DataFrame(table1, columns=["Y", "Показатель_1"])
    tfame2 = pd.DataFrame(table2, columns=["Y", "Показатель_2"])

    plt.clf()
    plt.bar(tfame["Y"], tfame["Показатель_1"])
    plt.savefig("chart11.jpeg")
    plt.clf()

    plt.bar(tfame2["Y"], tfame2["Показатель_2"])
    plt.savefig("chart12.jpeg")
    plt.clf()

    # Анализ данных с использованием numpy
    print(f"\nАнализ:")
    print(f"Показатель 1 - макс: {np.max(data1)} руб., мин: {np.min(data1)} руб.")
    print(f"Показатель 2 - макс: {np.max(data2)} руб., мин: {np.min(data2)} руб.")

#ЗАПУСК

def main():
    print("МИКРОСЕРВИС: Защита от отказа загрузки данных")

    # Здесь указываем РЕАЛЬНЫЙ файл с данными
    # Если файл существует - загрузится он
    # Если нет - сработает защита
    filename = "data.json"  # или "data.csv" - реальный файл

    print(f"\nЗагрузка данных из файла: {filename}")
    data = load_data(filename)

    years, values1, values2 = prepare_data(data)

    print("\nФормирование таблиц и графиков...")
    show_results(years, values1, values2)

    print("\nМИКРОСЕРВИС ВЫПОЛНЕН")
    
if __name__ == "__main__":
    main()