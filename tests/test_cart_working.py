import pytest
from .data_providers import valid_product
from time import sleep




@pytest.mark.parametrize("product", valid_product, ids=[repr(x) for x in valid_product])
def test_cart_working(app, product):
    app.add_new_product_to_cart(product)
    sleep(2)
    app.del_product_from_cart(product)

@pytest.mark.parametrize("product", valid_product, ids=[repr(x) for x in valid_product])
def test_cart_working2(app,product):
    old_NOP=app.get_quantity_of_product_in_cart_on_prod_page()
    print(old_NOP)
    app.add_new_product_to_cart(product)
    new_NOP=app.get_quantity_of_product_in_cart_on_prod_page()
    print(new_NOP)
    assert old_NOP+1 == new_NOP

    app.del_product_from_cart(product)
    newnew_NOP=app.get_quantity_of_product_in_cart_on_prod_page()
    assert new_NOP-1 == newnew_NOP

def test_cart_working2(app):
    old_NOP=app.get_quantity_of_product_in_cart_on_prod_page()
    app.add_random_distinct_prod(3)
    new_NOP=app.get_quantity_of_product_in_cart_on_prod_page()
    assert old_NOP+3 == new_NOP

    app.delete_all_from_cart()
    newnew_NOP=app.get_quantity_of_product_in_cart_on_prod_page()
    assert newnew_NOP == 0


















    #app.add_random_product_to_cart(product)
    # sleep(2)
    # app.del_product_from_cart(product)



    # old_ids = app.get_customer_ids()
    #
    # app.register_new_customer(customer)
    #
    # new_ids = app.get_customer_ids()
    #
    # assert all([i in new_ids for i in old_ids])
    # assert len(new_ids) == len(old_ids) + 1
