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
    >>> user_letters('Vasilii Ivanovich')
    VI
    >>>user_letters(Ivan)
    V

    """


    parts = name.split
    return parts[0][0] + parts [1][0]
