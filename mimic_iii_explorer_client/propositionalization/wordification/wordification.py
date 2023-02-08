from typing import List

from generated_client import WordificationConfig, WordificationResult
from mimic_iii_explorer_client.client.wordification_api_client import PropositionalizationApiClient
from mimic_iii_explorer_client.propositionalization import logger


def compute_wordification(wordification_config: WordificationConfig) -> List[WordificationResult]:
    """Compute Wordification.

    :param wordification_config: request body for clinical text extraction
    :return: root entity ids and concatenated extracted text for that root entity
    """
    logger.info('Requesting mimic-iii-explorer to extract the clinical texts')

    return PropositionalizationApiClient().wordification(wordification_config)
