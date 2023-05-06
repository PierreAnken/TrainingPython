from student_exercices.Benjamin.archery.Archer import Archer
from student_exercices.Benjamin.archery.ArrowType import ArrowType
from student_exercices.Benjamin.archery.Bow import Bow
from student_exercices.Benjamin.archery.Quiver import Quiver
from student_exercices.Benjamin.archery.Target import Target

archer = Archer(1000, 'MAX MUSTERMANN')
quiver = Quiver(10, 81, 'BEARPAW Rückenköcher Back Pack Traditional')
bow = Bow(479, 0.9, 8, 'DRAKE Pathfinder Green Complete - 40-65 lbs - Compoundbogen')
arrow = ArrowType(5.60, 0.8, 'Komplettpfeil | PICEA - Holz - mit Naturfedern | 28-32 Zoll')


archer.buy(quiver, 1)
archer.buy(bow, 1)
archer.buy(arrow, 20)

archer.equipe(bow)
archer.equipe(quiver)

target_1m = Target(100,3)
print(target_1m.compute_points(0,0))
print(target_1m.compute_points(200,0))
print(target_1m.compute_points(25,25))

