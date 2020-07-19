class Student:
    def __init__(self):
        self.roll_no = None
        self.name = None

    def get_student_detail(self):
        return "name:{} roll_no:{}".format(self.name, self.roll_no)

    def set_student_name(self,name):
        self.name = name
    def set_student_roll_no(self,roll_no):
        self.roll_no = roll_no

if __name__ == '__main__':
    student1 = Student()
    student2 = Student()

    print(student1.get_student_detail())
    print(student2.get_student_detail())

    student1.set_student_roll_no(160109022)
    student1.set_student_name('manish')
    student2.set_student_roll_no(160109015)
    student2.set_student_name('samarth')

    print(student1.get_student_detail())
    print(student2.get_student_detail())

