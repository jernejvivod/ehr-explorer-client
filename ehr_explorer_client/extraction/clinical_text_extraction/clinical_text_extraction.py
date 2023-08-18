from typing import List

from generated_client import ClinicalTextResult, ClinicalTextConfig
from ehr_explorer_client.client.clinical_text_api_client import ClinicalTextApiClient
from ehr_explorer_client.extraction import logger


def extract_clinical_text(clinical_text_config: ClinicalTextConfig) -> List[ClinicalTextResult]:
    """Retrieve clinical texts from the MIMIC-III database.

    :param clinical_text_config: request body for clinical text extraction
    :return: root entity ids and concatenated extracted text for that root entity
    """
    logger.info('Requesting ehr-explorer to extract the clinical texts')

    # TODO do batched retrieval
    return ClinicalTextApiClient().clinical_text(clinical_text_config)
