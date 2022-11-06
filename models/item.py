class Item:
    '''Item class is a model class that we can use to initialize item
    we use this as a model to save item into database
    '''

    def __init__(self, id, name, qty, price):
        self.id = id
        self.name = name
        self.qty = qty
        self.price = price

    def __str__(self):
        return f"{self.name} - {self.qty} - {self.price}"
