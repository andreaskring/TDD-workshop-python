import unittest


class TestPerson(unittest.TestCase):

    def test_should_fail(self):
        self.assertTrue(False)


if __name__ == '__main__':
    unittest.main()
