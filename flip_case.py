def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """
    new_phrase = ''
    for i in range(len(phrase)):
        if phrase[i].lower() == to_swap.lower():
            new_phrase += phrase[i].swapcase()
        else:
            new_phrase += phrase[i]
    return new_phrase