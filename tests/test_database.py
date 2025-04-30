import pytest
from praktikum.database import Database


class TestDatabase:

    def test_available_buns(self): # проверить доступность булочек
        database = Database()
        buns = database.available_buns()
        available_buns = len(buns)
        assert available_buns == 3 and buns[available_buns - 1].name == 'red bun'

    def test_available_ingredients(self): # проверить доступность ингредиентов
        database = Database()
        ingredients = database.available_ingredients()
        available_ingredients = len(ingredients)
        assert available_ingredients == 6 and ingredients[available_ingredients - 1].name == 'sausage'
