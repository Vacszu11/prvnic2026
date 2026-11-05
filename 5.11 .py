def sčítání (a, b):
   # """"""funkce pro čítání dvou čísel.""""""
    return a + b

soucet = sčítání(5, 7)
print("Součet je:", soucet)

soucet2 = sčítání(a=10, b=15)
print("Součet je:", soucet2)

def delen(a, b):
    if b == 0:
        return "Nelze dělit nulou!"
    else:
        return a / b

print("Dělení je:", delen(b=4, a=8))