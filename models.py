import sqlite3

class Product:
	def __init__(self):
		self.con = sqlite3.connect("test.db")
		self.cur = self.con.cursor()
		self.create_table()

	def create_table(self):
		# self.cur.execute("""DROP TABLE products""")
		self.cur.execute("""CREATE TABLE IF NOT EXISTS products
			date DATE PRIMARY KEY,
			sno REAL,
			team TEXT,
			won REAL,
			draw REAL,
			lost REAL,
			team_won REAL,
			team_draw REAL,
			team_lost REAL)""")

	def insert(self, item):
		self.cur.execute("""INSERT OR IGNORE INTO products VALUES(?,?,?,?,?,?,?,?,?)""", item)
		self.con.commit()

	def read(self):
		self.cur.execute("""SELECT * FROM products""")
		rows = self.cur.fetchall()
		return rows
