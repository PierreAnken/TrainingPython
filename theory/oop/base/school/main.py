from bases.theory.classes.base.school.school import School
from bases.theory.classes.base.school.student import Student

if __name__ == '__main__':
    school_1 = School(name='Montreux school')

    s1 = Student('Pierre', 'Anken')
    s2 = Student('Iman', 'Julaidan')

    school_1.register_student(s1)
    school_1.register_student(s2)

    school_1.build_class_room('A100')
    school_1.build_class_room('A200')


