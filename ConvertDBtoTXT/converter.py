import sqlite3 as sql
conn = sql.connect("convertDBtoTXT\deals.db")
cur = conn.cursor()
query = cur.execute("SELECT id, brand, model, price, year, mileage FROM cars")

with open("convertDBtoTXT\cars.txt","w") as f:
    for el in query:
        f.write(f"{el[0]},{el[1]},{el[2]},{el[3]},{el[4]},{el[5]}\n")
        