import sqlite3
from uuid_extensions import uuid7
from db.connection import connect_db
from models.item import Item


class Transaction:
    '''Transaction class is a model class that we can use to create transaction
    adding item, delete item, update item and so on.
    '''

    def __init__(self, name=""):
        self.name = name
        self.uuid = str(uuid7())

    def create_transaction(self):
        '''create a new transaction into table transaction
        '''
        conn = connect_db()
        sql = '''INSERT INTO transactions(id, name)
              VALUES(?,?)'''

        cur = conn.cursor()

        try:
            cur.execute(sql, (self.uuid, self.name))
            conn.commit()
        except sqlite3.Error as err_msg:
            print(f'SQLite error: {err_msg}')

    def get_transaction(self, uuid):
        '''get existing transaction by uuid.

        Parameter:
        uuid(string): unique id as a string
        '''
        conn = connect_db()
        sql = '''SELECT * from transactions WHERE id = ?'''
        cur = conn.cursor()

        try:
            cur.execute(sql, (uuid,))
            result = cur.fetchone()
        except sqlite3.Error as err_msg:
            print(f'SQLite error: {err_msg}')

        if result is None:
            return None

        self.uuid = result[0]
        self.name = result[1]
        return result

    def delete_transaction(self):
        '''delete transaction from table transaction.
        '''
        conn = connect_db()
        sql = '''DELETE from transactions WHERE id = ?'''
        cur = conn.cursor()

        try:
            cur.execute(sql, (self.uuid,))
            conn.commit()
        except sqlite3.Error as err_msg:
            print(f'SQLite error: {err_msg}')

    def add_item(self, item: Item):
        '''add item into table item.

        Parameter:
        item(Item): item that contains id, name, qty, price.
        '''
        conn = connect_db()
        sql = '''INSERT INTO item(id, name, qty, price, transaction_id)
              VALUES(?,?,?,?,?)'''

        data = (item.id, item.name, item.qty, item.price, self.uuid)

        cur = conn.cursor()
        try:
            cur.execute(sql, data)
            conn.commit()
        except sqlite3.Error as err_msg:
            print(f'SQLite error: {err_msg}')

    def get_item(self, name):
        '''get item where name = args AND transaction_id = x.

        Parameter:
        name(string): item name
        '''
        conn = connect_db()
        sql = '''SELECT * from item WHERE name = ? AND transaction_id = ?'''

        data = (name, self.uuid)

        cur = conn.cursor()
        try:
            cur.execute(sql, data)
            result = cur.fetchone()
        except sqlite3.Error as err_msg:
            print(f'SQLite error: {err_msg}')

        return result

    def update_item_price(self, name, price):
        '''update item price from db where name = args AND transaction_id = x.

        Parameter:
        name(string): item name
        price(float): item price
        '''
        conn = connect_db()
        sql = '''UPDATE item SET price = ? WHERE name = ? AND transaction_id = ?'''

        data = (price, name, self.uuid)

        cur = conn.cursor()
        try:
            cur.execute(sql, data)
            conn.commit()
        except sqlite3.Error as err_msg:
            print(f'SQLite error: {err_msg}')

    def update_item_name(self, name, new_name):
        '''update item name from db where name = args AND transaction_id = x.

        Parameter:
        name(string): item name
        new_name(string): item new name
        '''

        conn = connect_db()
        sql = '''UPDATE item SET name = ? WHERE name = ? AND transaction_id = ?'''

        data = (new_name, name, self.uuid)

        cur = conn.cursor()
        try:
            cur.execute(sql, data)
            conn.commit()
        except sqlite3.Error as err_msg:
            print(f'SQLite error: {err_msg}')

    def update_item_qty(self, name, qty):
        '''update item qty from db where name = args AND transaction_id = x.

        Parameter:
        name(string): item name
        qty(integer): item qty
        '''
        conn = connect_db()
        sql = '''UPDATE item SET qty = ? WHERE name = ? AND transaction_id = ?'''

        data = (qty, name, self.uuid)

        cur = conn.cursor()
        try:
            cur.execute(sql, data)
            conn.commit()
        except sqlite3.Error as err_msg:
            print(f'SQLite error: {err_msg}')

    def delete_item(self, name):
        '''deleting item from db where name = args AND transaction_id = x.

        Parameter:
        name(string): item name
        '''
        conn = connect_db()
        sql = '''DELETE FROM item WHERE name = ? AND transaction_id = ?'''

        data = (name, self.uuid)

        cur = conn.cursor()
        try:
            cur.execute(sql, data)
            conn.commit()
        except sqlite3.Error as err_msg:
            print(f'SQLite error: {err_msg}')

    def all_item(self):
        '''get all item from db where transaction_id = x.
        '''
        conn = connect_db()
        sql = '''SELECT name, qty, price, transaction_id from item WHERE transaction_id = ?'''

        data = (self.uuid,)

        cur = conn.cursor()
        try:
            cur.execute(sql, data)
            result = cur.fetchall()
        except sqlite3.Error as err_msg:
            print(f'SQLite error: {err_msg}')

        return result

    def delete_all_item(self):
        '''deleting all item from db where transaction_id = x.
        '''
        conn = connect_db()
        sql = '''DELETE FROM item WHERE transaction_id = ?'''

        data = (self.uuid,)

        cur = conn.cursor()
        try:
            cur.execute(sql, data)
            conn.commit()
        except sqlite3.Error as err_msg:
            print(f'SQLite error: {err_msg}')
