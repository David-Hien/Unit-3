## Code
``` python
# Import libraries
import sqlite3
import random


class ElectricCars:
    """ This class represents Electric cars"""
    def __init__(self):
        self.name = "Quiz_039.db"
        self.connection = sqlite3.connect(self.name)
        self.cursor = self.connection.cursor()

    # This method creates the table (if not exist) for Electric cars in the database
    def create_db(self):
        # This command uses sqlite to operate the database
        self.cursor.execute("""CREATE TABLE if not exists Electric_cars(
            id INTEGER primary key,
            brand VARCHAR(255),
            model VARCHAR(255),
            maker VARCHAR(255),
            battery_size INTEGER
            );""")
        
        # Run the command above
        self.connection.commit()

    # This method insert the new values into the table in the database
    def insert_db(self):
        id = random.randint(1, 100000)
        self.cursor.execute(f"INSERT INTO Electric_cars values({id}, 'Tesla', 'Model S', 'Elon Musk', 500);")
        self.connection.commit()


# Run
Quiz_039 = ElectricCars()
Quiz_039.create_db()
Quiz_039.insert_db()

```

## Run
