# 4 Εντολή επιλογής - επανάληψης

---

## Περιεχόμενα

---

- 4.1 Παράδειγμα
- 4.2 Εντολή επανάληψης while
- 4.3 While παράδειγμα
- 4.4 Έλεγχος ορθότητας
- 4.5 Ασκήσεις

## [4.1 If Παράδειγμα](source/lab_04/lab_04_example_1.py)

---

```python
# Διάβασμα από τον χρήστη
number = input("Δώσε έναν αριθμό: ")

# Έλεγχος αν είναι αριθμός
if number.isdigit() is True:
  # Μετατροπή από str σε int
  number = int(number)
  if number == 0:
    print("Μηδέν")
  elif(number % 2) == 0:
    print("Άρτιος")
  else:
    print("Περιττός")
```

Για να κατεβάσετε τον κώδικα πατήστε [εδώ](source/lab_04/lab_04_example_1.py)

[![Video 8](../images/Video_1.PNG)](https://www.youtube.com/watch?v=oVyvV9fyMqA&list=PLlRCU8UBnRzRipr_LhWiF3YCoEkHUleLK&index=11)

## 4.2 Εντολή επανάληψης while

---

**ΠΡΟΣΟΧΗ!** Ένα while πρέπει **ΠΑΝΤΑ** να μεταβάλλει τουλάχιστον μία από τις μεταβλητές που ανήκουν στο *CONDITION*, αλλιώς θα δημιουργηθεί ένας ατέρμων βρόγχος (*infinite loop*).Δηλαδή το πρόγραμμα θα κολλήσει μέσα στον βρόγχο επ’ άπειρων.

## [4.3 While παράδειγμα](source/lab_04/lab_04_example_2.py)

---

Να γραφεί ένα πρόγραμμα το οποίο διαβάζει 10 αριθμούς και τυπώνει το άθροισμα τους.

```python
# Αρχικοποίηση μεταβλητών
i = 0
synolo = 0

while i < 10:
  number = int(input("Δώσε αριθμό: "))
  synolo = synolo + number
  i = i + 1

# Εκτύπωση αποτελέσματος
print("Το σύνολο είναι:", synolo)
```

Για να κατεβάσετε τον κώδικα πατήστε [εδώ](source/lab_04/lab_04_example_2.py)

[![Video 9](../images/Video_1.PNG)](https://www.youtube.com/watch?v=TllJBVYcrwU&list=PLlRCU8UBnRzRipr_LhWiF3YCoEkHUleLK&index=12)

## [4.4 Έλεγχος ορθότητας](source/lab_04/lab_04_example_3.py)

---

Να γραφεί ένα πρόγραμμα το οποίο διαβάζει 10 αριθμούς και τυπώνει το άθροισμα τους. Εάν ο χρήστης δεν εισάγει αριθμό, να επαναλαμβάνεται η ερώτηση.

```python
# Αρχικοποίηση μεταβλητών
i = 0
synolo = 0

while i < 10:
  number = input("Δώσε αριθμό: ")
  # Έλεγχος ορθότητας
  while not number.isdigit():
    number = input("Είπα δώσε αριθμό: ")
  number = int(number)
  synolo = synolo + number
  i = i + 1

# Εκτύπωση αποτελέσματος
print("Το σύνολο είναι:", synolo)
```

Για να κατεβάσετε τον κώδικα πατήστε [εδώ](source/lab_04/lab_04_example_3.py)

[![Video 10](../images/Video_1.PNG)](https://www.youtube.com/watch?v=7WAnutfgA_4&list=PLlRCU8UBnRzRipr_LhWiF3YCoEkHUleLK&index=13)

## 4.5 Ασκήσεις

---

### [Άσκηση 1](source/lab_04/lab_04_exercise_1.py)

Να γραφεί πρόγραμμα το οποίο:

1. Θα διαβάζει το αποτέλεσμα 2 ζαριών.
2. Θα ελέγχει αν ο χρήστης εισήγαγε σωστά νούμερα (1-6), αλλιώς θα εμφανίζει μήνυμα λάθους και θα τερματίζει.
3. Αν τα ζάρια ήταν τεσσάρια, θα τυπώνει «Ντορτια».
4. Αν τα ζάρια ήταν 1 και 2, θα τυπώνει «Ασσόδυο».
5. Αν τα ζάρια ήταν διπλά, θα τυπώνει «Διπλές» και το αποτέλεσμα.
6. Αλλιώς θα τυπώνει το αποτέλεσμα της ζαριάς.

```python
# Εισαγωγή δεδομένων
zaria1 = input("Δώσε 1η ζαριά: ")
zaria2 = input("Δώσε 2η ζαριά: ")

# Ελέγχουμε αν αυτό που έγραψε o χρήστης είναι νούμερα.
if zaria1.isdigit() and zaria2.isdigit():
  # Μετατροπή από str σε int
  zaria1 = int(zaria1)
  zaria2 = int(zaria2)
  # Ελέγχουμε αν τα νούμερα των ζαριών ήταν μεταξύ 1 - 6.
  if (zaria1 >= 1 and zaria1 <= 6) and (zaria2 >= 1 and zaria2 <= 6):
    if zaria1 == 4 and zaria2 == 4:
      print("Ντόρτια")
    elif (zaria1 == 1 and zaria2 == 2) or (zaria1 == 2 and zaria2 == 1):
      print("Ασσόδυο")
    elif zaria1 == zaria2:
      print("Διπλές", zaria1 + zaria2)
    else:
      print(zaria1 + zaria2)
  else:
    print("Γιατί οι ζαριές είναι εκτός ορίων 1 και 6;")
else:
  print("Γιατί έγραψες λέξη;")
```

Για να κατεβάσετε τον κώδικα πατήστε [εδώ](source/lab_04/lab_04_exercise_1.py)

[![Video 11](../images/Video_1.PNG)](https://www.youtube.com/watch?v=lIKLAjDxl-A&list=PLlRCU8UBnRzRipr_LhWiF3YCoEkHUleLK&index=14)

### [Άσκηση 2](source/lab_04/lab_04_exercise_2.py)

Ένας φοιτητής πρέπει να περάσει 6 μαθήματα σε ένα εξάμηνο. Να γραφεί πρόγραμμα που να διαβάζει τους βαθμούς του φοιτητή και να υπολογίζει το μέσο όρο της βαθμολογίας του για το συγκεκριμένο εξάμηνο. Ανάλογα με το μέσο όρο να εμφανίζεται το μήνυμα «Άριστα» (8,5-10), «Λίαν Καλώς» (6,5-8,49) και «Καλώς» (5-6,49).

```python
# Αρχικοποίηση μεταβλητών
i = 0
athroisma = 0

while i < 6:
  # Εισαγωγή βαθμού και μετατροπ΄ή από str σε float
  vathmos = float(input("Δώσε βαθμό: "))
  athroisma = athroisma + vathmos
  i = i + 1

# Υπολογισμός μέσου όρου
mo = athroisma / 6

if mo > 10:
  print("Κάτι δεν πάει καλά...")
elif mo >= 8.5:
  print("Άριστα!")
elif mo >= 6.5:
  print("Λίαν Καλώς")
elif mo >= 5:
  print("Καλώς")
else:
  print("Kόπηκες")
```

Για να κατεβάσετε τον κώδικα πατήστε [εδώ](source/lab_04/lab_04_exercise_2.py)

[![Video 12](../images/Video_1.PNG)](https://www.youtube.com/watch?v=6u4uAYDxuoY&list=PLlRCU8UBnRzRipr_LhWiF3YCoEkHUleLK&index=15)

### [Άσκηση 3](source/lab_04/lab_04_exercise_3.py)

Μία χρονιά έχει 365 μέρες. Όμως, ο χρόνος που χρειάζεται η γη για να περιστραφεί γύρω από τον ήλιο είναι λίγο μεγαλύτερος. Για αυτό, μερικές χρονιές χρειάζεται να προσθέτουμε την 29η Φεβρουαρίου για να διορθωθεί αυτό το σφάλμα. Αυτά τα έτη, που ονομάζονται δίσεκτα
υπολογίζονται ως εξής:

1. Αν ένα έτος διαιρείται με το 4, είναι δίσεκτο.
2. Αν όμως διαιρείται με το 100, δεν είναι. Εκτός αν διαιρείται με το 400.

Για παράδειγμα:

- το έτος 2016 ήταν δίσεκτο, επειδή διαιρείται με το 4.
- το έτος 1900 δεν ήταν δίσεκτο, επειδή διαιρείται με το 100.
- το έτος 2000 ήταν δίσεκτο, καθώς παρόλο που διαιρείται με το 100, διαιρείται και με το 400.

Να γραφεί πρόγραμμα το οποίο θα δέχεται ένα έτος και θα εμφανίζει μήνυμα αναφέροντας αν ήταν δίσεκτο ή όχι.

```python
# Διάβασμα έτους
etos = int(input("Δώσε έτος: "))

# Αν διαιρείται με 4 είναι δίσεκτο
if etos % 4 == 0:
  # Εκτός και αν διαιρείται και με 100
  if etos % 100 == 0:
    # Aλλα και σε αυτήν την περίπτωση αν διαιρείται με 400 είναι δίσεκτο
    if etos % 400 == 0:
      disekto = True
    else:
      disekto = False
  else:
    disekto = True
else:
  disekto = False

# Eκτύπωση αποτελέσματος
if disekto:
  print("Είναι δίσκετο")
else:
  print("Δεν είναι δίσεκτο")
```

Για να κατεβάσετε τον κώδικα πατήστε [εδώ](source/lab_04/lab_04_exercise_3.py)

### [Άσκηση 4](source/lab_04/lab_04_exercise_4.py)

Να γραφεί ένα πρόγραμμα το οποίο θα δέχεται από τον χρήστη αριθμούς και θα υπολογίζει το γινόμενό τους. Το πρόγραμμα θα τερματίζει όταν ο χρήστης εισάγει τον αριθμό 0. Να γίνεται έλεγχος ορθότητας.

```python
# Αρχικοποίηση μεταβλητών
ginomeno = 0
arithmos = 1
flag = False

while arithmos != 0:
  # Διάβασμα από τον χρήστη
  arithmos = input("Δώσε αριθμό: ")
  # Έλεγχος ορθότητας
  while not arithmos.isdigit():
    arithmos = input("Δώσε σωστά αριθμό: ")
  # Μετατροπή από str σε int
  arithmos = int(arithmos)
  if flag is False and arithmos != 0:
    ginomeno = 1
    flag = True
  if arithmos != 0:
    ginomeno = ginomeno * arithmos

# Eκτύπωση αποτελέσματος
print("Γινόμενο:", ginomeno)   
```

Για να κατεβάσετε τον κώδικα πατήστε [εδώ](source/lab_04/lab_04_exercise_4.py)

### [Άσκηση 5](source/lab_04/lab_04_exercise_5.py)

Να γραφεί ένα πρόγραμμα το οποίο θα δέχεται από τον χρήστη έναν αριθμό και θα τυπώνει το άθροισμα των ψηφίων του.

```python
# Αρχικοποίηση μεταβλητών
athroisma = 0

# Διάβασμα από τον χρ΄ήστη και μετατροπ΄ή από str σε int
number = int(input("Δώσε αριθμό: "))

while number != 0:
  tel_pshfio = number % 10
  number = number // 10
  athroisma += tel_pshfio

# Eκτύπωση αποτελέσματος
print("Άθροισμα:", athroisma)
```

Για να κατεβάσετε τον κώδικα πατήστε [εδώ](source/lab_04/lab_04_exercise_5.py)

[Home](../README.md) | [Lab 1](lab_01.md) | [Lab 2](lab_02.md) | [Lab 3](lab_03.md) | [Lab 4](lab_04.md) | [Lab 5](lab_05.md) | [Lab 6](lab_06.md) | [Lab 7](lab_07.md) | [Lab 8](lab_08.md) | [Lab 9](lab_09.md) | [Lab 10](lab_10.md)
