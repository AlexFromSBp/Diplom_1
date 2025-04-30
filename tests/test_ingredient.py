import pytest

from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import *

class TestIngredient:

    def test_get_price(self): # получить цену за ингредиент
        ingredient = Ingredient('Начинка', 'Говяжий метеорит (отбивная)', 3000)
        assert ingredient.get_price() == 3000

    def test_get_name(self): # получить название ингредиента
        ingredient = Ingredient('Начинка', 'Говяжий метеорит (отбивная)', 3000)
        assert ingredient.get_name() == 'Говяжий метеорит (отбивная)'

    @pytest.mark.parametrize(
        'type, name, price, expected_ingredient',
        [
            [INGREDIENT_TYPE_SAUCE, 'Соус традиционный галактический', 15, 'SAUCE'],
            [INGREDIENT_TYPE_FILLING, 'Хрустящие минеральные кольца', 300, 'FILLING']
        ]
    )
    def test_get_type_correct_type(self, type, name, price, expected_ingredient): # получить тип ингредиента
        ingredient = Ingredient(type, name, price)
        assert ingredient.get_type() == expected_ingredient
