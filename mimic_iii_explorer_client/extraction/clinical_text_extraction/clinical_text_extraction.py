from typing import List

from generated_client import ClinicalTextResult, ClinicalTextConfig
from mimic_iii_explorer_client.client.clinical_text_api_client import ClinicalTextApiClient
from mimic_iii_explorer_client.extraction import logger


def extract_clinical_text(clinical_text_config: ClinicalTextConfig) -> List[ClinicalTextResult]:
    """Retrieve clinical texts from the MIMIC-III database.

    :param clinical_text_config: request body for clinical text extraction
    :return: root entity ids and concatenated extracted text for that root entity
    """
    logger.info('Requesting mimic-iii-explorer to extract the clinical texts')

    return ClinicalTextApiClient().clinical_text(clinical_text_config)
