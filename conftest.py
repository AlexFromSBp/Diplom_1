import pytest
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from praktikum import Bun
from praktikum import Ingredient


@pytest.fixture
def ingredient(ingredient_type, name, price):
    ingredient = Ingredient(ingredient_type, name, price)
    return ingredient

@pytest.fixture
def bun(name, price):
    bun = Bun(name, price)
    return bun
