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


def get_ratios_tendency(ratio_1: tuple[int],
                        ratio_2: tuple[int]
                        ) -> bool | None:
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


def fit_num_pairs(outer_num_pair: tuple[int],
                  inner_num_pair: tuple[int]
                  ) -> tuple[int]:
    '''
    Considers outer_num_pair as a "parent" number pair
    which should fit inside a "child" inner_num_pair 
    number pair.

    For example:                                    \\
    outer_num_pair = (1920, 1080) # AKA screen      \\
    inner_num_pair = (1000, 600)  # AKA image       \\
    returns (1920, 1152), which is inner_num_pair
    optimised to fit to the outer_num_pair.
    '''

    ratio_tendecy = get_ratios_tendency(
        outer_num_pair, inner_num_pair
    )

    # --> What's going on below: 
    #   the bool values "True" and "False" are equivalent
    #   to 1 and 0, which can be used to assign indexes
    #   of two-option data sets. Thus they can be used
    #   to call a state-depending values, for example,
    #   in a tuple ("start", "abort") by their index, which
    #   is a bool value or a dictionary {0: "start"; 1: "abort"}
    #   simply calling by the bool value.

    outer = dict(enumerate(outer_num_pair))
    inner = dict(enumerate(inner_num_pair))

    outer_orient = (
        outer[0] <= outer[1]
        if ratio_tendecy else # in case of different orientation
        not outer[0] <= outer[1]
        )
    # If False (0), first integer is bigger
    inner_orient = (
        inner[0] <= inner[1])
    
    bigger_side = outer[outer_orient]
    # A simple proportion (A * B) = (C * ?)
    smaller_side = int(outer[outer_orient] * inner[not(inner_orient)]
                   / inner[inner_orient])
    
    fitted_pair = ((bigger_side, smaller_side)
                   if not(inner_orient) else # Just applying an orientation
                   (smaller_side, bigger_side))

    return fitted_pair


def add_columns_to_table(
        init_table: list[list],
        new_columns_head: list,
        default_value: str | int = ''
    ) -> list[list]:
    
    init_table[0] = init_table[0] + new_columns_head
    new_head = init_table[0]

    for id in range(len(init_table)):
        while len(init_table[id]) != len(new_head):
            init_table[id].append(default_value)
    
    return init_table