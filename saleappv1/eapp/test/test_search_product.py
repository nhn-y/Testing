from eapp.dao import load_products
from eapp.test.test_base import sample_product, test_session, test_app


def test_all(sample_product):
    actual_product = load_products()
    assert  len(actual_product) == len(sample_product)

def test_zero(sample_product):
    actual_product = load_products(kw='fdsfkdshfds')
    assert len(actual_product) == 0

def test_kw(sample_product):
    actual_product = load_products(kw='iPhone')
    assert len(actual_product) == 2
    assert all('iPhone'in p.name for p in actual_product)

def test_cateid(sample_product):
    actual_product = load_products(cate_id=2)
    assert  len(actual_product) ==2
    assert all( p.category_id ==2 for p in actual_product)

def test_kw_cate(sample_product):
    actual_product = load_products(kw='iPhone', cate_id=1)
    assert len(actual_product) == 1
    assert actual_product[0].name == 'iPhone 17'