from student_exercices.Benjamin.archery.Archer import Archer
from student_exercices.Benjamin.archery.ArrowType import ArrowType
from student_exercices.Benjamin.archery.Bow import Bow
from student_exercices.Benjamin.archery.Quiver import Quiver
from student_exercices.Benjamin.archery.Target import Target

archer = Archer(1000, 'MAX MUSTERMANN')
quiver = Quiver(10, 81, 'BEARPAW Rückenköcher Back Pack Traditional')
bow = Bow(479, 25, 'DRAKE Pathfinder Green Complete - 40-65 lbs - Compoundbogen')
arrow = ArrowType(5.60, 0.05, 'Komplettpfeil | PICEA - Holz - mit Naturfedern | 28-32 Zoll')

archer.buy(quiver, 1)
archer.buy(bow, 1)
archer.buy(arrow, 20)

archer.equipe(bow)
archer.equipe(quiver)

quiver.fill(9, arrow)

target_1m = Target(100, 3, 20)


sum_points = 0
for i in range(10):
    points = archer.shoot_arrow(target_1m)
    sum_points += points

print(f'Total points {sum_points}')
