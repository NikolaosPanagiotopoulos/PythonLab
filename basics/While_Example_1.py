"""
Να γράψετε πρόγραμμα το οποίο να διαβάζει το μισθό των υπαλλήλων 
μιας εταιρείας και να υπολογίζει και να εμφανίζει τον μέσο όρο των 
μισθών. Η διαδικασία να επαναλαμβάνεται μέχρι να μας δοθεί μισθός 
μικρότερος ή ίσος του 0.
"""

# Το πρόγραμμα δεν έχει τελειώσει ακόμα!
employee =[]
sal = 1

while sal > 0:
    sal = int(input("Enter a salary: "))
    employee.append(sal)
    sal = sal + 0
    average = sal/len(employee)
print(average)