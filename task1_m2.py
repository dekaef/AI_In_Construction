# TODO Написать 3 класса с документацией и аннотацией типов

if __name__ == "__main__":
    # TODO работоспособность экземпляров класса проверить с помощью doctest
    pass

import doctest

class Table:
    """
    Класс, описывающий объект "Стол".
    """

    def __init__(self, material: str, length: float, width: float):
        """
        Создание и подготовка объекта "Стол".

        :param material: Материал стола.
        :param length: Длина стола.
        :param width: Ширина стола.

        Примеры:
        >>> table = Table("Дерево", 1.5, 0.8)
        """
        if not isinstance(material, str):
            raise TypeError("Материал должен быть строкой.")
        if not isinstance(length, (int, float)) or length <= 0:
            raise ValueError("Длина должна быть положительным числом.")
        if not isinstance(width, (int, float)) or width <= 0:
            raise ValueError("Ширина должна быть положительным числом.")

        self.material = material
        self.length = length
        self.width = width

    def calculate_area(self) -> float:
        """
        Расчет площади стола.

        :return: Площадь стола.

        Примеры:
        >>> table = Table("Дерево", 1.5, 0.8)
        >>> table.calculate_area()
        1.2
        """
        return round(self.length * self.width, 2)

    def clean(self, cleaner: str) -> None:
        """
        Очистка стола с использованием указанного средства.

        :param cleaner: Средство для чистки.

        Примеры:
        >>> table = Table("Дерево", 1.5, 0.8)
        >>> table.clean("Wood Cleaner")
        """
        if not isinstance(cleaner, str) or not cleaner:
            raise ValueError("Название средства для чистки должно быть строкой.")
        pass

class Tree:
    """
    Класс, описывающий объект "Дерево".
    """

    def __init__(self, species: str, height: float):
        """
        Создание и подготовка объекта "Дерево".

        :param species: Вид дерева.
        :param height: Высота дерева.

        Примеры:
        >>> tree = Tree("Дуб", 10)
        """
        if not isinstance(species, str):
            raise TypeError("Вид дерева должен быть строкой.")
        if not isinstance(height, (int, float)) or height <= 0:
            raise ValueError("Высота дерева должна быть положительным числом.")

        self.species = species
        self.height = height

    def grow(self, years: int) -> None:
        """
        Увеличивает высоту дерева за указанный период.

        :param years: Количество лет.

        Примеры:
        >>> tree = Tree("Дуб", 10)
        >>> tree.grow(5)
        """
        if not isinstance(years, int) or years < 0:
            raise ValueError("Количество лет должно быть неотрицательным целым числом.")
        self.height += years * 0.5

    def photosynthesize(self) -> str:
        """
        Процесс фотосинтеза дерева.

        :return: Сообщение о процессе фотосинтеза.

        Примеры:
        >>> tree = Tree("Дуб", 10)
        >>> tree.photosynthesize()
        'Дерево поглощает углекислый газ и выделяет кислород.'
        """
        return "Дерево поглощает углекислый газ и выделяет кислород."

class Book:
    """
    Класс, описывающий объект "Книга".
    """

    def __init__(self, title: str, author: str, pages: int):
        """
        Создание и подготовка объекта "Книга".

        :param title: Название книги.
        :param author: Автор книги.
        :param pages: Количество страниц.

        Примеры:
        >>> book = Book("Гарри Поттер", "Дж. К. Роулинг", 500)
        """
        if not isinstance(title, str) or not title:
            raise ValueError("Название книги должно быть непустой строкой.")
        if not isinstance(author, str) or not author:
            raise ValueError("Имя автора должно быть непустой строкой.")
        if not isinstance(pages, int) or pages <= 0:
            raise ValueError("Количество страниц должно быть положительным целым числом.")

        self.title = title
        self.author = author
        self.pages = pages

    def read(self, pages: int) -> str:
        """
        Чтение указанного количества страниц книги.

        :param pages: Количество читаемых страниц.
        :return: Сообщение о процессе чтения.

        Примеры:
        >>> book = Book("Гарри Поттер", "Дж. К. Роулинг", 500)
        >>> book.read(50)
        'Вы прочитали 50 страниц книги.'
        """
        if not isinstance(pages, int) or pages <= 0:
            raise ValueError("Количество читаемых страниц должно быть положительным числом.")
        if pages > self.pages:
            raise ValueError("Невозможно прочитать больше страниц, чем есть в книге.")
        return f"Вы прочитали {pages} страниц книги."

    def get_summary(self) -> str:
        """
        Получение краткой информации о книге.

        :return: Краткое описание книги.

        Примеры:
        >>> book = Book("Гарри Поттер", "Дж. К. Роулинг", 500)
        >>> book.get_summary()
        'Книга "Гарри Поттер" написана автором Дж. К. Роулинг и содержит 500 страниц.'
        """
        return f"Книга \"{self.title}\" написана автором {self.author} и содержит {self.pages} страниц."

    def bookmark_page(self, page: int) -> str:
        """
        Установка закладки на указанной странице.

        :param page: Номер страницы для закладки.
        :return: Сообщение о добавленной закладке.

        Примеры:
        >>> book = Book("Гарри Поттер", "Дж. К. Роулинг", 500)
        >>> book.bookmark_page(120)
        'Закладка установлена на странице 120.'
        """
        if not isinstance(page, int) or page <= 0 or page > self.pages:
            raise ValueError("Номер страницы для закладки должен быть в пределах книги.")
        return f"Закладка установлена на странице {page}."

if __name__ == "__main__":
    doctest.testmod()
    