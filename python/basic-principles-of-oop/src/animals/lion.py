from .base import Animal


class Lion(Animal):
    """Класс, представляющий льва."""

    def __init__(self, name: str, age: int, mane_size: str = "средняя") -> None:
        """
        Инициализатор экземпляра класса Lion.

        :param name: Имя льва
        :type name: str
        :param age: Возраст льва в годах
        :type age: int
        :param mane_size: Размер гривы (маленькая, средняя, большая)
        :type mane_size: str
        :default mane_size: "средняя"
        """
        # Вызываем конструктор родительского класса
        super().__init__(name, "Лев", age)

        # Дополнительные атрибуты, специфичные для львов
        self._mane_size = mane_size
        self._pride_leader = False

    # Переопределяем метод make_sound (полиморфизм)
    def make_sound(self) -> None:
        """
        Лев рычит.

        :return: Звук, который издает лев
        :rtype: str
        """
        print(f"{self._name} рычит!")

    # Специфичные для льва методы
    def become_pride_leader(self) -> None:
        """
        Сделать льва вожаком прайда.
        """
        self._pride_leader = True
        print(f"{self._name} теперь вожак прайда!")

    def hunt(self, prey: str) -> None:
        """
        Лев охотится на добычу.

        :param prey: Добыча, на которую охотится лев
        :type prey: str
        """
        print(f"{self._name} охотится на {prey}")
        # После охоты лев голоден
        self._is_hungry = True

    def get_mane_size(self) -> str:
        """
        Получить размер гривы льва.

        :return: Размер гривы
        :rtype: str
        """
        return self._mane_size

    def is_pride_leader(self) -> bool:
        """
        Проверить, является ли лев вожаком прайда.

        :return: True если лев вожак прайда, иначе False
        :rtype: bool
        """
        return self._pride_leader

    # Переопределяем родительский метод для учета специфики льва
    def eat(self, food: str) -> None:
        """
        Покормить льва (с учетом того, что львы - хищники).

        :param food: Вид пищи для льва
        :type food: str
        """
        # Львы предпочитают мясо
        if (
            "мясо" in food.lower()
            or "антилоп" in food.lower()
            or "зебр" in food.lower()
        ):
            if self._is_hungry:
                print(f"{self._name} с удовольствием ест {food}")
                self._is_hungry = False
            else:
                print(
                    f"{self._name} не голоден, он приберегает {food} на потом"
                )
        else:
            print(f"Львы не едят {food}! {self._name} отказывается есть {food}")

    # Переопределяем строковое представление
    def __str__(self) -> str:
        """
        Строковое представление льва.

        :return: Информация о льве в формате строки
        :rtype: str
        """
        leader_status = " (вожак прайда)" if self._pride_leader else ""
        return f"Лев {self._name}, {self._age} лет, грива: {self._mane_size}{leader_status}"

    def __repr__(self) -> str:
        """
        Официальное строковое представление объекта для отладки.

        :return: Строка, которую можно использовать для воссоздания объекта
        :rtype: str
        """
        return f"Lion(name='{self._name}', age={self._age}, mane_size='{self._mane_size}')"


# Дополнительно: можно создать класс для львицы
class Lioness(Lion):
    """Класс, представляющий львицу."""

    def __init__(self, name: str, age: int, cubs_count: int = 0) -> None:
        """
        Инициализатор экземпляра класса Lioness.

        :param name: Имя львицы
        :type name: str
        :param age: Возраст львицы в годах
        :type age: int
        :param cubs_count: Количество детенышей
        :type cubs_count: int
        :default cubs_count: 0
        """
        # Львицы не имеют гривы
        super().__init__(name, age, mane_size="нет")
        self._cubs_count = cubs_count
        self._is_hunting = False

    def give_birth(self, cubs: int = 1) -> None:
        """
        Львица рожает детенышей.

        :param cubs: Количество родившихся детенышей
        :type cubs: int
        :default cubs: 1
        """
        self._cubs_count += cubs
        print(f"У львицы {self._name} родилось {cubs} детеныша(ей)!")

    def get_cubs_count(self) -> int:
        """
        Получить количество детенышей львицы.

        :return: Количество детенышей
        :rtype: int
        """
        return self._cubs_count

    def __str__(self) -> str:
        """
        Строковое представление львицы.

        :return: Информация о львице в формате строки
        :rtype: str
        """
        cubs_info = (
            f", детенышей: {self._cubs_count}" if self._cubs_count > 0 else ""
        )
        return f"Львица {self._name}, {self._age} лет{cubs_info}"
