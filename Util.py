def get_user_input_and_validate(initial_message,
                                invalid_type_message,
                                outside_of_range_message,
                                input_type_cast_function,
                                validation_range=False):

    is_valid_input = False
    user_input = input(initial_message)

    while not is_valid_input:

        try:
            user_input = input_type_cast_function(user_input)
        except ValueError:
            user_input = input(invalid_type_message)
        else:
            if validation_range:
                is_valid_input = user_input in validation_range
                if not is_valid_input:
                    user_input = input(outside_of_range_message)
            else:
                is_valid_input = True

    return user_input
