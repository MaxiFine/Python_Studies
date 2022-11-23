# The Contact Class holds contact information


class Contact:
    # The __init__ method contact information
    def __init__(self, name, phone, email, address):
        self._name = name
        self._phone = phone
        self._email = email
        self._address = address

    # The set methods sets the name, phone, email attributes
    def set_name(self, name):
        self._name = name

    def set_phone(self, phone):
        self._phone = phone

    def set_email(self, email):
        self._email = email



    # The get methods returns the values that are stored in them
    def get_name(self):
        return self._name

    def get_phone(self):
        return self._phone

    def get_email(self):
        return self._email

    def __str__(self):
        return "Name: " + self._name + "\nPhone: " + self._phone + \
               "\nEmail: " + self._email
