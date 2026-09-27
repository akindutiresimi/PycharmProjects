import unittest

from student.student import Student
class MyTestCase(unittest.TestCase):
    def test_the_student_name_and_show_which_grade_the_student_has(self):
        student = Student()
        self.assertEqual(student.name, "John Dan")
        self.assertEqual(")


if __name__ == '__main__':
    unittest.main()
