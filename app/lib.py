def is_valid_email(email):
    """

    >>> is_valid_email('student@localhost.ru')
    True

    >>> is_valid_email('vasya')
    False
    """
    return '@' in email