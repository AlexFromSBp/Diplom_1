import pytest

from praktikum.bun import Bun


class TestBun:

    def test_bun_generate(self): #Генерация позиции
        bun = Bun("Черная планета X", 123)
        assert bun.name == "Черная планета X"
        assert bun.price == 123

    def test_get_name(self): #Проверка названия
        bun = Bun('Черная планета X', 123)
        assert bun.get_name() == 'Черная планета X'

    def test_get_price(self): #Проверка прайса
        bun = Bun('Черная планета X', 123)
        assert bun.get_price() == 123
