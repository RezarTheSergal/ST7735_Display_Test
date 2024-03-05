import ST7735


# инициализация дисплея (применяется однажды при запуске приложения)
def initialize_display():
    return ST7735.ST7735(port=0, cs=0, dc=24, backlight=None, rst=25, width=128, height=160, rotation=90, offset_left=0,
                         offset_top=0, invert=False)
