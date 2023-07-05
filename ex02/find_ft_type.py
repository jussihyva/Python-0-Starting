def all_thing_is_obj(object: any) -> int:
    # your code here
    param_type = type(object)
    if param_type == list:
        print('{} : {}'.format('List', str(param_type)))
    elif param_type == tuple:
        print('{} : {}'.format('Tuple', str(param_type)))
    elif param_type == set:
        print('{} : {}'.format('Set', str(param_type)))
    elif param_type == dict:
        print('{} : {}'.format('Dict', str(param_type)))
    elif param_type == str:
        print('{} {} : {}'.format(object, 'is in the kitchen', str(param_type)))
    else:
        print('{}'.format('Type not found'))
    return 42
