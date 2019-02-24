# def is_valid_email(email):
#     """
#
#     >>> is_valid_email('student@localhost.ru')
#     True
#
#     >>> is_valid_email('vasya')
#     False
#     """
#     return '@' in email

def user_letters(name):

    """
    >>> user_letters('Василий Иванович')
    'ВИ'
    >>> user_letters('Иван')
    'И'
    >>> user_letters('Василий Алибабаевич Петров')
    'ВА'
    """


    parts = name.split(' ', 1)
    result = ''
    for part in parts:
        result += part[0]
    return result.upper()


