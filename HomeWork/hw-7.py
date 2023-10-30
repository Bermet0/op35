import sqlite3
with sqlite3.connect('student.db') as conn:

    conn.execute('''CREATE TABLE IF NOT EXISTS student (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    hobby TEXT,
                    first_name TEXT,
                    last_name TEXT,
                    birth_year INTEGER,
                    score INTEGER);''')


    students = [
        ('hobby1', 'John', 'Doe', 1990, 5),
        ('hobby2', 'Jane', 'Smith', 1991, 15),
        ('hobby3', 'Alex', 'Johnson', 1992, 8),
        ('hobby4', 'Emily', 'Brown', 1993, 9),
        ('hobby1', 'John', 'Duhabushen123', 1990, 5),
        ('hobby2', 'Jane', 'Smithelena123', 1991, 15),
        ('hobby3', 'Alex', 'Johnsonmach123', 1992, 8),
        ('hobby4', 'Emily', 'Brownessa123', 1993, 9),
        ('hobby1', 'John', 'Doe', 1990, 5),
        ('hobby2', 'Jane', 'Smith', 1991, 15),

    ]
    conn.executemany('INSERT INTO student (hobby, first_name, last_name, birth_year, score) VALUES (?, ?, ?, ?, ?)',
                     students)


    long_last_name_students = conn.execute('SELECT * FROM student WHERE LENGTH(last_name) > 10').fetchall()
    print("Студенты с фамилией длиннее 10 символов:")
    for student in long_last_name_students:
        print(student)


    conn.execute('UPDATE student SET first_name = "genius" WHERE score > 10')


    genius_students = conn.execute('SELECT * FROM student WHERE first_name = "genius"').fetchall()
    print("Студенты-гении:")
    for student in genius_students:
        print(student)


    conn.execute('DELETE FROM student WHERE id % 2 = 0')

    conn.commit()

