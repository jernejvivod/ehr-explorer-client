from typing import List

from generated_client import WordificationConfig, WordificationResult
from ehr_explorer_client.client.wordification_api_client import PropositionalizationApiClient
from ehr_explorer_client.propositionalization import logger


def compute_wordification(wordification_config: WordificationConfig) -> List[WordificationResult]:
    """Compute Wordification.

    :param wordification_config: request body for clinical text extraction
    :return: root entity ids and concatenated extracted text for that root entity
    """
    logger.info('Requesting ehr-explorer to extract the clinical texts')

    return PropositionalizationApiClient().wordification(wordification_config)
