def ft_filter(function, params) -> list:
    """filter(function or None, iterable) --> filter object

Return an iterator yielding those items of iterable for which function(item)
is true. If function is None, return the items that are true."""
    new_list = [x for x in params if function(x) == True]
    return new_list
