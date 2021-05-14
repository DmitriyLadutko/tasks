import sqlite3

CREATE_TABLE = """CREATE TABLE User (
    ID_user integer primary key autoincrement,
    first_name varchar(50),
    last_name varchar (50),
    age integer
);"""
INSERT_INTO_USER = """INSERT INTO USer (first_name, last_name, age) VALUES (?, ?, ?);"""

if __name__ == '__main__':
    connection = sqlite3.connect('test.db')
    cursor = connection.cursor()
    '''Запрос в БД'''
    cursor.execute(INSERT_INTO_USER, [('Dima', 'Ladutko', 29),
                                          ('Nastia', 'Ladutko', 27),
                                          ('Dasha', 'Ladutko', 26),
                                          ])
    cursor.close()
    '''Запись в БД'''
    connection.commit()
    connection.close()
