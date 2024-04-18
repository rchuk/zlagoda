# coding: utf-8

from fastapi.testclient import TestClient


from openapi_server.models.customer_card import CustomerCard  # noqa: F401
from openapi_server.models.customer_card_criteria import CustomerCardCriteria  # noqa: F401
from openapi_server.models.customer_card_view import CustomerCardView  # noqa: F401


def test_count_customer_card(client: TestClient):
    """Test case for count_customer_card

    Count customer cards
    """
    params = [("criteria", openapi_server.CustomerCardCriteria())]
    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/api/customer-card/count",
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_create_customer_card(client: TestClient):
    """Test case for create_customer_card

    Create a new customer card
    """
    customer_card_view = {"first_name":"firstName","last_name":"lastName","zip_code":"zipCode","patronymic":"patronymic","phone_number":"phoneNumber","discount_percent":0,"city":"city","street":"street"}

    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "PUT",
    #    "/api/customer-card",
    #    headers=headers,
    #    json=customer_card_view,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_delete_customer_card(client: TestClient):
    """Test case for delete_customer_card

    Delete a customer card by id
    """

    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "DELETE",
    #    "/api/customer-card/{id}".format(id=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_get_customer_card_by_id(client: TestClient):
    """Test case for get_customer_card_by_id

    Get customer card by id
    """

    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/api/customer-card/{id}".format(id=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_get_customer_card_list(client: TestClient):
    """Test case for get_customer_card_list

    Get list of customer cards
    """
    params = [("criteria", openapi_server.CustomerCardCriteria())]
    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/api/customer-card",
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_update_customer_card(client: TestClient):
    """Test case for update_customer_card

    Update existing customer card
    """
    customer_card_view = {"first_name":"firstName","last_name":"lastName","zip_code":"zipCode","patronymic":"patronymic","phone_number":"phoneNumber","discount_percent":0,"city":"city","street":"street"}

    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "POST",
    #    "/api/customer-card/{id}".format(id=56),
    #    headers=headers,
    #    json=customer_card_view,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

