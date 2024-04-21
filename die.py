from random import randint
class Die():
    """Класс, представляющий 1 кубик"""

    def __init__(self, num_sides=6):
        """По умолчанию шестигранный кубик"""
        self.num_sides = num_sides

    def roll(self):
        return randint(1, self.num_sides)