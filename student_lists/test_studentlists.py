"""
Practice using

 assertTrue
 assertFalse
 assertIsNone
 assertIsNotNone
 assertIn
 assertNotIn

"""

from studentlists import ClassList, StudentError
from unittest import TestCase

class TestStudentLists(TestCase):

    def test_add_student_check_student_in_list(self):
        test_class = ClassList(2)
        test_class.add_student('Test Student')
        self.assertIn('Test Student', test_class.class_list)

        test_class.add_student('Another Test Student')
        self.assertIn('Test Student', test_class.class_list)
        self.assertIn('Another Test Student', test_class.class_list)

    def test_add_student_already_in_list(self):
        test_class = ClassList(2)
        test_class.add_student('Test Student')
        with self.assertRaises(StudentError):
            test_class.add_student('Test Student')

    def test_add_remove_student_ensure_removed(self):
        test_class = ClassList(2)
        test_class.add_student('Test Student')
        test_class.remove_student('Test Student')
        self.assertNotIn('Test Student', test_class.class_list)

    def test_add_example_student_and_remove_student_not_in_list(self):
        test_class= ClassList(3)
        test_class.add_student('Mariah Carey')
        test_class.add_student('Joey Jackson')
        with self.assertRaises(StudentError):
            test_class.remove_student('Hannah Montana')

    def test_remove_student_from_an_empty_list(self):
        test_class=ClassList(2)
        with self.assertRaises(StudentError):
         test_class.remove_student('')

    def test_is_enrolled_when_student_present(self):
        test_class = ClassList(2)
        test_class.add_student('Snoop Dogg')
        test_class.add_student('Martha Stewart')
        self.assertTrue(test_class.is_enrolled('Snoop Dogg'))
        self.assertTrue(test_class.is_enrolled('Martha Stewart'))

    def test_is_enrolled_empty_class_list(self):
        test_class = ClassList(2)
        self.assertFalse(test_class.is_enrolled('Snoop Dogg'))

    def test_is_enrollled_with_students_not_enrolled(self):
        test_class=ClassList(2)
        test_class.add_student('Michael Janson')
        test_class.add_student('Hailey Beiber')
        self.assertFalse(test_class.is_enrolled('Jannet Michael'))

    def test_string_with_students_enrolled(self):
        test_class = ClassList(2)
        test_class.add_student('Taylor Swift')
        test_class.add_student('Kanye West')
        self.assertEqual('Taylor Swift, Kanye West', str(test_class))

    def test_string_empty_class(self):
        test_class = ClassList(2)
        self.assertEqual('', str(test_class))

    def test_index_of_student_student_present(self):
        test_class = ClassList(3)
        test_class.add_student('Harry')
        test_class.add_student('Hermione')
        test_class.add_student('Ron')

        self.assertEqual(1, test_class.index_of_student('Harry'))
        self.assertEqual(2, test_class.index_of_student('Hermione'))
        self.assertEqual(3, test_class.index_of_student('Ron'))

      
        self.assertIsNotNone(test_class.index_of_student('Harry'))

    def test_index_of_student_is_none_if_class_list_is_empty(self):
        test_class=ClassList(3)
        index = test_class.index_of_student('Test Student')
        self.assertIsNone(index)

    def test_index_of_student_is_none_if_class_is_not_empty_but_student_not_in_list(self):
        test_class=ClassList(3)
        index = test_class.index_of_student('Lily Miguire', test_class.class_list)
        self.assertIsNone(index)
   
    ## TODO write a test for your new is_class_full method when the class is full. 
    # use assertTrue.
    
    ## TODO write a test for your new is_class_full method for when is empty, 
    # and when it is not full. Use assertFalse.
