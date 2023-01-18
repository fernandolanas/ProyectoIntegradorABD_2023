from faker import Faker
import random
import psycopg2
 
# Connect to the PostgreSQL database
connection = psycopg2.connect(
    host="hostname",
    database="database_name",
    user="username",
    password="password"
)
 
cursor = connection.cursor()
 
# Create the 'client' table
cursor.execute('''CREATE TABLE client(clientId serial, clientName varchar(150), clientLastName varchar(150), clientPhoneNumber varchar(150));''')
 
# Use Faker to generate fake data for the table
faker = Faker()
for _ in range(50):
    client_name = faker.first_name()
    client_last_name = faker.last_name()
    client_phone_number = faker.phone_number()
 
    # Insert the fake data into the 'client' table
    cursor.execute(f"INSERT INTO client (clientName, clientLastName, clientPhoneNumber) VALUES ('{client_name}', '{client_last_name}', '{client_phone_number}')")
 
# Commit the changes and close the connection
connection.commit()
connection.close()
