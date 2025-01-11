import doctest


class Tile:
    def __init__(self, tile_area: float, tile_type: str):
        """
        Создание и подготовка к работе объекта "Плитка".
        :param tile_area: Площадь плитки.
        :param tile_type: Вид плитки.
        Примеры:        >>> tile = Tile(4000, "керамическая")
        """

        if not isinstance(tile_area, (int, float)):
            raise TypeError("Площадь должна быть типа int или float")
        if tile_area <= 0:
            raise ValueError("Площадь должна быть положительным числом")
        self.tile_area = tile_area

        if not isinstance(tile_type, (str)):
            raise TypeError("Вид плитки должен быть str")
        self.tile_type = tile_type

    def durability_test(self, pressure: float) -> int:
        """
        Толщина плитки.
        :param thickness: Толщина плитку.
        Примеры:        >>> tile = Tile(40000, "керамическая") >>> tile.thickness(60)
        :return: Толщина плитки.
        """

        if not isinstance(thickness, (int, float)):
            raise TypeError("Толщина должна быть типа int или float")
        if thickness <= 0:
            raise ValueError("Толщина не может быть отрицательной")
        ...
    def water_absorption(self, water_mass: float) -> str:
        """
        Испытание плитки на водопоглощение.
        :param water_mass: Масса воды, поглощенной за время испытания.
        Примеры:        >>> tile = Tile(40000, "керамическая")>>> tile.water_absorption(1000)
        :return: Информация о водопоглощении плитки.
        """
        if not isinstance(water_mass, (int, float)):
            raise TypeError("Масса поглощенной воды должна быть типа int или float")
        if water_mass < 0:
            raise ValueError("Масса воды не может быть отрицательной")
        ...
class Noteb:
    def __init__(self, colour: str, diagonal: float):
        """
        Создание и подготовка к работе объекта "Ноутбук".
        :param colour: Цвет ноутбука.
        :param diagonal: Диагональ ноутбука.
        Примеры:        >>> noteb = Noteb('черный', 16.9)  # инициализация экземпляра класса
        """
        if not isinstance(colour, (str)):
            raise TypeError("Цвет должен быть типа str")
        self.colour = colour

        if not isinstance(diagonal, (int, float)):
            raise TypeError("Диагональ ноутбука должна быть типа int или float")
        if diagonal <= 0:
            raise ValueError("Диагональ экрана у ноутбука должна быть положительным числом")
        self.diagonal = diagonal

    def turn_on(self) -> str:
        """
        Включение ноутбука.
        Примеры:        >>> noteb = Noteb('черный', 16.9)        >>> noteb.turn_on()
        :return: Сообщение о включении.
        """
        ...
    def os(self) -> str:
        """
        Операционная система, установленная на ноутбуке.
        :param os: Название ОС должно быть строкой.
        Примеры:        >>> noteb('черный', 16.9)        >>> noteb.os('Окна')
        :return: Название ОС.
        """
        if not isinstance(os, (str)):
            raise TypeError("Название ОС должно быть словом")
        ...
class Car:
    def __init__(self, brand: str, model: str, year: int, mileage: float):
        """
        Создание объекта "Автомобиль".
        :param brand: Марка автомобиля
        :param model: Модель автомобиля
        :param year: Год выпуска автомобиля
        :param power: Мощность автомобиля в лс
        Примеры:        >>> car = Car('BMW', '525i', 2018, 244000.0)
        """
        if not isinstance(brand, str):
            raise TypeError("Марка автомобиля должна быть str.")
        if not isinstance(model, str):
            raise TypeError("Модель автомобиля должна быть str.")
        if not isinstance(year, int):
            raise TypeError("Год выпуска должен быть целым числом.")
        if year < 1886:
            raise ValueError("Год выпуска не может быть раньше 1886 года.")
        if not isinstance(power, (int, float)) or power < 0:
            raise ValueError("Мощность автомобиля должна быть положительным числом.")
        self.brand = brand
        self.model = model
        self.year = year
        self.power = power

    def chip(self, tuning: float) -> None:
        """
        Увеличивает пробег автомобиля на указанное расстояние.
        :param distance: Пройденное расстояние в километрах.
        Примеры:        >>> car = Car('BMW', '525i', 2018, 244000.0)        >>> car.chip(200.0)
        :return: Новое значение пробега с учетом пройденного расстояния.
        """
        if tuning < 0:
            raise ValueError("Увеличение мощности не должно быть меньше нуля.")
        self.power += tuning
        ...
    def age(self) -> int:
        """
        Вычисляет возраст автомобиля в годах с использованием функции from datetime import date.
        Примеры:        >>> car = Car('BMW', '525i', 2018, 244000.0)        >>> car.age()
        :return: Возраст автомобиля.
        """
        ...


if __name__ == "__main__":
    doctest.testmod()

