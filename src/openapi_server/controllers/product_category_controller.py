import connexion
from typing import Dict
from typing import Tuple
from typing import Union

from openapi_server.models.product_category import ProductCategory  # noqa: E501
from openapi_server.models.product_category_criteria import ProductCategoryCriteria  # noqa: E501
from openapi_server.models.product_category_view import ProductCategoryView  # noqa: E501
from openapi_server import util


def count_product_category():  # noqa: E501
    """Count product categories

     # noqa: E501


    :rtype: Union[int, Tuple[int, int], Tuple[int, int, Dict[str, str]]
    """
    return 'do some magic!'


def create_product_category(product_category_view):  # noqa: E501
    """Create a new product category

     # noqa: E501

    :param product_category_view: 
    :type product_category_view: dict | bytes

    :rtype: Union[int, Tuple[int, int], Tuple[int, int, Dict[str, str]]
    """
    if connexion.request.is_json:
        product_category_view = ProductCategoryView.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def delete_product_category(id):  # noqa: E501
    """Delete a product category by id

     # noqa: E501

    :param id: 
    :type id: int

    :rtype: Union[bool, Tuple[bool, int], Tuple[bool, int, Dict[str, str]]
    """
    return 'do some magic!'


def get_product_category_by_id(id):  # noqa: E501
    """Get product category by id

     # noqa: E501

    :param id: 
    :type id: int

    :rtype: Union[ProductCategory, Tuple[ProductCategory, int], Tuple[ProductCategory, int, Dict[str, str]]
    """
    return 'do some magic!'


def get_product_category_list(criteria=None):  # noqa: E501
    """Get list of product categories

     # noqa: E501

    :param criteria: 
    :type criteria: dict | bytes

    :rtype: Union[List[ProductCategory], Tuple[List[ProductCategory], int], Tuple[List[ProductCategory], int, Dict[str, str]]
    """
    if connexion.request.is_json:
        criteria =  ProductCategoryCriteria.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def update_product_category(id, product_category_view):  # noqa: E501
    """Update existing product category

     # noqa: E501

    :param id: 
    :type id: int
    :param product_category_view: 
    :type product_category_view: dict | bytes

    :rtype: Union[bool, Tuple[bool, int], Tuple[bool, int, Dict[str, str]]
    """
    if connexion.request.is_json:
        product_category_view = ProductCategoryView.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
