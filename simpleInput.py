"""Library for simplified input handling"""
import builtins

def sinput(prompt_text, input_type, failure_text, range_low, range_high):
    """
    simpleInput input handler
    :param prompt_text: Text to show when prompting for input
    :param input_type: Type of desired input
    :param failure_text: Text to show if input is not accepted
    :param range_low: Low range-end for input
    :param range_high: High range-end
    :return: input
    """

    while True:
        given_input = input(prompt_text)
        if type(given_input) == input_type:
            if type(given_input) == builtins.int or type(given_input) == builtins.float:
                if range_low <= given_input and given_input <= range_high:
                    return given_input
            else:
                return given_input
        else:
            print(failure_text)
