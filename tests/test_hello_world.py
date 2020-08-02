# from src.hello_world import Student
import unittest

from src.hello_world import Student


class TestHelloWorld(unittest.TestCase):

    def test_get_student_detail_when_name_is_none_rollno_is_none(self):
        self.assertEqual(Student().get_student_detail(),"name:None roll_no:None")

    def test_get_student_detail_when_name_is_manish_rollno_is_none(self):
        student = Student()
        student.set_student_name("manish")
        self.assertEqual(student.get_student_detail(),"name:manish roll_no:None")

    def test_get_student_detail_when_name_is_none_rollno_is_160109022(self):
        student = Student()
        student.set_student_roll_no(160109022)
        self.assertEqual(student.get_student_detail(),"name:None roll_no:160109022")


if __name__ == '__main__':
    unittest.main()