import pytest
from .data_providers import valid_product
from time import sleep


@pytest.mark.parametrize("product", valid_product, ids=[repr(x) for x in valid_product])
def test_cart_working(app, product):
    app.add_new_product_to_cart(product)
    sleep(10)


    # old_ids = app.get_customer_ids()
    #
    # app.register_new_customer(customer)
    #
    # new_ids = app.get_customer_ids()
    #
    # assert all([i in new_ids for i in old_ids])
    # assert len(new_ids) == len(old_ids) + 1
