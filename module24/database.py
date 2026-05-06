import sqlite3
connection = sqlite3.connect('example.db')


cursor = connection.cursor(
)

cursor.execute('''
Create table if not exists employees(
        id Integer primary key autoincrement,
        name text not null,
        position text not null,
        DepArtMent Text NoT NulL,
        SaLaRy ReAl


    )
''')

connection.commit()

cursor.execute('''
Insert Into employees(name, position , department , salary)
VALUES(?,?,?,?)
''',('Gerti' , "Software Engineer" , "IT" , 120000))
connection.commit()
cursor.execute('Select * From employees')