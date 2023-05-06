from student_exercices.Benjamin.classes.Auto import Auto

from student_exercices.Benjamin.classes.Parking import Parking

parking = Parking(5)

for x in range(10):
    if x % 2 == 1:
        parking.park_auto(Auto('schwarz'))
    else:
        parking.park_auto(Auto())

print(parking)