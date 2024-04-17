import connexion
from typing import Dict
from typing import Tuple
from typing import Union

from openapi_server.models.employee import Employee  # noqa: E501
from openapi_server.models.employee_criteria import EmployeeCriteria  # noqa: E501
from openapi_server.models.employee_view import EmployeeView  # noqa: E501
from openapi_server import util


def count_employee(criteria=None):  # noqa: E501
    """Count employees

     # noqa: E501

    :param criteria: 
    :type criteria: dict | bytes

    :rtype: Union[int, Tuple[int, int], Tuple[int, int, Dict[str, str]]
    """
    if connexion.request.is_json:
        criteria =  EmployeeCriteria.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def create_employee(employee_view):  # noqa: E501
    """Create a new employee

     # noqa: E501

    :param employee_view: 
    :type employee_view: dict | bytes

    :rtype: Union[int, Tuple[int, int], Tuple[int, int, Dict[str, str]]
    """
    if connexion.request.is_json:
        employee_view = EmployeeView.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def delete_employee(id):  # noqa: E501
    """Delete an employee by id

     # noqa: E501

    :param id: 
    :type id: int

    :rtype: Union[bool, Tuple[bool, int], Tuple[bool, int, Dict[str, str]]
    """
    return 'do some magic!'


def get_employee_by_id(id):  # noqa: E501
    """Get employee by id

     # noqa: E501

    :param id: 
    :type id: int

    :rtype: Union[Employee, Tuple[Employee, int], Tuple[Employee, int, Dict[str, str]]
    """
    return 'do some magic!'


def get_employee_list(criteria=None):  # noqa: E501
    """Get list of employees

     # noqa: E501

    :param criteria: 
    :type criteria: dict | bytes

    :rtype: Union[List[Employee], Tuple[List[Employee], int], Tuple[List[Employee], int, Dict[str, str]]
    """
    if connexion.request.is_json:
        criteria =  EmployeeCriteria.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def get_employee_me():  # noqa: E501
    """Get employee id of self

     # noqa: E501


    :rtype: Union[int, Tuple[int, int], Tuple[int, int, Dict[str, str]]
    """
    return 'do some magic!'


def update_employee(id, employee_view):  # noqa: E501
    """Update existing employee

     # noqa: E501

    :param id: 
    :type id: int
    :param employee_view: 
    :type employee_view: dict | bytes

    :rtype: Union[bool, Tuple[bool, int], Tuple[bool, int, Dict[str, str]]
    """
    if connexion.request.is_json:
        employee_view = EmployeeView.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
