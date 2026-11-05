#Slovnik

kontakty = {
    "jmeno": "Jan",
    "prijmeni": "Novak",
    "vek": 30,
    "telefon": "123456789",
    "email": "Jan.novak@seznam.cz",
    "oblibene_jidlo": ["pizza", "sushi", "tacos"],
    "oblibene_barvy": ["modra", "zelena", "cervena"]
}
#vytiskne celou data strukturu
telefon = kontakty.get("telefon")
print("Telefoní číslo:", telefon)
print(f"Telefoní číslo: {telefon}")


