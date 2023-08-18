from typing import List

from ehr_explorer_client.client.clinical_text_api_client import ClinicalTextApiClient
from ehr_explorer_client.extraction import logger
from generated_client import ClinicalTextResult, ClinicalTextConfig


def extract_clinical_text(clinical_text_config: ClinicalTextConfig) -> List[ClinicalTextResult]:
    """Retrieve clinical texts from the MIMIC-III database.

    :param clinical_text_config: request body for clinical text extraction
    :return: root entity ids and concatenated extracted text for that root entity
    """
    logger.info('Requesting ehr-explorer to extract the clinical texts')

    api_client = ClinicalTextApiClient()
    ids = clinical_text_config.root_entities_spec.ids

    results = []
    for ids_partition in _partition(ids, 1000):
        clinical_text_config.root_entities_spec.ids = ids_partition
        results.extend(api_client.clinical_text(clinical_text_config))

    return results


def _partition(ids, batch_size):
    """Partition iterable of IDs into a tuple of partitions.

    :param ids: ids to partition
    :param batch_size: batch size
    """
    return (ids[pos:pos + batch_size] for pos in range(0, len(ids), batch_size))
