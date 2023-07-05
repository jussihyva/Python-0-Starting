def NULL_not_found(object: any) -> int:
    # your code here
    result = 0
    object_type = type(object)
    if object is None:
        print('{}: {} {}'.format('Nothing', 'None', str(object_type)))
    elif object_type == float and object != object:
        print('{}: {} {}'.format('Cheese', 'nan', str(object_type)))
    elif object_type == int and object == 0:
        print('{}: {} {}'.format('Zero', '0', str(object_type)))
    elif object_type == str and object == '':
        print('{}: {}'.format('Empty', str(object_type)))
    elif (object_type == bool) and (object is False):
        print('{}: {} {}'.format('Fake', 'False', str(object_type)))
    else:
        print('Type not Found')
        result = 1
    return result
