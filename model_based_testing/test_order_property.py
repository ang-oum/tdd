from hypothesis import given
from hypothesis.strategies import integers

from order import LineItem


@given(integers(),integers())
def test_line_item(price: int, quantity: int)->None:
    line_item = LineItem("Apple", price, quantity)
    assert line_item.total == price * quantity

#pytest will test many inputs/properties

#actions->rules
#sanitychecks->invariants

