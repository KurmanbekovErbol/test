from TEST_data import DatabaseManager

class User:
    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age

class UserService:
    def __init__(self, db_name="users.db"):
        self.db = DatabaseManager(db_name)

    def add_user(self, user):
        if self.find_user_by_name(user.name):
            print("Пользователь уже существует")
            return
        self.db.add_user(user)
        print("Пользователь добавлен")

    def find_user_by_name(self, name):
        user_data = self.db.get_user(name)
        if user_data:
            return User(name=user_data[1], email=user_data[2], age=user_data[3])
        else:
            print("Не найдено")

    def delete_user_by_email(self, name):
        delete_user = self.find_user_by_name(name)
        if delete_user:
            self.db.delete(name)
        else:
            None

class Admin(User):
    def __init__(self, name, email, age, level):
        super().__init__(name, email, age)
        self.level = level

class Customer(User):
    def __init__(self, name, email, age, rating):
        super().__init__(name, email, age)
        self.rating = rating

    def close(self):
        self.db.close()

userService = UserService()
user = User("1",'1',1)
userService.add_user(user)