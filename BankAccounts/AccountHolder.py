class AccountHolder:
    def __init__(self, fname: str, lname: str):
        self.first_name = fname
        self.last_name = lname

    @property
    def first_name(self):
        return self._first_name

    @property
    def last_name(self):
        return self._last_name

    @first_name.setter
    def first_name(self, value: str):
        self._first_name = value

    @last_name.setter
    def last_name(self, value: str):
        self._last_name = value

    def __repr__(self):
        return f'{self.first_name} {self.last_name}'
