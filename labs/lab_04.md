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
number = input("Δώσε έναν αριθμό: ")

if number.isdigit() == True:
  number = int(number)
  if number == 0:
    print("Μηδέν")
  elif(number % 2) == 0:
    print("Άρτιος")
  else:
    print("Περιττός")
```

Για να κατεβάσετε τον κώδικα πατήστε [εδώ](source/lab_04/lab_04_example_1.py)

## 4.2 Εντολή επανάληψης while

---

**ΠΡΟΣΟΧΗ!** Ένα while πρέπει **ΠΑΝΤΑ** να μεταβάλλει τουλάχιστον μία από τις μεταβλητές που ανήκουν στο *CONDITION*, αλλιώς θα δημιουργηθεί ένας ατέρμων βρόγχος (*infinite loop*).Δηλαδή το πρόγραμμα θα κολλήσει μέσα στον βρόγχο επ’ άπειρων.

## [4.3 While παράδειγμα](source/lab_04/lab_04_example_2.py)

---

Να γραφεί ένα πρόγραμμα το οποίο διαβάζει 10 αριθμούς και τυπώνει το άθροισμα τους.

```python
i = 0
synolo = 0

while i < 10:
  number = int(input("Δώσε αριθμό: "))
  synolo = synolo + number
  i = i + 1 

print("Το σύνολο είναι: ", synolo)
```

Για να κατεβάσετε τον κώδικα πατήστε [εδώ](source/lab_04/lab_04_example_2.py)

## [4.4 Έλεγχος ορθότητας](source/lab_04/lab_04_example_3.py)

---

Να γραφεί ένα πρόγραμμα το οποίο διαβάζει 10 αριθμούς και τυπώνει το άθροισμα τους. Εάν ο χρήστης δεν εισάγει αριθμό, να επαναλαμβάνεται η ερώτηση.

```python
i = 0
synolo = 0

while i < 10:
  number = input("Δώσε αριθμό: ")
  while not number.isdigit():
    number = input("Δώσε αριθμό: ")
  number = int(number)
  synolo = synolo + number
  i = i + 1 

print("Το σύνολο είναι:", synolo)
```

Για να κατεβάσετε τον κώδικα πατήστε [εδώ](source/lab_04/lab_04_example_3.py)

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

```

Για να κατεβάσετε τον κώδικα πατήστε [εδώ](source/lab_04/lab_04_exercise_1.py)

### [Άσκηση 2](source/lab_04/lab_04_exercise_2.py)

Ένας φοιτητής πρέπει να περάσει 6 μαθήματα σε ένα εξάμηνο. Να γραφεί πρόγραμμα που να διαβάζει τους βαθμούς του φοιτητή και να υπολογίζει το μέσο όρο της βαθμολογίας του για το συγκεκριμένο εξάμηνο. Ανάλογα με το μέσο όρο να εμφανίζεται το μήνυμα «Άριστα» (8,5-10), «Λίαν Καλώς» (6,5-8,49) και «Καλώς» (5-6,49).

```python

```

Για να κατεβάσετε τον κώδικα πατήστε [εδώ](source/lab_04/lab_04_exercise_2.py)

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

```

Για να κατεβάσετε τον κώδικα πατήστε [εδώ](source/lab_04/lab_04_exercise_3.py)

### [Άσκηση 4](source/lab_04/lab_04_exercise_4.py)

Να γραφεί ένα πρόγραμμα το οποίο θα δέχεται από τον χρήστη αριθμούς και θα υπολογίζει το γινόμενό τους. Το πρόγραμμα θα τερματίζει όταν ο χρήστης εισάγει τον αριθμό 0. Να γίνεται έλεγχος ορθότητας.

```python
ginomeno = 0
arithmos = 1
flag = False

while arithmos != 0:
  arithmos = input("Δώσε αριθμό: ")
  while not arithmos.isdigit():
    arithmos = input("Είπα δώσε αριθμό: ")
  arithmos = int(arithmos)
  if flag == False and arithmos != 0:
    ginomeno = 1
    flag = True
  if arithmos != 0:
    ginomeno = ginomeno * arithmos

print("Γινόμενο:", ginomeno)     
```

Για να κατεβάσετε τον κώδικα πατήστε [εδώ](source/lab_04/lab_04_exercise_4.py)

### [Άσκηση 5](source/lab_04/lab_04_exercise_5.py)

Να γραφεί ένα πρόγραμμα το οποίο θα δέχεται από τον χρήστη έναν αριθμό και θα τυπώνει το άθροισμα των ψηφίων του.

```python
athroisma = 0

number = int(input("Δώσε αριθμό: "))

while number != 0:
  tel_pshfio = number % 10
  number = number // 10
  athroisma += tel_pshfio

print("Άθροισμα:", athroisma)
```

Για να κατεβάσετε τον κώδικα πατήστε [εδώ](source/lab_04/lab_04_exercise_5.py)

[Home](../README.md) | [Lab 1](lab_01.md) | [Lab 2](lab_02.md) | [Lab 3](lab_03.md) | [Lab 4](lab_04.md) | [Lab 5](lab_05.md) | [Lab 6](lab_06.md) | [Lab 7](lab_07.md) | [Lab 8](lab_08.md) | [Lab 9](lab_09.md) | [Lab 10](lab_10.md)