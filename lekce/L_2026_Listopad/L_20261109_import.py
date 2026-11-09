import math

print(f"Číslo pi: {math.pi}")
print(f"sinus 90 stupňů: {math.sin(math.pi / 2)}")

def bezpečné_dělení(a, b):
    try:
        vysledek = a / b
    except ZeroDivisionError as zde:
        print(f"Chyba: {zde}")
        return None
    except Exception as e:
         zprava = f"nelze delit objěkt {a} / {b}: {e}"
         raise Exception(zprava) 
    finally:
        print("Dělení bylo provedeno.")
        print("tento vysledek se pvede vždy")
    return vysledek

print(bezpečné_dělení(10, 2))
print(bezpečné_dělení(10, 0))

    