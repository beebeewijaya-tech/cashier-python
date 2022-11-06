import sqlite3


def connect_db() -> sqlite3.Connection:
    '''connecting to sqlite3, to be able doing db transaction, query
    '''
    conn = sqlite3.connect("project.db")
    return conn
