import math

from debug import DebugPrint


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



def compare_ratios(ratio_1: tuple[int],
                   ratio_2: tuple[int]
                   ) -> bool:
    '''
    Compare two ratios by equaling 2nd ratio
    to 1st by the first ratios number and put
    second ratios numbers under compare.\n
    Return True if first ratio's 2nd number
    is bigger or equal than second ratio's 
    2nd number, else return False.
    \n\n
    Example:\\
    ratio_1 = (16,9)\\
    ratio_2 = (4,3)\\
    Adjusting ratio_2 to ratio_1 by equaling
    ratio_2's 1st number to ratio_1's 1st number:\\
    (4,3) -> (16,**12**)\\
    since “12” in 16:12 bigger than “9” in 16:9,
    False is returned.
    '''

    ratio_compared = round(
        ratio_1[0] * ratio_2[1]
            / ratio_2[0]
    )

    compare = ratio_1[1] >= ratio_compared

    if compare:
        return True
    else:
        return False



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

    ratio_tendency = compare_ratios(
        outer_num_pair, inner_num_pair
    )

    DebugPrint("ratio tendency: ", ratio_tendency)

    # --> What's going on below: 
    #   the bool values "True" and "False" are equivalent
    #   to 1 and 0, which can be used to assign indexes
    #   of two-option data sets. Thus they can be used
    #   to call a state-depending values, for example,
    #   in a tuple ("start", "abort") by their index, which
    #   is a bool value or a dictionary {0: "start"; 1: "abort"}
    #   simply calling by the bool value.

    outer = dict(enumerate(outer_num_pair))
    # By calling "outer[outer_orient]" the biggest
    # value of outer is returned.
    outer_orient = (False if outer[0] > outer[1]
                    else True)

    inner = dict(enumerate(inner_num_pair))
    # By calling "inner[inner_orient]" the biggest
    # value of inner is returned.
    inner_orient = (False if inner[0] > inner[1]
                    else True)
    
    DebugPrint(inner, inner_orient, inner[inner_orient])
    
    if not ratio_tendency:
        bigger_side = outer[not(outer_orient)]
    else:
        bigger_side = outer[outer_orient]
    
    # A simple proportion (A / B) = (C / ?)
    smaller_side = int((bigger_side * inner[not(inner_orient)])
                                / inner[inner_orient])
        
    fitted_pair = ((smaller_side, bigger_side) if not ratio_tendency
                   else (bigger_side, smaller_side))

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