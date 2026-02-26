import textwrap

from PIL import Image, ImageDraw

from modules.program import get_path, load_font


def text_to_field(
        text: str,
        fields_size: tuple[int],
        font_size,
        color: tuple[int] = (220, 220, 220),
        font_path: str = 'font_default'
) -> Image:
    '''
    Place a given text on an alpha layer
    of a PIL.Image module object.

    **Text wrapping is not considered**.
    '''
    scene = Image.new('RGBA', fields_size, (0, 0, 0, 0))
    draw = ImageDraw.Draw(scene)

    font_path = get_path(font_path)
    font = load_font(font_size=font_size)
    position = (0, 0)

    draw.text(position, text, fill=color, font=font)

    return scene


def know_text_size(
        text_string: str,
        font_path: str = 'font_default',
        font_size: int = 20
    ) -> tuple[int]:
    '''
    Calculate text size in pixels based on
    '''

    image = Image.new("RGB", (100, 100), color="white")
    draw = ImageDraw.Draw(image)
    
    font = load_font(
        font_path=font_path,
        font_size=font_size)

    bbox = draw.textbbox((0, 0), text_string, font=font, anchor='la')

    width = bbox[2] - bbox[0]
    height = bbox[3] - bbox[1]

    return (width, height)


def text_field_and_wrap(
        scene_width: int,
        text: str,
        font_size: int,
        font_path: str = 'font_default',
) -> tuple[tuple, str]:
    '''
    Fit the text within needed width in pixels
    and wrap it.

    Return text field (box) size in pixels and wrapped text.
    '''
    text_single_line = know_text_size(
        text,
        font_path=font_path,
        font_size=font_size)
    font_line_height = text_single_line[1]

    for lengh in range(1, len(text)+1):
        try_wrapped_text = textwrap.fill(
            text, width=lengh)
        
        try_text_box_size = know_text_size(
            try_wrapped_text,
            font_path=font_path,
            font_size=font_size)
        
        try_text_width = try_text_box_size[0]

        if try_text_width <= scene_width:
            text_box_size = try_text_box_size
            wrapped_text = try_wrapped_text
        else:
            break
    
    # correcting missing half of a last text
    # line by adding the half (to the height)
    text_box_size = (text_box_size[0], 
                    text_box_size[1] + round(font_line_height / 2))
    
    return text_box_size, wrapped_text