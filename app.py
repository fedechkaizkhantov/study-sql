import sqlite3
import json

from database import *
connect = sqlite3.connect('sber.db')
cursor = connect.cursor()
initTables(connect)
addClient (connect,'Сергей','Иванов', 27)
addClient (connect,'Сергей','Иванов', 30)
addClientfromJSON(connect,'client.json')
midAge(connect)


cursor.execute('SELECT * FROM client')
for row in cursor.fetchall():
	print(row)
