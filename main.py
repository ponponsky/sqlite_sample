import sqlite3
from contextlib import closing

dbname = "sample.db"

with closing(sqlite3.connect(dbname)) as conn:
    c = conn.cursor()
    query = '''drop table if exists User'''
    c.execute(query)
    conn.commit()

with closing(sqlite3.connect(dbname)) as conn:
    c = conn.cursor()
    query = '''create table if not exists
                User(id integer primary key, name varchar(32))'''
    c.execute(query)
    conn.commit()

with closing(sqlite3.connect(dbname)) as conn:
    c = conn.cursor()
    query = ''' insert into User (id, name) values (?,?)'''
    user = (1, "Yamashita")
    c.execute(query, user)
    conn.commit()

with closing(sqlite3.connect(dbname)) as conn:
    c = conn.cursor()
    query = ''' insert into User (id, name) values (?,?)'''
    user = [
        (2, "Kinoshita")
        ,(3, "Hasegawa")
    ]
    c.executemany(query, user)
    conn.commit()

with closing(sqlite3.connect(dbname)) as conn:
    c = conn.cursor()
    query = "select * from User"
    for row in c.execute(query):
        print(row)