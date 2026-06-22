import user_type;

class Admin(User):

    def __init__(
        self,
        age,
        email,
        home_address,
        name,
        password,
        phone
    ):
        super().__init__(
            age,
            email,
            home_address,
            name,
            password,
            phone,
            user_type.ADMIN
        )