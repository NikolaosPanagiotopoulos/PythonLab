"""Άσκηση 2 – Lectures 4
Ένας φοιτητής ζήτησε από τους γονείς του να αγοράσει έναν H/Y
αξίας 3000€. Οι γονείς του συµφώνησαν να του δώσουν τα χρήµατα
µε τον εξής τρόπο: Την πρώτη εβδοµάδα θα του δώσουν 20€. Στο
τέλος κάθε εβδοµάδας θα του δίνουνε τα διπλάσια από αυτά που
του δώσανε την προηγούµενη εβδοµάδα µέχρι να συγκεντρωθεί το
ποσό που χρειάζεται.
Να γίνει πρόγραµµα σε Python το οποίο θα υπολογίζει και θα
εµφανίζει τον αριθµό των εβδοµάδων που χρειάστηκε ο φοιτητής
να πάρει τον Η/Υ καθώς και το πόσο που περισσεύει (αν περισσεύει).
"""

# Το πρόγραμμα δεν έχει τελειώσει ακόμα!

money = 20
weeks = 0
i = 0

while money <= 3000:
    money = 2 * money
    i += 1
print(i)
