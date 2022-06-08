from typing import Sequence, Tuple, List

from mimic_iii_analysis.mimic_iii_explorer_client.client import Client
from mimic_iii_analysis.mimic_iii_explorer_client.model.id_retrieval_spec import IdRetrievalSpec, IdRetrievalFilterSpec


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
    client = Client()

    # get ids
    ids_req_body = IdRetrievalSpec(
        root_entity_name,
        id_property,
        [IdRetrievalFilterSpec(f[0], f[1], f[2], f[3]) for f in filter_specs] if filter_specs is not None else None
    )
    return client.retrieve_ids(ids_req_body)
