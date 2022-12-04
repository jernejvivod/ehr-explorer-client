from typing import Sequence, Tuple, List

from generated_client import IdRetrievalSpec, IdRetrievalFilterSpec
from mimic_iii_explorer_client.client.ids_api_client import IdsApiClient
from mimic_iii_explorer_client.extraction import logger


def retrieve_ids(root_entity_name: str,
                 id_property: str,
                 filter_specs: Sequence[Tuple[str]],
                 ) -> List[str]:
    """Extract ids for specified root entity.

    :param root_entity_name: root entity name
    :param id_property: id property of root entity
    :param filter_specs: specifications for entity filters
    :return:
    """
    # initialize client
    client = IdsApiClient()

    # get ids
    ids_req_body = IdRetrievalSpec(
        root_entity_name,
        id_property,
        [IdRetrievalFilterSpec(entity_name=f[0], property_name=f[1], comparator=f[2], property_val=f[3]) for f in filter_specs] if filter_specs is not None else None
    )

    logger.info('Requesting mimic-iii-explorer to retrieve the ids')
    return client.ids(ids_req_body)
