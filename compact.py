def compact(lst):
    """Return a copy of lst with non-true elements removed.

        >>> compact([0, 1, 2, '', [], False, (), None, 'All done'])
        [1, 2, 'All done']
    """
    new_lst = []
    for idx in lst:
        if idx:
            new_lst.append(idx)
    return new_lst