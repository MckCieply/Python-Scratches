import sqlite3 as sql
conn = sql.connect("convertDBtoTXT\deals.db")
cur = conn.cursor()
query = cur.execute("SELECT id, brand, model, price, year, mileage FROM cars")

