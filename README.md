# Introduction

This is a cashier simulation apps that can create a transaction, adding an item into transaction, updating an item, delete items, calculcate total prices.

# How to run the project

```
    pip3 install requirements.txt
    python3 main.py
```

# Menu

1. Add New Transaction
2. Use existing transaction
3. Add New Item Into Transaction
4. Update Item Price
5. Update Item Name
6. Update Item Qty
7. Delete Item
8. Reset Transaction
9. Delete Transaction
10. Check Order
11. Total Price
12. Exit

# Tools

1. Python3
2. SQLite3

# Folder Structure

├───.vscode
├───controllers
├───db
├───helpers
└───models

vscode: vscode setup for python project
controllers: controlling the flow of the code, calls in `main.py` and consuming the `models` and `helpers`
models: communicating with database, query db or transact
helpers: utils function
