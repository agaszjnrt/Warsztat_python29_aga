#zadaniem jest pobieranie danych z kolumn w pliku csv (excel) i podstawianie pod nie wartości ze słowników, (dla kazdej kolumny inny)
#i zwrócenie pliku csv z podstawionymi wartościami.
# q komórce wtystępuję ciąg wartości (lista)
import csv
import pandas as pd

#import csvreader as csvreader
filename = "wsad1_slowniki.csv" #input("Podaj nazwę pliku:")
il_wierszy = 0
def wczytaj_plik():
    fields = []
    rows = []
    with open(filename, 'r') as csvfile:
        #w oryginale było csvreader podpowiadacz zalecił nazwę _reader choć teraz nie wiem po co jest wczytany csv
        csvreader = csv.reader(csvfile)
        fields = next(csvreader)
        for row in csvreader:
            rows.append(row)

        il_wierszy = csvreader.line_num

        print(f"total noo of rows: {csvreader.line_num}")
        print('Field names are:' + ','.join(field for field in fields))
        return il_wierszy
print(wczytaj_plik())

#print('\n First 5 rows are:\n')
def zczytaj_z_pierwszej(rows=None):
    for row in rows[:il_wierszy]:
        for col in row[0]:
            print("%10s" %col, end=" ")
        print('\n')
# def tworz_slownik:
#     for i in col[0]
#print(csvfile.name)

#powinna przejść pierwszą kolumnę i zczytać wszystkie wartości
#jeżeli wartości są takie same z wartości w kol 2 i 3 robi słowniki
#tyle słowników ile unikalnych wartości w pierwszej kolumnie

# def tworz_slownik():
#     for x in range