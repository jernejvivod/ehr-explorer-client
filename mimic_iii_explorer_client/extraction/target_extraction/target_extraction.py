from typing import List

from generated_client import ExtractedTarget, TargetExtractionSpec
from mimic_iii_explorer_client.client.target_api_client import TargetApiClient
from mimic_iii_explorer_client.extraction import logger


def extract_target(target_extraction_spec: TargetExtractionSpec) -> List[ExtractedTarget]:
    """Retrieve target values for specified objective from the MIMIC-III database.

    :param target_extraction_spec: request body for target extraction
    :return: root entity ids and encoded computed target values
    """
    logger.info('Requesting mimic-iii-explorer to extract the target values for the specified ids')
    return TargetApiClient().target(target_extraction_spec)
