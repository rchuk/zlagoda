# coding: utf-8

from fastapi.testclient import TestClient


from openapi_server.models.product_category import ProductCategory  # noqa: F401
from openapi_server.models.product_category_criteria import ProductCategoryCriteria  # noqa: F401
from openapi_server.models.product_category_view import ProductCategoryView  # noqa: F401


def test_count_product_category(client: TestClient):
    """Test case for count_product_category

    Count product categories
    """

    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/api/product-category/count",
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_create_product_category(client: TestClient):
    """Test case for create_product_category

    Create a new product category
    """
    product_category_view = {"name":"name"}

    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "PUT",
    #    "/api/product-category/",
    #    headers=headers,
    #    json=product_category_view,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_delete_product_category(client: TestClient):
    """Test case for delete_product_category

    Delete a product category by id
    """

    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "DELETE",
    #    "/api/product-category/{id}".format(id=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_get_product_category_by_id(client: TestClient):
    """Test case for get_product_category_by_id

    Get product category by id
    """

    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/api/product-category/{id}".format(id=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_get_product_category_list(client: TestClient):
    """Test case for get_product_category_list

    Get list of product categories
    """
    params = [("criteria", openapi_server.ProductCategoryCriteria())]
    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/api/product-category/",
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_update_product_category(client: TestClient):
    """Test case for update_product_category

    Update existing product category
    """
    product_category_view = {"name":"name"}

    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "POST",
    #    "/api/product-category/{id}".format(id=56),
    #    headers=headers,
    #    json=product_category_view,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

