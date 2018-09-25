import requests


def __get_item_json__(item_id, realm_index) -> dict:
    """
    Returns auctionhouse information from 'https://theunderminejournal.com/'

    Args:
        item_id (int): Defines the item with an id. Id's can be found at: 'https://www.wowhead.com/items'
        realm_index (int): Defines the realm with an id. List of Id's couln't be found. Thrall-EU = 238 

    Returns:
        dict: Returns a dict if a item with a proper json was found
        None: Returns None if no items or data was found

    Raises:
        None
    """

    # construct the url string
    url_string = "https://theunderminejournal.com/api/item.php?house=" + \
        str(realm_index) + "&item=" + str(item_id)

    r = requests.get(url_string)  # get the json from underminejournal

    item_dict = r.json()  # construct dictionary

    return item_dict


def get_item_name(item_id, realm_index) -> str:
    """
    Returns name from underminejournal json

    Args:
        item_id (int): Defines the item with an id. Id's can be found at: 'https://www.wowhead.com/items'
        realm_index (int): Defines the realm with an id. List of Id's couln't be found. Thrall-EU = 238 

    Returns:
        str: Returns a string that defines the name of the item
        None: Returns None if no items or data was found

    Raises:
        None
    """

    #  get item json and direct to name
    item_name = __get_item_json__(item_id, realm_index)[
        "stats"][0]["name_enus"]

    return item_name


def get_item_current_price(item_id, realm_index) -> int:
    """
    Returns current price from underminejournal json

    Args:
        item_id (int): Defines the item with an id. Id's can be found at: 'https://www.wowhead.com/items'
        realm_index (int): Defines the realm with an id. List of Id's couln't be found. Thrall-EU = 238 

    Returns:
        int: Returns an integer in wow bronce currency of the current lowest price
        None: Returns None if no items or data was found

    Raises:
        None
    """

    #  get item json and direct to name
    item_price = __get_item_json__(item_id, realm_index)[
        "stats"][0]["price"]

    return item_price


def get_item_quantity(item_id, realm_index) -> int:
    """
    Returns current quantity from underminejournal json

    Args:
        item_id (int): Defines the item with an id. Id's can be found at: 'https://www.wowhead.com/items'
        realm_index (int): Defines the realm with an id. List of Id's couln't be found. Thrall-EU = 238 

    Returns:
        int: Returns an integer with the quantity avalable in the ah currently
        None: Returns None if no items or data was found

    Raises:
        None
    """

    #  get item json and direct to name
    item_quantity = __get_item_json__(item_id, realm_index)[
        "stats"][0]["quantity"]

    return item_quantity
