lista = []
i = 0

# Δίαβασμα πίνακα
while i < 10:
    number = int(input("Δώσε αριθμό: "))
    lista.append(number)
    i += 1

# Αρχικοποίηση μεταβλητών
j = 0
k = 0
m = 0
athroisma = 0
artios = 0
perittos = 0
megistos = lista[0]
elaxistos = lista[0]

# Yπολογισμός ζητούμενων
while j < 10:
    athroisma += lista[j]
    j = j + 1

print("Το άθροισμα είναι: ", athroisma)

while k < 10:
    if lista[k] % 2 == 0:
        artios += 1
    else:
        perittos += 1
    k += 1

print("To πλήθος των άρτιων είναι: ", artios, " Tο πλήθος των περιττών είναι: ", perittos)

while m < 10:
    if megistos < lista[l]:
        megistos = lista[l]

    if elaxistos > lista[l]:
        elaxistos = lista[l]

    m += 1
 
print("Η διαφορά είναι: ", megistos-elaxistos)
