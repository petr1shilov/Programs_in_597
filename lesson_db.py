import sqlite3

# Подключение к БД
con = sqlite3.connect('school.db')

# совершение действий с БД
curcor = con.cursor()
# Добавление в таблицы БД
# curcor.execute('CREATE TABLE pupils(fname TEXT, lname TEXT, mark INT)')
# Добавление строк в БД
# curcor.execute('''INSERT INTO pupils VALUES(
#                                     'DIMA',
#                                     'EVSEEV',
#                                         5)''')
# curcor.execute('''INSERT INTO pupils VALUES(
#                                     'ROMA',
#                                     'ROMANOV',
#                                         3)''')
# curcor.execute('''INSERT INTO pupils VALUES(
#                                     'ANDREI',
#                                     'KUNDA',
#                                         4)''')
# Изменение значаний строк в БД
# curcor.execute('''UPDATE pupils SET fname='Anton' WHERE lname='EVSEEV' ''')
# уданение из БД
# curcor.execute('''DELETE FROM pupils WHERE fname='ANDREI' ''')
curcor.execute('''SELECT * FROM pupils''')
# fecth - get - взять что-либо
list_of_puils = curcor.fetchall()

for i in list_of_puils:
    print(i)

print('************************')

print(*list_of_puils, sep='\n')

name = list_of_puils[0][0], list_of_puils[0][1], list_of_puils[0][2]
print(name)

con.commit()