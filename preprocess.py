import sqlite3

conn = sqlite3.connect('bus_delay_data')
cursor = conn.cursor()

print("Database connected succesfully")

conn.close()