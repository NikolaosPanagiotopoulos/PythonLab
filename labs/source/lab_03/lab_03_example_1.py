number = input("Δώσε έναν αριθμό: ")

if number.isdigit() is True:
	number = int(number)
	if number == 0:
		print("Μηδέν")
	else:
		print("Άλλος αριθμός")
