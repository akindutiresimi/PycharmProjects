import unittest

from student.Student import Student
class MyTestCase(unittest.TestCase):

    def test_that_student_name_and_show_which_grade_the_student(self):
        student = Student("John Dan", 9)
        self.assertEqual(student.name, "John Dan")
        self.assertEqual(student.show_gradelevel, 9)
         # add assertion here

    def test_that_student_name_and_show_that_gradelevel_increase_by_one(self):
        student = Student("John Dan", 9)
        self.assertEqual(student.promotion(),10)

    def test_that_student_pass_by_taking_the_student_score(self):
        student = Student("John Dan", 9)
        self.assertEqual(student.has_passed(70),True)

    def test_that_student_update_is_name(self):
        student = Student("John Dan", 9)
        self.assertEqual(student.update_name("Emma Joshua"), "Emma Joshua")

    def test_that_wether_student_is_in_final_graduating_year(self):
        student = Student("John Dan", 9)
        self.assertEqual(student.show_gradelevel, 9)
        self.assertEqual(student.is_graduating(),False)

if __name__ == '__main__':
    unittest.main()
