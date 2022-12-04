from typing import List

from generated_client import ExtractedTarget, TargetExtractionSpec
from mimic_iii_explorer_client import TargetSpec
from mimic_iii_explorer_client.client.target_api_client import TargetApiClient
from mimic_iii_explorer_client.extraction import logger
from mimic_iii_explorer_client.mimic_iii_explorer_client.model.target_extraction_spec import TargetTypeEnum


def extract_target(target_spec: str, ids: List[object]) -> List[ExtractedTarget]:
    """Retrieve target values for specified objective from the MIMIC-III database.

    :param target_spec: objective specification
    :param ids: ids for objective root entity
    :return: root entity ids and extracted target value
    """

    # initialize client
    client = TargetApiClient()

    # initialize TargetExtractionSpecDto instance
    if target_spec == TargetSpec.PATIENT_DIED_DURING_ADMISSION.value:
        target_type = TargetTypeEnum.PATIENT_DIED_DURING_ADMISSION.value
    else:
        raise NotImplementedError('Value {0} of argument target_spec not supported'.format(target_spec))
    target_extraction_spec = TargetExtractionSpec(target_type=target_type, ids=ids)

    logger.info('Requesting mimic-iii-explorer to extract the target values for the specified ids')
    return client.target(target_extraction_spec)
