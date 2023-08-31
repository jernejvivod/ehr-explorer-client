from typing import List

from ehr_explorer_client.client.wordification_api_client import PropositionalizationApiClient
from ehr_explorer_client.propositionalization import logger
from generated_client import WordificationConfig, WordificationResult


def compute_wordification(wordification_config: WordificationConfig) -> List[WordificationResult]:
    """Compute Wordification.

    :param wordification_config: request body for clinical text extraction
    :return: root entity ids and concatenated extracted text for that root entity
    """
    logger.info('Requesting ehr-explorer to extract the clinical texts')

    api_client = PropositionalizationApiClient()
    ids = wordification_config.root_entities_spec.ids

    results = []
    for ids_partition in _partition(ids, 1000):
        wordification_config.root_entities_spec.ids = ids_partition
        results.extend(api_client.wordification(wordification_config))

    return results


def _partition(ids, batch_size):
    """Partition iterable of IDs into a tuple of partitions.

    :param ids: ids to partition
    :param batch_size: batch size
    """
    return (ids[pos:pos + batch_size] for pos in range(0, len(ids), batch_size))
