import sqlite3

conn = sqlite3.connect('mobile_store.db')
cursor = conn.cursor()


cursor.execute('''
    CREATE TABLE IF NOT EXISTS mobiles (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        brand TEXT,
        model TEXT,
        price REAL
    )
''')


def create_mobile(brand, model, price):
    cursor.execute('''
        INSERT INTO mobiles (brand, model, price)
        VALUES (?, ?, ?)
    ''', (brand, model, price))
    conn.commit()


def get_mobiles():
    cursor.execute('SELECT * FROM mobiles')
    return cursor.fetchall()



def update_mobile(id, brand, model, price):
    cursor.execute('''
        UPDATE mobiles
        SET brand = ?, model = ?, price = ?
        WHERE id = ?
    ''', (brand, model, price, id))
    conn.commit()


def delete_mobile(id):
    cursor.execute('DELETE FROM mobiles WHERE id = ?', (id,))
    conn.commit()


create_mobile('Samsung', 'Galaxy S23', 999.99)
create_mobile('Apple', 'iPhone 14', 1099.99)


mobiles = get_mobiles()
print("All mobiles:", mobiles)


update_mobile(1, 'Samsung', 'Galaxy S24', 1099.99)


delete_mobile(2)


mobiles = get_mobiles()
print("Updated mobiles:", mobiles)


conn.close()
