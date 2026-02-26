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