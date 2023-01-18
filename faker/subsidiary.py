from faker import Faker
import psycopg2

# Connect to the database
conn = psycopg2.connect(
    host="hostname",
    database="database_name",
    user="username",
    password="password"
)

# Create a cursor object
cur = conn.cursor()

# Create the table
cur.execute("CREATE TABLE subsidiary(subsidiaryId SERIAL PRIMARY KEY, subsidiaryName VARCHAR(150), phoneNumber VARCHAR(150))")
conn.commit()

# Create a Faker object
fake = Faker()

# Insert fake data into the table
for _ in range(50):
    cur.execute(
        "INSERT INTO subsidiary (subsidiaryName, phoneNumber) VALUES (%s, %s)",
        (fake.company(), fake.phone_number())
    )
conn.commit()

# Close the cursor and connection
cur.close()
conn.close()
