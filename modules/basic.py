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