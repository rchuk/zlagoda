# coding: utf-8

from fastapi.testclient import TestClient


from openapi_server.models.product import Product  # noqa: F401
from openapi_server.models.product_criteria import ProductCriteria  # noqa: F401
from openapi_server.models.product_view import ProductView  # noqa: F401


def test_count_product(client: TestClient):
    """Test case for count_product

    Count products
    """
    params = [("criteria", openapi_server.ProductCriteria())]
    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/api/product/count",
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_create_product(client: TestClient):
    """Test case for create_product

    Create a new product
    """
    product_view = {"archetype":0,"quantity":1,"price":6,"upc":"upc"}

    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "PUT",
    #    "/api/product",
    #    headers=headers,
    #    json=product_view,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_delete_product(client: TestClient):
    """Test case for delete_product

    Delete a product by id
    """

    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "DELETE",
    #    "/api/product/{id}".format(id=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_get_product_by_id(client: TestClient):
    """Test case for get_product_by_id

    Get product by id
    """

    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/api/product/{id}".format(id=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_get_product_list(client: TestClient):
    """Test case for get_product_list

    Get list of products
    """
    params = [("criteria", openapi_server.ProductCriteria())]
    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/api/product",
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_update_prodact(client: TestClient):
    """Test case for update_prodact

    Update existing product
    """
    product_view = {"archetype":0,"quantity":1,"price":6,"upc":"upc"}

    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "POST",
    #    "/api/product/{id}".format(id=56),
    #    headers=headers,
    #    json=product_view,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

