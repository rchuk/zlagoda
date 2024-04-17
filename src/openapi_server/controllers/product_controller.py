import connexion
from typing import Dict
from typing import Tuple
from typing import Union

from openapi_server.models.product import Product  # noqa: E501
from openapi_server.models.product_criteria import ProductCriteria  # noqa: E501
from openapi_server.models.product_view import ProductView  # noqa: E501
from openapi_server import util


def count_product(criteria=None):  # noqa: E501
    """Count products

     # noqa: E501

    :param criteria: 
    :type criteria: dict | bytes

    :rtype: Union[int, Tuple[int, int], Tuple[int, int, Dict[str, str]]
    """
    if connexion.request.is_json:
        criteria =  ProductCriteria.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def create_product(product_view):  # noqa: E501
    """Create a new product

     # noqa: E501

    :param product_view: 
    :type product_view: dict | bytes

    :rtype: Union[int, Tuple[int, int], Tuple[int, int, Dict[str, str]]
    """
    if connexion.request.is_json:
        product_view = ProductView.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def delete_product(id):  # noqa: E501
    """Delete a product by id

     # noqa: E501

    :param id: 
    :type id: int

    :rtype: Union[bool, Tuple[bool, int], Tuple[bool, int, Dict[str, str]]
    """
    return 'do some magic!'


def get_product_by_id(id):  # noqa: E501
    """Get product by id

     # noqa: E501

    :param id: 
    :type id: int

    :rtype: Union[Product, Tuple[Product, int], Tuple[Product, int, Dict[str, str]]
    """
    return 'do some magic!'


def get_product_list(criteria=None):  # noqa: E501
    """Get list of products

     # noqa: E501

    :param criteria: 
    :type criteria: dict | bytes

    :rtype: Union[List[Product], Tuple[List[Product], int], Tuple[List[Product], int, Dict[str, str]]
    """
    if connexion.request.is_json:
        criteria =  ProductCriteria.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def update_prodact(id, product_view):  # noqa: E501
    """Update existing product

     # noqa: E501

    :param id: 
    :type id: int
    :param product_view: 
    :type product_view: dict | bytes

    :rtype: Union[bool, Tuple[bool, int], Tuple[bool, int, Dict[str, str]]
    """
    if connexion.request.is_json:
        product_view = ProductView.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
