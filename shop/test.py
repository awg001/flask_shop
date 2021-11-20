import sqlite3 


db = sqlite3.connect('shop.db')
cur = db.cursor()

db.execute('DROP TABLE IF EXISTS users')
db.commit()