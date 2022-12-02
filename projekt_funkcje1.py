#zadaniem jest pobieranie danych z kolumn w pliku csv (excel) i podstawianie pod nie wartości ze słowników, (dla kazdej kolumny inny)
#i zwrócenie pliku csv z podstawionymi wartościami.
# q komórce wtystępuję ciąg wartości (lista)
#import csv
import pandas as pd

df = pd.read_csv('wsad1_slowniki.csv', delimiter= ';')
#df1 = pd.DataFrame.dropna(df)
#print(df)
print(df.columns)

df.drop(['media::image','media::audio', 'label::language (xx)'], axis=1, inplace=True)
print(df.columns)
# print(df.columns)
# for i in
#     df.loc[df['list_name'] == value]
#pandas.read_csv(filepath_or_buffer, *, sep=_NoDefault.no_default, delimiter=None, header='infer', names=_NoDefault.no_default, index_col=None, usecols=None, squeeze=None, prefix=_NoDefault.no_default, mangle_dupe_cols=True, dtype=None, engine=None, converters=None, true_values=None, false_values=None, skipinitialspace=False, skiprows=None, skipfooter=0, nrows=None, na_values=None, keep_default_na=True, na_filter=True, verbose=False, skip_blank_lines=True, parse_dates=None, infer_datetime_format=False, keep_date_col=False, date_parser=None, dayfirst=False, cache_dates=True, iterator=False, chunksize=None, compression='infer', thousands=None, decimal='.', lineterminator=None, quotechar='"', quoting=0, doublequote=True, escapechar=None, comment=None, encoding=None, encoding_errors='strict', dialect=None, error_bad_lines=None, warn_bad_lines=None, on_bad_lines=None, delim_whitespace=False, low_memory=True, memory_map=False, float_precision=None, storage_options=None)

#import csvreader as csvreader
# filename = "wsad1_slowniki.csv" #input("Podaj nazwę pliku:")
# il_wierszy = 0
# def wczytaj_plik():
#     fields = []
#     rows = []
#     with open(filename, 'r') as csvfile:
#         #w oryginale było csvreader podpowiadacz zalecił nazwę _reader choć teraz nie wiem po co jest wczytany csv
#         csvreader = csv.reader(csvfile)
#         fields = next(csvreader)
#         for row in csvreader:
#             rows.append(row)
#
#         il_wierszy = csvreader.line_num
#
#         print(f"total noo of rows: {csvreader.line_num}")
#         print('Field names are:' + ','.join(field for field in fields))
#         return il_wierszy
# print(wczytaj_plik())
#def usun_puste_kol():

#print('\n First 5 rows are:\n')
# def zczytaj_z_pierwszej(rows=None):
#     for row in rows[0]:
#         for col in row[0]:
#             print("%10s" %col, end=" ")
#         print('\n')
# def tworz_slownik:
#     for i in col[0]
#print(csvfile.name)

#powinna przejść pierwszą kolumnę i zczytać wszystkie wartości
#jeżeli wartości są takie same z wartości w kol 2 i 3 robi słowniki
#tyle słowników ile unikalnych wartości w pierwszej kolumnie

# def tworz_slownik():
#     for x in range