import requests


def get_item_json(item_id, realm_index) -> dict:
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
        realm_index + "&item=" + item_id

    r = requests.get(url_string)  # get the json from underminejournal

    item_dict = r.json()  # construct dictionary

    return item_dict
