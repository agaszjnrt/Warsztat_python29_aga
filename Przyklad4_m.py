from typing import Any
#uzywane do wyszukiwania błedow
#nie zwroci błedó gdy uzytkownik uzywa roznych typew dla kluczy
# def get_ci(d: dict, key: str) -> Any:
#     for k, v in d.items():
#         if key.lower() == k.lower():
#             return v

# wersja z restrykcjami
def get_ci(d: dict[str, Any], key: str) -> Any:
    for k, v in d.items():
        if key.lower() == k.lower():
            return v

#importowanie z modułu typing nie długo zniknie
#generalnie Pan zaleca używanie typow generycznych

#PARAMETRY CZYSTO POZYCYJNE: (lub nazwy argumentow)
#wskazanie, ze okreslone argumenty tylko za pomoca nazw- to w przyszlosci pozwala zmodyfikowac funkcje latwiej
#wszystkie argumenty przed / pozycycjne, za *
def concatene(first: str, second:str,/,*, delim:str):
    return delim.join([first, second])
print(concatene("jan","kowalski", delim=" "))

def concatene2(*items, delim:str):
    return delim.join(items)
print(concatene("jan","kowalski", delim=" "))
print(concatene2("jan","kowalski", delim=" "))