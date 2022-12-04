from typing import List

from generated_client import IdRetrievalSpec
from mimic_iii_explorer_client.client.ids_api_client import IdsApiClient
from mimic_iii_explorer_client.extraction import logger


def retrieve_ids(id_retrieval_spec: IdRetrievalSpec) -> List[str]:
    """Extract ids for specified root entity.

    :param id_retrieval_spec: request body for ID retrieval
    :return: retrieved IDs
    """
    logger.info('Requesting mimic-iii-explorer to retrieve the ids')

    return IdsApiClient().ids(id_retrieval_spec)
