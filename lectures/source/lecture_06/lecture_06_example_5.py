list = [3, 4, 1, 9, 4, 2]
maxThesi = 0
thesi = 0

for item in list:
    if item > list[maxThesi]:
        maxThesi = thesi
    thesi += 1

print("Μέγιστη θέση:", maxThesi)
