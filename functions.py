def count_words(data):
    """Liczy slowa i zapisuje w postaci listy"""
    words = []
    word = str
    
    for letter in data:
        if letter == " ": #sprawdza czy nie ma spacji; jesli jest dodaje slowo do listy
            words.append(word)
        else: #sumuje litery do slow
            word = str(word) + str(letter)
    return words  

def input_data(): 
    """Pobiera tekst od uzytkownika"""
    data = input()
    data += "\n"
    return data
        
def print_data(data, verify=False, words=None):
    """Wyswietla dane, gdy wywolane""" 
    if "/print" in data:
        print(data)
        data = data.replace("/print", "") 
    if "/analyze" in data:
        data = data.replace("/analyze", "") 
        print("Analizowanie danych...")
        lenth = len(data)
        print(f"Obecny dokument zawiera {lenth} liter")
    if verify == True: #wiadomosc do debbugowania 
        for value in words:
            print(value)
    else:
        pass
