# Replace the "ANSWER HERE" with your answer

def remove_elements(list_to_remove_elements):
    
    if len(list_to_remove_elements) > 5: del list_to_remove_elements[5]
    if len(list_to_remove_elements) > 4: del list_to_remove_elements[4]
    if len(list_to_remove_elements) > 0: del list_to_remove_elements[0]
    
    return list_to_remove_elements


def add_elements(list_to_add_elements):
    
    list_to_add_elements.insert(0, 'Pink')
    list_to_add_elements.insert(len(list_to_add_elements), 'Yellow')

    return list_to_add_elements


def is_empty(list_to_check):
    return len(list_to_check) == 0  # Remove this line and implement


def check_lists(list_to_compare1, list_to_compare2):
    
    try:
        list_to_compare1[2]
        list_to_compare2[2]
    except:
        return False
    
    return (list_to_compare1[2] == list_to_compare2[2])


def list_of_lists(list_of_lists_to_modify):
    return [list_of_lists_to_modify[0][:2],list_of_lists_to_modify[1][1:4],list_of_lists_to_modify[2][-2:]]
