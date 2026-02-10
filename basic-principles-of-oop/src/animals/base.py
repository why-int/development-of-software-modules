# Базовый (родительский) класс Animal (животное)
class Animal:
    """Базовый класс для всех животных."""

    def __init__(self, name: str, species: str, age: int) -> None:
        """
        Инициализатор экземпляра класса Animal.

        :param name: Имя животного
        :type name: str
        :param species: Вид животного
        :type species: str
        :param age: Возраст животного в годах
        :type age: int
        """
        # Инкапсуляция: защищенные атрибуты
        self._name = name
        self._species = species
        self._age = age
        self._is_hungry = True

    # Публичные методы (интерфейс)
    def eat(self, food: str) -> None:
        """
        Покормить животное.

        Если животное голодно, оно ест указанную еду.
        Если не голодно, выводится соответствующее сообщение.

        :param food: Вид пищи для животного
        :type food: str
        """
        if self._is_hungry:
            print(f"{self._name} ест {food}")
            self._is_hungry = False
        else:
            print(f"{self._name} не голоден(а)")

    def sleep(self) -> None:
        """
        Уложить животное спать.

        Выводит сообщение о том, что животное спит.
        """
        print(f"{self._name} спит")

    def make_sound(self) -> None:
        """
        Издать характерный звук животного.

        Этот метод должен быть переопределен в дочерних классах.

        :return: Звук, который издает животное
        :rtype: None
        :raises NotImplementedError: Если метод не переопределен
        """
        raise NotImplementedError(
            "Этот метод должен быть реализован в дочернем классе"
        )

    # Геттеры для доступа к защищенным данным
    def get_name(self) -> str:
        """
        Получить имя животного.

        :return: Имя животного
        :rtype: str
        """
        return self._name

    def get_species(self) -> str:
        """
        Получить вид животного.

        :return: Вид животного
        :rtype: str
        """
        return self._species

    def get_age(self) -> int:
        """
        Получить возраст животного.

        :return: Возраст животного в годах
        :rtype: int
        """
        return self._age

    def is_hungry(self) -> bool:
        """
        Проверить, голодно ли животное.

        :return: True если животное голодно, иначе False
        :rtype: bool
        """
        return self._is_hungry

    def __str__(self) -> str:
        """
        Строковое представление объекта.

        :return: Информация о животном в формате строки
        :rtype: str
        """
        return f"{self._name} ({self._species}), {self._age} лет"

    def __repr__(self) -> str:
        """
        Официальное строковое представление объекта для отладки.

        :return: Строка, которую можно использовать для воссоздания объекта
        :rtype: str
        """
        return f"Animal(name='{self._name}', species='{self._species}', age={self._age})"
