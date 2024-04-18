# coding: utf-8

from fastapi.testclient import TestClient


from openapi_server.models.receipt import Receipt  # noqa: F401
from openapi_server.models.receipt_criteria import ReceiptCriteria  # noqa: F401
from openapi_server.models.receipt_view import ReceiptView  # noqa: F401


def test_count_receipt(client: TestClient):
    """Test case for count_receipt

    Count receipts
    """
    params = [("criteria", openapi_server.ReceiptCriteria())]
    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/api/receipt/count",
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_create_receipt(client: TestClient):
    """Test case for create_receipt

    Create a new receipt
    """
    receipt_view = {"customer_card_id":0,"items":[{"product":6,"quantity":1},{"product":6,"quantity":1}]}

    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "PUT",
    #    "/api/receipt",
    #    headers=headers,
    #    json=receipt_view,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_delete_receipt(client: TestClient):
    """Test case for delete_receipt

    Delete a receipt by id
    """

    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "DELETE",
    #    "/api/receipt/{id}".format(id=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_get_receipt_by_id(client: TestClient):
    """Test case for get_receipt_by_id

    Get receipt by id
    """

    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/api/receipt/{id}".format(id=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_get_receipt_list(client: TestClient):
    """Test case for get_receipt_list

    Get list of receipts
    """
    params = [("criteria", openapi_server.ReceiptCriteria())]
    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/api/receipt",
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

