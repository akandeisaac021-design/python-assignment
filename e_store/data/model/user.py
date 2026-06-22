import user_type;

class User:

    def __init__(
        self,
        age,
        email,
        home_address,
        name,
        password,
        phone,
        user_type
    ):
        self.age = age
        self.email = email
        self.home_address = home_address
        self.name = name
        self.password = password
        self.phone = phone
        self.user_type = user_type
