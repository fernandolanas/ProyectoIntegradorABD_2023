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
cur.execute("CREATE TABLE location(locationId SERIAL PRIMARY KEY, province VARCHAR(150), City VARCHAR(150))")
conn.commit()

# Create a Faker object
fake = Faker()

# Insert fake data into the table
for _ in range(50):
    cur.execute(
        "INSERT INTO location (province, City) VALUES (%s, %s)",
        (fake.state(), fake.city())
    )
conn.commit()

# Close the cursor and connection
cur.close()
conn.close()
