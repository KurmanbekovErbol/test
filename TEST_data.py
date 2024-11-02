import sqlite3

class DatabaseManager:
    def __init__(self, db_name="users.db"):
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS users(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                email TEXT UNIQUE NOT NULL,
                age INTGER NOT NULL
            )            
""")
        
    def admins_table(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS admins(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                email TEXT UNIQUE NOT NULL,
                age INT NOT NULL,
                level INT NOT NULL
            )            
""")

    def customers_table(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS customers(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                email TEXT UNIQUE NOT NULL,
                age INTGER NOT NULL,
                rating TEXT
            )            
""")

    def add_user(self, user):
        self.cursor.execute("INSERT INTO users (name, email, age) VALUES (?, ?, ?)", (user.name, user.email, user.age))

        self.connection.commit()

    def add_admin(self, admin):
        self.cursor.execute("INSERT INTO users (name, email, age, level) VALUES (?, ?, ?, ?)", (admin.name, admin.email, admin.age, admin.level))

        self.connection.commit()

    def add_customer(self, customer):
        self.cursor.execute("INSERT INTO users (name, email, age, rating) VALUES (?, ?, ?, ?)", (customer.name, customer.email, customer.age, customer.rating))

        self.connection.commit()

    def get(self, id):
        self.cursor.execute("SELECT * FROM users WHERE id = ?", (id,))
        return self.cursor.fetchone()
    
    def delete(self, name):
        self.cursor.execute("DELETE FROM users WHERE name = ?", (name,))
        self.connection.commit()
        print(f"Пользователь {name} удален(а)")

    def get_user(self, name):
        self.cursor.execute("SELECT * FROM users WHERE name = ?", (name,))
        return self.cursor.fetchone()

    
    
    def close(self):
        self.connection.close()