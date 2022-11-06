def check_order_utils(data):
    '''This utilities function is to check the data is invalid or not. 
    If it's empty data, or non-numeric for the price and quantity, then it's invalid

    Parameters:
    data (item): an item record coming from database
    '''
    is_invalid = True
    if data[0] == "":
        is_invalid = False

    if data[1] is None or str(data[1]).isnumeric():
        is_invalid = False

    if data[2] is None or str(data[2]).isnumeric():
        is_invalid = False

    return is_invalid
