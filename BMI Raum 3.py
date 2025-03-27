import os  # Modul für Systemfunktionen # Модуль для работы с системой  #Raum 3 Anastasia Maksym Tobias

# Funktion zur sicheren Eingabe des Namens # Функция для безопасного ввода имени
def eingabe_name():
    while True:
        name = input("Gib deinen Namen ein: ").strip()  # Geben Sie den Namen ohne Leerzeichen an den Rändern ein # Ввод имени без пробелов по краям
        if name:  # Проверяем, что имя не пустое
            return name
        print("Fehler: Der Name darf nicht leer sein!")  # Fehler: Name darf nicht leer sein! # Ошибка: имя не может быть пустым!

# Funktion zur sicheren Eingabe des Geschlechts # Функция для безопасного ввода пола
def eingabe_geschlecht():
    while True:
        geschlecht = input("Bist du Mann oder Frau? (m/f): ").strip().lower()
        if geschlecht in ["m", "f"]:
            return geschlecht
        print("Fehler: Bitte 'm' für Mann oder 'f' für Frau eingeben.")  # Fehler: Geben Sie „m“ für männlich oder „f“ für weiblich ein. # Ошибка: введите "m" для мужчины или "f" для женщины.

# Funktion zur sicheren Eingabe von Gewicht und Größe # Функция для безопасного ввода веса и роста
def eingabe_daten():
    while True:  
        try:
            gewicht = float(input("Gib dein Gewicht in kg ein: "))  
            if gewicht <= 0:  
                print("Fehler: Das Gewicht muss größer als 0 sein!")  
                continue  

            groesse = float(input("Gib deine Größe in Metern ein (z.B. 1.75): "))  
            if groesse <= 0:  
                print("Fehler: Die Größe muss größer als 0 sein!")  
                continue  

            return gewicht, groesse  

        except ValueError:  
            print("Ungültige Eingabe! Bitte eine Zahl eingeben.")  

# Funktion zur Berechnung des BMI # Функция для расчета ИМТ
def berechne_bmi(gewicht, groesse):
    return gewicht / (groesse * groesse)  

# Funktion zur Klassifikation des BMI nach Geschlecht # Функция для классификации ИМТ по полу
def klassifiziere_bmi(bmi, geschlecht):
    if geschlecht == "m":  # Männer-Tabelle / Таблица для мужчин
        if bmi < 16.0:
            return "Starkes Untergewicht " #/ Сильный недостаток веса
        elif bmi < 17.0:
            return "Mäßiges Untergewicht " #/ Умеренный недостаток веса
        elif bmi < 18.5:
            return "Leichtes Untergewicht " # / Легкий недостаток веса
        elif bmi < 25.0:
            return "Normalgewicht " #/ Норма
        elif bmi < 30.0:
            return "Übergewicht " #/ Избыточный вес
        elif bmi < 35.0:
            return "Adipositas Grad I " #/ Ожирение 1 степени
        elif bmi < 40.0:
            return "Adipositas Grad II " #/ Ожирение 2 степени
        else:
            return "Adipositas Grad III " #/ Ожирение 3 степени
    
    else:  # Frauen-Tabelle / Таблица для женщин
        if bmi < 15.0:
            return "Starkes Untergewicht " #/ Сильный недостаток веса
        elif bmi < 15.9:
            return "Mäßiges Untergewicht " #/ Умеренный недостаток веса
        elif bmi < 17.5:
            return "Leichtes Untergewicht " # / Легкий недостаток веса
        elif bmi < 24.0:
            return "Normalgewicht " #/ Норма
        elif bmi < 29.0:
            return "Übergewicht " #/ Избыточный вес
        elif bmi < 34.0:
            return "Adipositas Grad I " #/ Ожирение 1 степени
        elif bmi < 39.0:
            return "Adipositas Grad II " #/ Ожирение 2 степени
        else:
            return "Adipositas Grad III " #/ Ожирение 3 степени

# Hauptprogramm # Основная программа
name = eingabe_name()  # Пользователь вводит свое имя
geschlecht = eingabe_geschlecht()  # Пользователь выбирает пол

print(f"Hallo, {name}! Willkommen beim BMI-Rechner.")  

gewicht, groesse = eingabe_daten()  
bmi = berechne_bmi(gewicht, groesse)  
kategorie = klassifiziere_bmi(bmi, geschlecht)  

# Ausgabe des Ergebnisses # Вывод результата
print(f"\n{name}, dein BMI beträgt: {round(bmi, 1)}")  
print(kategorie)  