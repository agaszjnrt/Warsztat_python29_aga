from pprint import pprint


first_name = "Jan"
last_name = "Kowalski"
height = 168
weight = 70

user = {
    "first_name": first_name,
    "last_name": last_name,
    "display_name": f"{first_name} {last_name}",
    "height": height,
    "weight": weight,
    "bmi": weight / (height / 100) ** 2,
}

if __name__ == "__main__":
    pprint(user)
#wersja z przypisaniem = dopieszczanie kodu
from pprint import pprint


user = {
    "first_name": (first_name := "Jan"),
    "last_name": (last_name := "Kowalski"),
    "display_name": f"{first_name} {last_name}",
    "height": (height := 168),
    "weight": (weight := 70),
    "bmi": weight / (height / 100) ** 2,
}

if __name__ == "__main__":
    pprint(user)


