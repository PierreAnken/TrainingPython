from student_exercices.Tobias.poo_vs_procedural.poo.Auto import Auto
from student_exercices.Tobias.poo_vs_procedural.poo.Garage import Garage
from student_exercices.Tobias.poo_vs_procedural.poo.Land import Land
from student_exercices.Tobias.poo_vs_procedural.poo.Owner import Owner

if __name__ == '__main__':

    de_land = Land('DE')
    it_land = Land('IT')
    tintin = Owner('Tintin')

    autos_g1 = [
        Auto("Audi", 11, de_land),
        Auto("BMW", 12, de_land, tintin),
        Auto("Mercedes", 13, de_land, tintin)
    ]

    garage_1 = Garage(autos=autos_g1)

    autos_g2 = [
        Auto("Lambo", 14, it_land),
        Auto("Ferrari", 25000, it_land),
    ]

    garage_2 = Garage(autos=autos_g2)

    garage_1.print_garage()
