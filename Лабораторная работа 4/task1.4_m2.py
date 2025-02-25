class MusicalInstrument:
    """Базовый класс для музыкальных инструментов."""

    def __init__(self, name: str, material: str, origin: str):
        """
        Инициализация музыкального инструмента.

        :param name: Название инструмента.
        :param material: Основной материал изготовления.
        :param origin: Страна происхождения инструмента.
        """
        self.name = name
        self.material = material
        self.origin = origin

    def __str__(self) -> str:
        """Возвращает строковое представление музыкального инструмента."""
        return f"{self.name} (Материал: {self.material}, Страна: {self.origin})"

    def __repr__(self) -> str:
        """Возвращает строковое представление для отладки."""
        return f"MusicalInstrument('{self.name}', '{self.material}', '{self.origin}')"

    def play(self) -> str:
        """Имитация игры на инструменте."""
        return f"Играет на {self.name}."


class StringInstrument(MusicalInstrument):
    """Класс для струнных инструментов, наследуется от MusicalInstrument."""

    def __init__(self, name: str, material: str, origin: str, number_of_strings: int):
        """
        Инициализация струнного инструмента.

        :param name: Название инструмента.
        :param material: Основной материал изготовления.
        :param origin: Страна происхождения инструмента.
        :param number_of_strings: Количество струн.
        """
        super().__init__(name, material, origin)
        self.number_of_strings = number_of_strings

    def __str__(self) -> str:
        """Возвращает строковое представление струнного инструмента."""
        return f"{super().__str__()} | Количество струн: {self.number_of_strings}"

    def tune(self) -> str:
        """Метод настройки струнного инструмента."""
        return f"{self.name} настроен, можно играть!"


class PercussionInstrument(MusicalInstrument):
    """Класс для ударных инструментов, наследуется от MusicalInstrument."""

    def __init__(self, name: str, material: str, origin: str, is_tunable: bool):
        """
        Инициализация ударного инструмента.

        :param name: Название инструмента.
        :param material: Основной материал изготовления.
        :param origin: Страна происхождения инструмента.
        :param is_tunable: Можно ли настраивать инструмент.
        """
        super().__init__(name, material, origin)
        self.is_tunable = is_tunable  # Этот атрибут специфичен для ударных инструментов

    def __str__(self) -> str:
        """Возвращает строковое представление ударного инструмента."""
        return f"{super().__str__()} | Настраиваемый: {'Да' if self.is_tunable else 'Нет'}"

    def play(self) -> str:
        """
        Переопределенный метод игры на инструменте.

        В отличие от других инструментов, ударные могут звучать громче и иметь другой характер исполнения.
        """
        return f"Барабанит на {self.name} энергично!"


# Пример использования классов
if __name__ == "__main__":
    guitar = StringInstrument("Гитара", "Дерево", "Испания", 6)
    drum = PercussionInstrument("Барабан", "Кожа и металл", "Африка", True)

    print(guitar)
    print(drum)

    print(guitar.play())
    print(guitar.tune())

    print(drum.play())
