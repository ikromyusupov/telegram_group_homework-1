from read_data import read_data
from find_all_users_id import find_all_users_id

def find_user_message_count(data: dict, users_id: str)->dict:
    """
    This function will find the user's message count.
    
    Parameters:
        data (dict): Dictionary containing the data of the json file
        user_id (list): User id of the user
    Returns:
        dict: Number of messages of the users
    """
    message_count = dict(zip(users_id, [0]*len(users_id)))

    for message in data['messages']:
        if message['type'] == 'message':
            message_count[message['from_id']] += 1
        

    return message_count
