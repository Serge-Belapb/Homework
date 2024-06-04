import sqlite3


con = sqlite3.connect('BaseUsers.db')
cur = con.cursor()

newTable = """CREATE TABLE IF NOT EXISTS users(
               userid INTEGER PRIMARY KEY AUTOINCREMENT,
               name TEXT,
               login TEXT,
               password TEXT
               sub_date TEXT
               sub_mode TEXT);
            """
cur.execute(newTable)
con.commit()

sql = "INSERT INTO users (name, login, password, sub_date, sub_mode) " \
      "VALUES ('Иванов', 'Ivan_v', 'Iva0V', '12.11.2021', 'free')"

# sql = "SELECT * FROM users WHERE name = 'uuu2'"

# sql = "UPDATE users SET password = 'qqqqq' WHERE name = 'uuu2' AND login = 'lll'"

# sql =  "DELETE FROM users WHERE name = 'uuu2' AND login = 'lll'"

with con:
    q = cur.execute(sql)
print(len(q))