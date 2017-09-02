import unittest

from production.person import Person


class TestPerson(unittest.TestCase):

    # Testing get_name

    def setUp(self):
        self.person1 = Person('Clint', '010117-1111')
        self.person2 = Person('Bruce', '010117-1112')

    def test_should_return_clint_when_name_is_clint(self):
        self.assertEqual('Clint', self.person1.get_name())

    def test_should_return_bruce_when_name_is_bruce(self):
        self.assertEqual('Bruce', self.person2.get_name())

    def test_should_raise_exception_if_name_blank(self):
        with self.assertRaises(ValueError):
            Person('', '010117-1111')

    # Testing set_name

    def test_should_return_name_chuck_when_name_is_set_chuck(self):
        self.person1.set_name('Chuck')
        self.assertEqual('Chuck', self.person1.get_name())

    def test_should_return_name_harry_when_name_is_set_harry(self):
        self.person1.set_name('Harry')
        self.assertEqual('Harry', self.person1.get_name())

    def test_should_raise_exception_if_name_is_set_to_blank(self):
        with self.assertRaises(ValueError):
            self.person1.set_name('')

    # Testing get_cpr_number

    def test_should_return_010117_1111_when_cpr_is_010117_1111(self):
        self.assertEqual('010117-1111', self.person1.get_cpr_number())

    def test_should_return_010117_1112_when_cpr_is_010117_1112(self):
        self.assertEqual('010117-1112', self.person2.get_cpr_number())


if __name__ == '__main__':
    unittest.main()
