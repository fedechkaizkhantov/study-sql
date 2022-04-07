import sqlite3
import csv
import datetime


connect = sqlite3.connect('db')
cursor = connect.cursor()
# create table
cursor.execute("CREATE TABLE if not exists tab1 (col1 varchar(128));") # columns
file = open('111.csv','r') #file csv 
contents = csv.reader(file)
insert_records = "INSERT INTO tab1 (col1) VALUES (?)" # what to ins
cursor.executemany(insert_records, contents)
connect.commit()



#need to transform in def
cursor.execute("CREATE TABLE if not exists tab2 (col1 varchar(128));") 
file2 = open('222.csv','r') 
contents = csv.reader(file2) 
insert_records = "INSERT INTO allactiv2 (col1) VALUES (?)"
cursor.executemany(insert_records, contents)
connect.commit()

cursor.execute("CREATE TABLE if not exists tab3 (col1 varchar(128));")


# to show table
def showTable(tableName):
	print('_-'*20)
	print(tableName)

	print('_-'*20)
	cursor.execute(f'SELECT * FROM {tableName}')
	for row in cursor.fetchall():
		print(row)

	print('_-'*20+'\n')



def find (connect):
	cursor = connect.cursor()
	i = 0
	cursor.execute('''
			SELECT 
			tab1.col1 
			FROM tab1
			INNER JOIN tab2
			ON tab1.col1 = tab2.col1''')
	result = cursor.fetchall()
	if len(result) == 0:
		print(f'записей нет')
		return
	else:
		for row in result:
			email = result[i][0]
			i+=1
			cursor.execute('''INSERT INTO tab3 (col1) values (?)''',[email])
	connect.commit()

def toCsv(connect):
	cursor = connect.cursor()
	csvWriter = csv.writer(open("output.csv", "w"))
	cursor.execute('''
			SELECT DISTINCT
			tab3.col1 
			FROM tab3 ''')
	result = cursor.fetchall()
	for row in result:
		csvWriter.writerows(row)


