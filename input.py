"""Helper methods for getting user input"""


def get_bool_input(message):
    """Gets boolean input from the terminal"""
    values = {'y': True, 'yes': True, 'n': False, 'no': False, '': False}
    return values[validate_input_of_values(
        message=message,
        valid_values=set(values.keys())
    )]


def get_int_input(message):
    """Gets an integer input from the terminal"""

    def converts_to_int(check_string):
        try:
            int(check_string)
        except ValueError:
            return False
        else:
            return True

    return int(validate_input_of_predicate(
        message=message,
        condition=lambda x: converts_to_int(x) and int(x) > 0,
        failure_message='Please enter a positive integer.'
    ))


def validate_input_of_predicate(message, condition, failure_message):
    """Applies a condition to input to check it"""
    text = input(message)
    while not condition(text):
        text = input(failure_message)
    return text


def validate_input_of_values(message, valid_values):
    """Checks whether an input is in a set of valid inputs"""
    text = input(message).lower()
    while text not in valid_values:
        text = input(f'Valid inputs: {valid_values}')
    return text
