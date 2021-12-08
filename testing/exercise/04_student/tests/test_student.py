from unittest import TestCase, main

from project.student import Student


class StudentTest(TestCase):
    VALID_NAME = 'Student'

    def setUp(self) -> None:
        self.student = Student(self.VALID_NAME)

    def test_init__expect_to_set_correct_values(self):
        student = Student(self.VALID_NAME, {'course 1': ['notes']})
        self.assertEqual(self.VALID_NAME, self.student.name)
        self.assertEqual({}, self.student.courses)
        self.assertEqual({'course 1': ['notes']}, student.courses)

    def test_enroll__when_course_name_in_the_courses_dict__expect_to_update_the_notes_and_return_correct_message(self):
        self.student.courses = {"course 1": []}
        msg = self.student.enroll("course 1", ["note 1", "note 2"])
        self.assertEqual("Course already added. Notes have been updated.", msg)
        self.assertEqual({"course 1": ["note 1", "note 2"]}, self.student.courses)

    def test_enroll__when_course_not_in_courses_dict_but_has_notes_to_add__expect_to_add_course_with_notes(self):
        self.student.courses = {}
        msg = self.student.enroll("course 1", ["note 1"])
        self.assertEqual("Course and course notes have been added.", msg)
        self.assertEqual({"course 1": ["note 1"]}, self.student.courses)

    def test_enroll__when_course_not_in_courses_dict_and_no_notes__expect_to_add_course_and_return_correct_message(self):
        self.student.courses = {}
        msg = self.student.enroll("course 1", ["note 1"], "Y")
        self.assertEqual("Course and course notes have been added.", msg)
        self.assertEqual({"course 1": ["note 1"]}, self.student.courses)

        self.student.courses = {}
        msg = self.student.enroll("course 1", ["note 1"], "N")
        self.assertEqual("Course has been added.", msg)
        self.assertEqual({"course 1": []}, self.student.courses)

    def test_add_notes__when_course_in_courses_dict__expect_to_add_notes_and_return_correct_message(self):
        self.student.courses = {'course 1': ['note 1', 'note 2']}
        expected_message = "Notes have been updated"

        result = self.student.add_notes('course 1', ['note 3', 'note 4'])

        self.assertEqual(expected_message, result)

    def test_add_notes__when_course_not_in_courses_dict__expect_exception(self):
        with self.assertRaises(Exception) as context:
            self.student.add_notes('course 25', ['note 1'])

        self.assertEqual("Cannot add notes. Course not found.", str(context.exception))

    def test_leave_course__when_course_in_courses_dict__expect_to_remove_it_and_return_correct_message(self):
        self.student.courses = {'course 1': ['note 1']}
        expected_message = "Course has been removed"

        result = self.student.leave_course('course 1')

        self.assertEqual(expected_message, result)

    def test_leave_course__when_course_not_in_courses_dict__expect_exception(self):
        with self.assertRaises(Exception) as context:
            self.student.leave_course('course 10')

        self.assertEqual("Cannot remove course. Course not found.", str(context.exception))


if __name__ == '__main__':
    unittest.main()
