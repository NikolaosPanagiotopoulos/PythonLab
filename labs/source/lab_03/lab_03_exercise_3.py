# Διάβασμα αποτελεσμάτων
omada1 = input("Δώσε τους πόντους της ομάδας 1: ")
omada2 = input ("Δώσε τους πόντους της ομάδας 2: ")

# Έλεγχος αν είναι αριθμός
if not(omada1.isdigit() and omada2.isdigit()):
    # Ζήτα ξανά να διαβάσουμε αριθμό
    omada1 = input("Είπα δώσε πόντους για ομάδα 1: ")
    omada2 = input ("Είπα δώσε πόντους για ομάδα 2: ")

# Αφού ξέρουμε ότι είναι αριθμός
omada1 = int(omada1)
omada2 = int(omada2)

# Ελέγχουμε αν η ομάδα 1 συγκέντρωσε 25 βαθμούς
if omada1 == 25:
    print("Η ομάδα 1 κέρδισε!")
else:
    print("Η ομάδα 2 κέρδισε!")