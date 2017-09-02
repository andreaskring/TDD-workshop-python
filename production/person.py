class Person(object):

    def __init__(self, name: str, cpr: str):
        self.set_name(name)
        self.cpr = cpr

    def get_cpr_number(self) -> str:
        """
        Get the CPR number of a person
        :return: CPR number, e.g. 241217-1111
        """
        return self.cpr

    def get_name(self) -> str:
        """
        Get the name of the person
        :return: Full name of the person.
        """
        return self.name

    def is_cpr_number_valid(self) -> bool:
        """
        Check if the CPR number is valid.
        :return: True if the CPR number is valid and False otherwise.
        """
        pass

    def set_name(self, name: str):
        """
        Set the name of the person.
        :param name: The full name of the person.
        :raises ValueError: If string is empty.
        """
        if not name:
            raise ValueError('Name cannot be blank!')
        self.name = name

    def get_address(self) -> str:
        """
        Get the address of the person from the CPR number.
        :return: The address of the person.
        """
        pass
