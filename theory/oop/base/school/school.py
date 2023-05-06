from bases.theory.classes.base.school.ClassRoom import ClassRoom
from bases.theory.classes.base.school.student import Student


class School:

    # Class constructor called by new class instance creation school()
    def __init__(self, name: str):
        self.name = name
        self.student_list = []
        self.class_room_list = []

    # String representation of the class instances of school
    def __str__(self):
        return self.name

    def build_class_room(self, number: str):
        new_room = ClassRoom(number)
        self.class_room_list.append(new_room)

    # Register a student to the school
    def register_student(self, student: Student):
        # Check if the student is already registered
        if student in self.student_list:
            print(f'{student} is already registered in {self.name}')
        else:
            # We add the student to the list of students from the school
            self.student_list.append(student)
            print(f'{student} accepted to {self.name}')

    def print_students(self):
        """Print the list of students"""

        if not self.student_list:
            print(f'{self} has no students')
        else:
            print(f'{self} has following {len(self.student_list)} students:')
            for student in self.student_list:
                print(f' - {student}')
