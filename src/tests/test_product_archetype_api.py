# coding: utf-8

from fastapi.testclient import TestClient


from openapi_server.models.product_archetype import ProductArchetype  # noqa: F401
from openapi_server.models.product_archetype_criteria import ProductArchetypeCriteria  # noqa: F401
from openapi_server.models.product_archetype_view import ProductArchetypeView  # noqa: F401


def test_count_product_archetype(client: TestClient):
    """Test case for count_product_archetype

    Count product archetypes
    """

    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/api/product-archetype/count",
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_create_product_archetype(client: TestClient):
    """Test case for create_product_archetype

    Create a new product archetype
    """
    product_archetype_view = {"name":"name","description":"description","category":0,"manufacturer":"manufacturer"}

    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "PUT",
    #    "/api/product-archetype",
    #    headers=headers,
    #    json=product_archetype_view,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_delete_product_archetype(client: TestClient):
    """Test case for delete_product_archetype

    Delete a product archetype by id
    """

    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "DELETE",
    #    "/api/product-archetype/{id}".format(id=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_get_product_archetype_by_id(client: TestClient):
    """Test case for get_product_archetype_by_id

    Get product archetype by id
    """

    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/api/product-archetype/{id}".format(id=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_get_product_archetype_list(client: TestClient):
    """Test case for get_product_archetype_list

    Get list of product archetypes
    """
    params = [("criteria", openapi_server.ProductArchetypeCriteria())]
    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/api/product-archetype",
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_update_product_archetype(client: TestClient):
    """Test case for update_product_archetype

    Update existing product archetype
    """
    product_archetype_view = {"name":"name","description":"description","category":0,"manufacturer":"manufacturer"}

    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "POST",
    #    "/api/product-archetype/{id}".format(id=56),
    #    headers=headers,
    #    json=product_archetype_view,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

