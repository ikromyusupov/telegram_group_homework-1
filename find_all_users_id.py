from read_data import read_data

def find_all_users_id(data: dict)->list:
    """ 
    This function will find all the users in the json file and return the list of users id
    
    Parameters:
        data (dict): Dictionary containing the data of the json file
    Returns:
        list: List containing all the users id
    """
    lst = []
    for i in data["messages"]:
        if i.get('from_id') and i.get('from_id') not in lst:
            lst.append(i['from_id'])
    return lst
data = read_data("data/result.json")
