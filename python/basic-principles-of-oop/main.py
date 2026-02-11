# Точка входа для правильного масштабирования проектов (src - Source code, там хранится весь код)
from src.animals import lion

male_lion = lion.Lion(name="Гриша", age=1, mane_size="Большая")
female_lion = lion.Lioness(name="Света", age=2, cubs_count=3)

# Методы
male_lion_story = f"""
Лев по имени {male_lion.get_name()}, возраст {male_lion.get_age()}.
Размер гривы - {male_lion.get_mane_size()}
"""

female_lion_story: str = f"""
Львица по имени {female_lion.get_name()}, возраст {female_lion.get_age()}.
Кол-во детенышей - {female_lion.get_cubs_count()}
"""

print(male_lion_story)
print(female_lion_story)


prey = "Антилопа"

male_lion.make_sound()
male_lion.hunt(prey=prey)
male_lion.eat(food=prey)

female_lion.give_birth(cubs=2)
