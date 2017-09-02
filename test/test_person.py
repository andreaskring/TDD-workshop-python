import unittest

from production.person import Person


class TestPerson(unittest.TestCase):

    # Testing get_name

    def test_should_return_clint_when_name_is_clint(self):
        person = Person('Clint')
        self.assertEqual('Clint', person.get_name())

    def test_should_return_bruce_when_name_is_bruce(self):
        person = Person('Bruce')
        self.assertEqual('Bruce', person.get_name())

    def test_should_raise_exception_if_name_blank(self):
        with self.assertRaises(ValueError):
            Person('')

if __name__ == '__main__':
    unittest.main()
