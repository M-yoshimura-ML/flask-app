import sqlite3

try:
    conn = sqlite3.connect('database.db')
    print('Connected database successfully')
    conn.execute('CREATE TABLE students (name TEXT, address TEXT, city TEXT, pin TEXT)')
    print('TABLE created successfully')
    conn.commit()
except sqlite3.Error as e:
    print('SQLite error occurred:', e)
    if conn:
        conn.rollback()
        print('Transaction rolled back')
finally:
    conn.close()
