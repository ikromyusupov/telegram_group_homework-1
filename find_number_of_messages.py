from read_data import read_data

def find_number_of_messages(data: dict)->int:
    """
    Get the total number of messages.

    Parameters:
        data (dict): Dictionary containing the data of the json file.
    Returns:
        int: Total number of messages.
    
    """
    lst = []
    for i in data["messages"]:
        lst.append(i["id"])
    return lst
data = read_data("data/result.json")
print(find_number_of_messages(data))