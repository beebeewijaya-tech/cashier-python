from models.transaction import Transaction


def create_transaction():
    trx_name = input("Enter transaction name: ")

    trx = Transaction(trx_name)
    trx.create_transaction()
    return trx


def get_transaction():
    trx_id = input("Enter transaction id: ")

    trx = Transaction()
    rows = trx.get_transaction(trx_id)
    if rows is None:
        return None
    return trx


def delete_transaction(trx: Transaction):
    rows = trx.delete_transaction()
    if rows is None:
        return None
    return trx
