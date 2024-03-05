import image
import DisplayMeasurments as D_Ms


def setup():
    # ИНИЦИАЛИЗАЦИЯ ДИСПЛЕЯ ДЛЯ ДАЛЬНЕЙШЕГО ЕГО ИСПОЛЬЗОВАНИЕ ПО ВСЕЙ ПРОГРАММЕ!!
    display = D_Ms.initialize_display()
    # Загрузка изображения приветствия на экран
    image.wellcome_message(display, "wellcome.png")


if __name__ == '__main__':
    setup()
