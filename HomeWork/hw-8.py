import sqlite3


def create_database():
    conn = sqlite3.connect('students.db')
    c = conn.cursor()

    # Создаем таблицу студентов
    c.execute('''
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            hobby TEXT,
            name TEXT,
            surname TEXT,
            birth_year INTEGER,
            homework_score INTEGER
        )
    ''')

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
    c.executemany('''
        INSERT INTO students (hobby, name, surname, birth_year, homework_score)
        VALUES (?, ?, ?, ?, ?)
    ''', students)

    conn.commit()

    conn.close()

def get_students_with_long_surname():
    conn = sqlite3.connect('students.db')
    c = conn.cursor()

    c.execute('''SELECT * FROM students WHERE length(surname) > 10''')
    students = c.fetchall()

    conn.close()

    return students


def update_genius_students():
    conn = sqlite3.connect('students.db')
    c = conn.cursor()

    c.execute('''UPDATE students SET name="genius" WHERE homework_score > 10''')

    conn.commit()

    conn.close()


def get_genius_students():
    conn = sqlite3.connect('students.db')
    c = conn.cursor()

    c.execute('''SELECT * FROM students WHERE name="genius"''')
    students = c.fetchall()

    conn.close()

    return students


def delete_even_id_students():
    conn = sqlite3.connect('students.db')
    c = conn.cursor()

    c.execute('''DELETE FROM students WHERE id % 2 = 0''')

    conn.commit()

    conn.close()


create_database()


students_with_long_surname = get_students_with_long_surname()
print('Students with long surname:')
for student in students_with_long_surname:
    print(student)

update_genius_students()

genius_students = get_genius_students()
print('Genius students:')
for student in genius_students:
    print(student)

delete_even_id_students()
