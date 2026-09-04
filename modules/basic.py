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
    
    ratio_1_eq = ratio_1[0] > ratio_1[1]
    ratio_2_eq = ratio_2[0] > ratio_2[1]

    if ratio_1_eq == ratio_2_eq:
        return True
    else:
        return 



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


def aspect_fit(container_num_pair: tuple[int],
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

    k = min(container_num_pair[0]/inner_num_pair[0],
        container_num_pair[1]/inner_num_pair[1])

    img_width = round(inner_num_pair[0] * k)
    img_height = round(inner_num_pair[1] * k)

    return (img_width, img_height)


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