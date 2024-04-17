import connexion
from typing import Dict
from typing import Tuple
from typing import Union

from openapi_server.models.product_archetype import ProductArchetype  # noqa: E501
from openapi_server.models.product_archetype_criteria import ProductArchetypeCriteria  # noqa: E501
from openapi_server.models.product_archetype_view import ProductArchetypeView  # noqa: E501
from openapi_server import util


def count_product_archetype():  # noqa: E501
    """Count product archetypes

     # noqa: E501


    :rtype: Union[int, Tuple[int, int], Tuple[int, int, Dict[str, str]]
    """
    return 'do some magic!'


def create_product_archetype(product_archetype_view):  # noqa: E501
    """Create a new product archetype

     # noqa: E501

    :param product_archetype_view: 
    :type product_archetype_view: dict | bytes

    :rtype: Union[int, Tuple[int, int], Tuple[int, int, Dict[str, str]]
    """
    if connexion.request.is_json:
        product_archetype_view = ProductArchetypeView.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def delete_product_archetype(id):  # noqa: E501
    """Delete a product archetype by id

     # noqa: E501

    :param id: 
    :type id: int

    :rtype: Union[bool, Tuple[bool, int], Tuple[bool, int, Dict[str, str]]
    """
    return 'do some magic!'


def get_product_archetype_by_id(id):  # noqa: E501
    """Get product archetype by id

     # noqa: E501

    :param id: 
    :type id: int

    :rtype: Union[ProductArchetype, Tuple[ProductArchetype, int], Tuple[ProductArchetype, int, Dict[str, str]]
    """
    return 'do some magic!'


def get_product_archetype_list(criteria=None):  # noqa: E501
    """Get list of product archetypes

     # noqa: E501

    :param criteria: 
    :type criteria: dict | bytes

    :rtype: Union[List[ProductArchetype], Tuple[List[ProductArchetype], int], Tuple[List[ProductArchetype], int, Dict[str, str]]
    """
    if connexion.request.is_json:
        criteria =  ProductArchetypeCriteria.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def update_product_archetype(id, product_archetype_view):  # noqa: E501
    """Update existing product archetype

     # noqa: E501

    :param id: 
    :type id: int
    :param product_archetype_view: 
    :type product_archetype_view: dict | bytes

    :rtype: Union[bool, Tuple[bool, int], Tuple[bool, int, Dict[str, str]]
    """
    if connexion.request.is_json:
        product_archetype_view = ProductArchetypeView.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
