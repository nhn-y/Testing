from saleappv1.eapp.test.test_base import test_client, test_app

def test_add_to_cart_first_time(test_client):
    response = test_client.post('/api/carts', json={
        "id": 1,
        "name": "Laptop",
        "price": 50
    })
    assert response.status_code == 200
    data = response.get_json()

    assert data['total_quantity'] == 1
    assert data['total_amount'] == 50

def test_add_to_cart_increase_item(test_client):
    test_client.post('/api/carts', json={
        "id": 1,
        "name": "Laptop",
        "price": 50
    })

    response = test_client.post('/api/carts', json={
        "id": 2,
        "name": "Laptop",
        "price": 30
    })
    assert response.status_code == 200
    data = response.get_json()

    assert data['total_quantity'] == 2
    assert data['total_amount'] == 80

def test_add_to_cart_existing_item(test_client):
    with test_client.session_transaction() as session:
        session ['cart'] = {
            "1": {
                "id": "1",
                "name": "aaaa",
                "price": 30,
                "quantity": 2
            }
        }
    response = test_client.post('/api/carts', json={
        "id": 1,
        "name": "iphone 17",
        "price": 30
    })

    assert response.status_code == 200
    data = response.get_json()

    assert data['total_quantity'] == 3
    assert data['total_amount'] == 90

    with test_client.session_transaction() as session:
        cart = session['cart']

        assert len(cart) == 1
        assert "1" in cart

def test_update_success(test_client):
    with test_client.session_transaction() as session:
        session ['cart'] = {
            "1": {
                "id": "1",
                "name": "aaaa",
                "price": 30,
                "quantity": 2
            }
        }
    test_client.put('/api/carts/1', json = {
        'quantity': 8

    })