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
cur.execute("CREATE TABLE engagement(contractId SERIAL PRIMARY KEY, clientName VARCHAR(50), contractName VARCHAR(150),  clientPhoneNumber VARCHAR(20), contractStatus VARCHAR(50))")
conn.commit()

# Create a Faker object
fake = Faker()

# Insert fake data into the table
for _ in range(50):
    cur.execute(
        "INSERT INTO engagement (clientName, contractName, clientPhoneNumber, contractStatus) VALUES (%s, %s, %s, %s)",
        (fake.name(),fake.job(), fake.phone_number(), fake.random_element(elements=("Active", "Inactive", "Expired")))
    )
conn.commit()

# Close the cursor and connection
cur.close()
conn.close()
