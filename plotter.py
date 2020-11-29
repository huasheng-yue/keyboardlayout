import typing
from types import ModuleType
from enum import Enum

import pygame

def init_pygame_and_draw_keyboard(keyboard_layout: str):
    pygame.init()
    pygame.display.set_caption("{} keyboard layout".format(keyboard_layout))

    keyboard = get_keyboard(keyboard_layout, (0, 0))

    screen = pygame.display.set_mode(
        (keyboard.rect.width, keyboard.rect.height))
    screen.fill(pygame.Color('black'))

    keyboard.draw(screen)
    pygame.display.update()

def run_until_window_closed():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False


class TxtAnchor(Enum):
    TOP_LEFT = 'tl'
    TOP_CENTER = 'tc'
    TOP_RIGHT = 'tr'
    MIDDLE_LEFT = 'ml'
    MIDDLE_CENTER = 'mc'
    MIDDLE_RIGHT = 'mr'
    BOTTOM_LEFT = 'bl'
    BOTTOM_CENTER = 'bc'
    BOTTOM_RIGHT = 'br'

class TxtSprite(pygame.sprite.Sprite):
    def __init__(
        self,
        x: int,
        y: int,
        txt_anchor: TxtAnchor,
        txt: str,
        font: pygame.font.SysFont,
        font_color: pygame.Color,
    ):
        super().__init__()
        self.font_color = font_color
        self.txt = txt
        self.font = font
        self.render_text()

        txt_width = self.image.get_width()
        txt_height = self.image.get_height()

        if txt_anchor is TxtAnchor.TOP_LEFT:
            xloc = x
            yloc = y
        elif txt_anchor is TxtAnchor.BOTTOM_LEFT:
            xloc = x
            yloc = y - txt_height
        elif txt_anchor is TxtAnchor.BOTTOM_RIGHT:
            xloc = x - txt_width
            yloc = y - txt_height
        elif txt_anchor is TxtAnchor.TOP_CENTER:
            xloc = x - txt_width//2
            yloc = y
        elif txt_anchor is TxtAnchor.BOTTOM_CENTER:
            xloc = x - txt_width//2
            yloc = y - txt_height
        elif txt_anchor is TxtAnchor.MIDDLE_CENTER:
            xloc = x - txt_width//2
            yloc = y - txt_height//2
        self.rect = pygame.Rect(xloc, yloc, txt_width, txt_height)

    def render_text(self):
        self.image = self.font.render(self.txt, 1, self.font_color)


class RectSprite(pygame.sprite.Sprite):
    def __init__(
        self,
        r: pygame.Rect,
        color: pygame.Color,
    ):
        super().__init__()
        self.image = pygame.Surface([r.width, r.height])
        self.image.fill(color)
        self.rect = pygame.Rect(r.x, r.y, r.width, r.height)


class Key:
    def __init__(
        self,
        bg_sprites: pygame.sprite.Group,
        txt_sprites: pygame.sprite.Group
    ):
        self.bg_sprites = bg_sprites
        self.txt_sprites = txt_sprites



class KeyGroup(pygame.sprite.Group):
    def __init__(
        self,
        r: pygame.Rect,
        key_margin: int,
        color: pygame.Color,
        txt_info: typing.Dict[str, str],
        font: pygame.font.SysFont,
        font_color: pygame.Color,
        txt_xpadding: int,
        txt_ypadding: int,
    ):
        super().__init__()
        x, y, width, height = r.x, r.y, r.width, r.height
        key_padding = key_margin//2
        r = pygame.Rect(
            x+key_padding,
            y+key_padding,
            width-2*key_padding,
            height-2*key_padding,
        )
        bg_sprite = RectSprite(r, color)
        self.add(bg_sprite)

        for txt_anchor, label_txt in txt_info.items():
            txt_anchor = TxtAnchor(txt_anchor)
            if txt_anchor is TxtAnchor.TOP_LEFT:
                xloc = x + key_padding + txt_xpadding
                yloc = y + key_padding + txt_ypadding
            elif txt_anchor is TxtAnchor.BOTTOM_LEFT:
                xloc = x + key_padding + txt_xpadding
                yloc = y + height - key_padding - txt_ypadding
            elif txt_anchor is TxtAnchor.BOTTOM_RIGHT:
                xloc = x + width - key_padding - txt_xpadding
                yloc = y + height - key_padding - txt_ypadding
            elif txt_anchor is TxtAnchor.TOP_CENTER:
                xloc = x + width//2
                yloc = y + key_padding + txt_ypadding
            elif txt_anchor is TxtAnchor.BOTTOM_CENTER:
                xloc = x + width//2
                yloc = y + height - key_padding - txt_ypadding
            elif txt_anchor is TxtAnchor.MIDDLE_CENTER:
                xloc = x + width//2
                yloc = y + height//2
            txt_sprite = TxtSprite(
                xloc,
                yloc,
                txt_anchor,
                label_txt,
                font,
                font_color
            )
            self.add(txt_sprite)


class KeyboardLayout(pygame.sprite.Group):
    __letter_key_size_keycoords = (1, 1)

    @classmethod
    def __get_remainder_x(
        cls,
        xmax: int,
        letter_key_width: int,
        key_names: typing.List[str],
        layout: ModuleType
    ):
        if (
            any(key_name in layout.key_width_percent_remainder_sizes
                for key_name in key_names
            )
        ):
            used_width = 0
            for key_name in key_names:
                if key_name in layout.key_width_percent_remainder_sizes:
                    continue
                keysize_name = layout.key_to_key_size.get(key_name, None)
                key_xsize_keycoords, _ = layout.key_sizes.get(
                    keysize_name, cls.__letter_key_size_keycoords)
                key_width = letter_key_width * key_xsize_keycoords
                used_width += key_width
            remainder_x = xmax - used_width
            return remainder_x
        return None

    @classmethod
    def __get_key_width_height(
        cls,
        key_name: str,
        remainder_x: typing.Optional[int],
        letter_key_width: int,
        letter_key_height: int,
        layout: ModuleType,
    ):
        keysize_name = layout.key_to_key_size.get(key_name, None)
        key_xsize_keycoords, key_ysize_keycoords = (
            layout.key_sizes.get(keysize_name, cls.__letter_key_size_keycoords)
        )
        key_width_percent_remainder = (
            layout.key_width_percent_remainder_sizes.get(key_name, None)
        )
        if key_width_percent_remainder is None:
            key_width = letter_key_width * key_xsize_keycoords
        else:
            key_width = remainder_x*(key_width_percent_remainder/100)
        key_height = letter_key_height * key_ysize_keycoords
        return key_width, key_height

    @classmethod
    def __max_width(
        cls,
        letter_key_width: int,
        layout: ModuleType,
    ):
        for row in layout.rows:
            key_names = set(key['name'] for key in row['keys'])
            if any(
                key_name in layout.key_width_percent_remainder_sizes for
                key_name in key_names
            ):
                continue
            used_width = 0
            for key_name in key_names:
                keysize_name = layout.key_to_key_size.get(key_name, None)
                key_xsize_keycoords, _ = (
                    layout.key_sizes.get(
                        keysize_name, cls.__letter_key_size_keycoords
                    )
                )
                key_width = letter_key_width * key_xsize_keycoords
                used_width += key_width
            break
        return used_width

    @classmethod
    def __max_height(
        cls,
        letter_key_height: int,
        layout: ModuleType,
    ):
        height_max = 0
        for row in layout.rows:
            for row_key in row['keys']:
                key_name = row_key['name']
                keysize_name = layout.key_to_key_size.get(key_name, None)
                _, key_ysize_keycoords = (
                    layout.key_sizes.get(
                        keysize_name, cls.__letter_key_size_keycoords
                    )
                )
                _, row_y_keycoords = row["location"]
                row_y = row_y_keycoords * letter_key_height
                key_height = letter_key_height * key_ysize_keycoords
                key_ymax = row_y + key_height
                if key_ymax > height_max:
                    height_max = key_ymax
        return height_max

    def __add_additional_sprites_to_key(
        self,
        key_name: str,
        key_group: KeyGroup,
        key_margin: int,
        key_color: pygame.Color,
    ):
        txt_sprites = key_group.sprites()[1:]
        key = self._key_name_to_key[key_name]
        key.txt_sprites.add(txt_sprites)

        new_bg_sprite = key_group.sprites()[0]
        existing_bg_sprite = key.bg_sprites.sprites()[0]
        if existing_bg_sprite.rect.width < new_bg_sprite.rect.width:
            used_rect = existing_bg_sprite.rect
            used_y = used_rect.bottom
        else:
            used_rect = new_bg_sprite.rect
            used_y = used_rect.top - key_margin
        r = pygame.Rect(
            used_rect.left,
            used_y,
            used_rect.width,
            key_margin,
        )
        sticher_sprite = RectSprite(r, key_color)
        self.add([sticher_sprite])
        key.bg_sprites.add([new_bg_sprite, sticher_sprite])

    def __init__(
        self,
        position: typing.Tuple[int],
        layout_name: str,
        keyboard_padding: int,
        letter_key_width: int,
        letter_key_height: int,
        key_margin: int,
        key_color: pygame.Color,
        font_color: pygame.Color,
        font: pygame.font.SysFont,
        txt_xpadding: int,
        txt_ypadding: int,
        keyboard_color: typing.Optional[pygame.Color]=None
    ):
        super().__init__()
        layout = __import__(
            'keyboard_layouts.{}'.format(layout_name),
            fromlist=['']
        )
        self._key_name_to_key = {}

        x, y = position
        xanchor = x + keyboard_padding
        yanchor = y + keyboard_padding
        if key_margin:
            xanchor += -key_margin//2
            yanchor += -key_margin//2
        xmax = 0
        ymax = 0
        max_width = self.__max_width(letter_key_width, layout)
        max_height = self.__max_height(letter_key_height, layout)
        self.rect = pygame.Rect(
            x,
            y,
            max_width - key_margin + 2*keyboard_padding,
            max_height - key_margin + 2*keyboard_padding,
        )
        if keyboard_color:
            bg_sprite = RectSprite(self.rect, keyboard_color)
            self.add(bg_sprite)
        for row in layout.rows:
            row_keys = row['keys']
            key_names = set(key['name'] for key in row_keys)
            remainder_x = self.__get_remainder_x(
                max_width, letter_key_width, key_names, layout)

            row_x_keycoords, row_y_keycoords = row['location']
            key_x = xanchor + row_x_keycoords * letter_key_width
            row_y = yanchor + row_y_keycoords * letter_key_height
            for row_key in row_keys:
                key_name = row_key['name']
                key_width, key_height = self.__get_key_width_height(
                    key_name,
                    remainder_x,
                    letter_key_width,
                    letter_key_height,
                    layout,
                )
                rect = pygame.Rect(key_x, row_y, key_width, key_height)
                key_group = KeyGroup(
                    rect,
                    key_margin,
                    key_color,
                    row_key['txt_info'],
                    font,
                    font_color,
                    txt_xpadding,
                    txt_ypadding
                )
                self.add(key_group.sprites())
                key_x += key_width
                if key_name not in self._key_name_to_key:
                    bg_sprites = pygame.sprite.Group(key_group.sprites()[:1])
                    txt_sprites = pygame.sprite.Group(key_group.sprites()[1:])
                    key = Key(bg_sprites, txt_sprites)
                    self._key_name_to_key[key_name] = key
                else:
                    self.__add_additional_sprites_to_key(
                        key_name, key_group, key_margin, key_color)

    def update_key(
        self,
        key_name: str,
        bg_color: typing.Optional[pygame.Color] = None,
        font_color: typing.Optional[pygame.Color] = None,
    ):
        key = self._key_name_to_key[key_name]
        if bg_color:
            for bg_sprite in key.bg_sprites.sprites():
                bg_sprite.image.fill(bg_color)
        if font_color:
            for txt_sprite in key.txt_sprites.sprites():
                txt_sprite.font_color = font_color
                txt_sprite.render_text()


def get_keyboard(keyboard_layout: str, position: typing.List[int]):
    letter_key_width = 55
    letter_key_height = 51
    keyboard_padding = 3
    key_margin = 10
    key_color = pygame.Color('grey')
    font_color = key_color.__invert__()

    font_size = letter_key_width//4
    font = pygame.font.SysFont('Arial', font_size)
    font_color = key_color.__invert__()
    txt_xpadding = letter_key_width//6
    txt_ypadding = letter_key_width//10

    keyboard_layout = KeyboardLayout(
        position,
        keyboard_layout,
        keyboard_padding,
        letter_key_width,
        letter_key_height,
        key_margin,
        key_color,
        font_color,
        font,
        txt_xpadding,
        txt_ypadding,
        keyboard_color=font_color
    )
    # keyboard_layout.update_key(
    #     "return",
    #     bg_color=pygame.Color('white'),
    #     font_color=pygame.Color('red')
    # )
    return keyboard_layout


if __name__=="__main__":
    layout_name = 'azerty'
    # layout_name = 'qwerty'
    screen = init_pygame_and_draw_keyboard(layout_name)
    run_until_window_closed()
