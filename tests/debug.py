users_dict = {
    'user_1': {
        'user_1_1': {
            'user_1_2': {
                'user_1_3': 'Maryna Viazovska'
            }
        }
    },
    'user_2': 'Lina Kostenko',
    'user_3': {
        'user_3_1': 'Kateryna Bilokur'
    }
}


my_list = []

def rec(value: dict):
    for v in value.values():
        if isinstance(v, str):
            my_list.append(v)
        else:
            rec(v)
    return my_list


rec(users_dict)

print(my_list)