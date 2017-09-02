import unittest

from production.person import Person


class TestPerson(unittest.TestCase):

    # Testing get_name

    def setUp(self):
        self.person = Person('Clint')

    def test_should_return_clint_when_name_is_clint(self):
        self.assertEqual('Clint', self.person.get_name())

    def test_should_return_bruce_when_name_is_bruce(self):
        person = Person('Bruce')
        self.assertEqual('Bruce', person.get_name())

    def test_should_raise_exception_if_name_blank(self):
        with self.assertRaises(ValueError):
            Person('')

    # Testing set_name

    def test_should_return_name_chuck_when_name_is_set_chuck(self):
        self.person.set_name('Chuck')
        self.assertEqual('Chuck', self.person.get_name())

    def test_should_return_name_harry_when_name_is_set_harry(self):
        self.person.set_name('Harry')
        self.assertEqual('Harry', self.person.get_name())

    def test_should_raise_exception_if_name_is_set_to_blank(self):
        with self.assertRaises(ValueError):
            self.person.set_name('')

if __name__ == '__main__':
    unittest.main()
