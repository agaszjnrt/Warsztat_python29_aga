from collections import ChainMap
#ChainMap funkcja przykrywajaca-nieprzykrywajaca.stad mozna zastapowac
#umożliwia otrzymanie czegos ala słownikowego ale ma dodatki z klas typu parents etc
#user_account = {""}
user_account = {"id": "PL43678fhdj", "type": "konto"}
user_profile = {"name": "Jan Kowalski", "type": "profil"}
user = ChainMap(user_account, user_profile)
print(user["id"])
print(user["name"])
user["name"] = "Pokemon"
user["name"] = "Mickiewicz"
user["id"] = "000000001"
print(user["name"])
print(user["type"])
print(user_profile)
print(user_account)
print(user)
    #  print



print([3, 4, 5, 6, 7] + ["t", "o"])

value = [1, 2, 3]
value += [4, 5, 6]
print(value)

# na zecie

z1 = {1, 2, 3}
z2 = {1, 4}
print(z1 & z2)
print(z1 | z2)
print(z1 - z2)
print(z1 ^ z2)

slow1 = {"1":1}
slow2 = {"2":2}
slow3 = {}
print(slow1)
slow1 |= slow2
slow3 |= slow1
print(slow1)
print(slow3)

#print(slow1 |slow2)
# w wynikowym obiekcie zachowywane sa klucze z prawegoobiektu -
# pamoietaj o tym gdy klucze sie powtarzaja (lewy modyfikowany jest wartosciami z prawego
#print({"1": 1} | {"1": 2, "2": 3})
# a = {'a':1}
# b = {'a':3, 'b':2}
# print({**a, **b}
#
# #rozpakowywanie słownika powyżej
# #met chain map