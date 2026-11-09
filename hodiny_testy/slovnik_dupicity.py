cislo_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 9, 9, 9, 9, 9, 9,]
unikatni_cisla = set(cislo_list)
print("unikatní čísla:", unikatni_cisla)
print("puvodní seznam:", cislo_list)

prazdna_mnozina = set()
prazdna_mnozina.add(150)
prazdna_mnozina.add(90)

print("mnozina po přidánní prvků:", prazdna_mnozina)

if 5 in unikatni_cisla:
    print("Číslo 5 je v množině unikatnich_čísel.")

else:
    print("Číslo 5 ---NENÍ--- v množině unikatnich_čísel.")
    