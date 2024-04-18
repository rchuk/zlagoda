# coding: utf-8

from fastapi.testclient import TestClient


from openapi_server.models.employee import Employee  # noqa: F401
from openapi_server.models.employee_criteria import EmployeeCriteria  # noqa: F401
from openapi_server.models.employee_view import EmployeeView  # noqa: F401


def test_count_employee(client: TestClient):
    """Test case for count_employee

    Count employees
    """
    params = [("criteria", openapi_server.EmployeeCriteria())]
    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/api/employee/count",
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_create_employee(client: TestClient):
    """Test case for create_employee

    Create a new employee
    """
    employee_view = {"first_name":"firstName","last_name":"lastName","zip_code":"zipCode","patronymic":"patronymic","phone_number":"phoneNumber","city":"city","street":"street","work_start_date":"2000-01-23","salary":0,"birth_date":"2000-01-23"}

    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "PUT",
    #    "/api/employee",
    #    headers=headers,
    #    json=employee_view,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_delete_employee(client: TestClient):
    """Test case for delete_employee

    Delete an employee by id
    """

    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "DELETE",
    #    "/api/employee/{id}".format(id=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_get_employee_by_id(client: TestClient):
    """Test case for get_employee_by_id

    Get employee by id
    """

    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/api/employee/{id}".format(id=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_get_employee_list(client: TestClient):
    """Test case for get_employee_list

    Get list of employees
    """
    params = [("criteria", openapi_server.EmployeeCriteria())]
    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/api/employee",
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_get_employee_me(client: TestClient):
    """Test case for get_employee_me

    Get employee id of self
    """

    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/api/employee/me",
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_update_employee(client: TestClient):
    """Test case for update_employee

    Update existing employee
    """
    employee_view = {"first_name":"firstName","last_name":"lastName","zip_code":"zipCode","patronymic":"patronymic","phone_number":"phoneNumber","city":"city","street":"street","work_start_date":"2000-01-23","salary":0,"birth_date":"2000-01-23"}

    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "POST",
    #    "/api/employee/{id}".format(id=56),
    #    headers=headers,
    #    json=employee_view,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

