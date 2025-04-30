import pytest

from praktikum.burger import Burger
from praktikum.bun import Bun
from praktikum.database import Database
from praktikum.ingredient import Ingredient
from unittest.mock import Mock

class TestBurger:
    def test_set_buns(self): # добавить булку
        burger = Burger()
        bun_mock = Mock(spec=Bun)
        burger.set_buns(bun_mock)
        assert burger.bun == bun_mock

    def test_add_ingredient(self): # добавить ингредиент
        burger = Burger()
        ingredient_mock = Mock(spec=Ingredient)
        burger.add_ingredient(ingredient_mock)
        assert ingredient_mock in burger.ingredients

    def test_remove_ingredient(self): # удалить ингредиент
        burger = Burger()
        mock_ingredient = Mock()
        burger.add_ingredient(mock_ingredient)
        burger.remove_ingredient(0)
        assert len(burger.ingredients) == 0

    def test_move_ingredient(self): # переместить ингредиент
        burger = Burger()
        ingredient_mock1 = Mock(spec=Ingredient)
        ingredient_mock2 = Mock(spec=Ingredient)
        burger.add_ingredient(ingredient_mock1)
        burger.add_ingredient(ingredient_mock2)
        burger.move_ingredient(0, 1)
        assert burger.ingredients == [ingredient_mock2, ingredient_mock1]

    def test_get_price(self): # получить прайс
        bun_mock = Mock()
        bun_mock.get_price.return_value = 100

        ingredient_mock1 = Mock()
        ingredient_mock1.get_price.return_value = 15
        ingredient_mock2 = Mock()
        ingredient_mock2.get_price.return_value = 25

        burger = Burger()
        burger.set_buns(bun_mock)
        burger.add_ingredient(ingredient_mock1)
        burger.add_ingredient(ingredient_mock2)

        expected_price = 100*2 + 15 + 25
        assert burger.get_price() == expected_price

    def test_get_receipt(self): # получить квитанцию
        burger = Burger()
        database = Database()
        burger.set_buns(database.available_buns()[0])
        burger.add_ingredient(database.available_ingredients()[0])
        burger.add_ingredient(database.available_ingredients()[3])
        expected_receipt = "(==== black bun ====)\n" \
                           "= sauce hot sauce =\n" \
                           "= filling cutlet =\n" \
                           "(==== black bun ====)\n\n" \
                           "Price: 400"
        assert expected_receipt == burger.get_receipt()
