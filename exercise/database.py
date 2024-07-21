#1) Функция, которая создает таблицу client если она уже есть, необходимо
#вывести об этом сообщение в консоль
def initTables(connect):
	cursor = connect.cursor()
	try:
		cursor.execute('select * from client')
	except:
		cursor.execute("""
			CREATE TABLE if not exists client (
				id integer primary key autoincrement,
				name varchar(128),
				lastname varchar(128),
				age integer
				)""")

# 2)Функция, которая добавляет клиентов в таблицу (если клиента с такими
# фамилией и именем нет в таблице)
def addClient (connect, name, lastname, age):
	cursor = connect.cursor()
	cursor.execute('select name, lastname from client where (name = ? and lastname = ?)', [name, lastname])
	result = cursor.fetchall()
	if len(result) != 0:
		print(f'клиент с именем {name} {lastname} уже есть')
		return
	else:
		cursor.execute('''INSERT INTO client(name, lastname, age) 
						values (?, ?, ?)''',[name, lastname, age])
	connect.commit()

# 3)Функция, которая получив путь до JSON файла и добавляет клиентов в таблицу
#(только тех, которые по фамилии и имени отсутствуют в таблице)
# читать строку, проверить наличие клиента, добавить строку
def addClientfromJSON(connect, path):
	import json
	with open(path, 'r', encoding='utf-8') as f: 
		text = json.load(f) 
	i = 0	
	for txt in text:
		cursor = connect.cursor()
		
		print(text[i])	
		strName = text[i]['name']
		strLastname = text[i]['lastname']
		strAge = text[i]['age']
		i+=1
		cursor.execute('select name, lastname from client where (name = ? and lastname = ?)', [strName, strLastname])

		result = cursor.fetchall()
		if len(result) != 0:
			print(f'клиент с именем {strName} {strLastname} уже есть')
		else:
			cursor.execute('''INSERT INTO client(name, lastname, age) 
						values (?, ?, ?)''',[strName, strLastname, strAge])

		connect.commit()
#4)Функция, которая возвращает средний возраст клиентов.

def midAge(connect):
	cursor = connect.cursor()
	cursor.execute('''SELECT avg(age) as mid FROM client 
		''')
	result = cursor.fetchall()
	mid = result[0][0]
	print(f'Средний возраст клиентов {mid} лет')
	return


