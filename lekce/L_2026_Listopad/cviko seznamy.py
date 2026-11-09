import math
#proměnné a retezce
jmeno = "Petr"
vek = 25
print(f"jmenuji se {jmeno}a je mi {vek} let")

numbers = [8, 7, 6, 5, 4]
numbers.sort()
print(f"seřazený seznam: {numbers}")
print(f"První prvek seznamu: {numbers[0]}")
print(f"Poslední prvek seznamu: {numbers[-1]}")
#Slovníky a mnoziny
student = {
    "jmeno": "Radek",
    "věk": 20,
    "predmety": ["Matematika", "Informatika"]
}

student [vek] = 25
student ["jmeno"] = "Petr"
student ["předměty"] = ["Matematika", "Fyzika", "Informatika"]
print ("student: ", student)

data = [3,3,3,3,3,3,3,3,5,6,7,9,9,9,9,9,9]
unique_data = set(data)
print(f"Unikátní hodnoty: {unique_data}")

for i in range(1, 11):
    if i % 3 == 0:              #delení 3
        print("fizz")
    elif i % 5 == 0:              #delení 5
        print("je delitelné 5")
    else:
        print(i)

def vypočet_obvodu_obdelníku(delka, šířka=None):
    if šírka is None:
        šírka = delka
    return 2 * (delka + šírka)
delka = 5
šířka = 3

print(f"obvod obdelníku s delkou {{delka}} a  sirkou {{šířka}} je: {{vypočet_obvodu_obdelníku(delka, šířka)}}")