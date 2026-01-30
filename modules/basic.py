import math


def define_id(number: str | int,
              prefix: str = "id_",
              max_id_lenth: int = 13,
              padding_char: str = '0',
              suffix: str = ''
    ) -> str:

    number = str(number)
    
    if len(number) > max_id_lenth:
        max_id_lenth = len(number)
        
    lenth = (max_id_lenth - len(number))
    num = padding_char * lenth + number

    return f'{prefix}{num}{suffix}'


def two_number_ratio(num1: int, num2: int) -> tuple:
    '''returns the simplest ratio of two numbers as a tuple'''

    gcd = math.gcd(num1, num2)
    return (num1//gcd, num2//gcd)


def get_ratios_tendency(ratio_1: tuple, ratio_2: tuple) -> bool | None:
    '''Checks if two ratios have the same tendency. Applying to an image
    logic it means if both ratios are landscape or portrait or square.\\
    True for horizontal and vertical, False if they differ
    and None if square'''

    if ratio_1[0] == ratio_1[1] or ratio_2[0] == ratio_2[1]:
        return None
    elif (ratio_1[0] > ratio_1[1] and ratio_2[0] > ratio_2[1]) or \
         (ratio_1[0] < ratio_1[1] and ratio_2[0] < ratio_2[1]):
        return True
    else:
        return False