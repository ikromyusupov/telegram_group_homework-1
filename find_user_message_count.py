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
    return 0
#     lst = []
#     for i in data["messages"]:
#         lst.append(i["id"])
#     return lst
# data = read_data("data/result.json")
# users_id = find_all_users_id(data)
# print(find_user_message_count(data))