from read_data import read_data
from find_all_users_id import find_all_users_id

data = read_data("data/result.json")
users_id = find_all_users_id(data)

def find_user_message_count(data: dict, users_id: str)->dict:
    """
    This function will find the user's message count.
    
    Parameters:
        data (dict): Dictionary containing the data of the json file
        user_id (list): User id of the user
    Returns:
        dict: Number of messages of the users
    """
    return len(users_id)