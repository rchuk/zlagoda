import connexion
from typing import Dict
from typing import Tuple
from typing import Union

from openapi_server.models.receipt import Receipt  # noqa: E501
from openapi_server.models.receipt_criteria import ReceiptCriteria  # noqa: E501
from openapi_server.models.receipt_view import ReceiptView  # noqa: E501
from openapi_server import util


def count_receipt(criteria=None):  # noqa: E501
    """Count receipts

     # noqa: E501

    :param criteria: 
    :type criteria: dict | bytes

    :rtype: Union[int, Tuple[int, int], Tuple[int, int, Dict[str, str]]
    """
    if connexion.request.is_json:
        criteria =  ReceiptCriteria.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def create_receipt(receipt_view):  # noqa: E501
    """Create a new receipt

     # noqa: E501

    :param receipt_view: 
    :type receipt_view: dict | bytes

    :rtype: Union[int, Tuple[int, int], Tuple[int, int, Dict[str, str]]
    """
    if connexion.request.is_json:
        receipt_view = ReceiptView.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def delete_receipt(id):  # noqa: E501
    """Delete a receipt by id

     # noqa: E501

    :param id: 
    :type id: int

    :rtype: Union[bool, Tuple[bool, int], Tuple[bool, int, Dict[str, str]]
    """
    return 'do some magic!'


def get_receipt_by_id(id):  # noqa: E501
    """Get receipt by id

     # noqa: E501

    :param id: 
    :type id: int

    :rtype: Union[Receipt, Tuple[Receipt, int], Tuple[Receipt, int, Dict[str, str]]
    """
    return 'do some magic!'


def get_receipt_list(criteria=None):  # noqa: E501
    """Get list of receipts

     # noqa: E501

    :param criteria: 
    :type criteria: dict | bytes

    :rtype: Union[List[Receipt], Tuple[List[Receipt], int], Tuple[List[Receipt], int, Dict[str, str]]
    """
    if connexion.request.is_json:
        criteria =  ReceiptCriteria.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
