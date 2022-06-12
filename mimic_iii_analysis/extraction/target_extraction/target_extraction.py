from typing import List

from mimic_iii_analysis import TargetSpec
from mimic_iii_analysis.extraction import logger
from mimic_iii_analysis.mimic_iii_explorer_client.client import Client
from mimic_iii_analysis.mimic_iii_explorer_client.model.target_extraction_result import ExtractedTargetDto
from mimic_iii_analysis.mimic_iii_explorer_client.model.target_extraction_spec import TargetExtractionSpecDto, TargetTypeEnum


def extract_target(target_spec: str, ids: List[object]) -> List[ExtractedTargetDto]:
    """Retrieve target values for specified objective from the MIMIC-III database.

    :param target_spec: objective specification
    :param ids: ids for objective root entity
    :return: root entity ids and extracted target value
    """

    # initialize client
    client = Client()

    # initialize TargetExtractionSpecDto instance
    if target_spec == TargetSpec.PATIENT_DIED_DURING_ADMISSION.value:
        target_type = TargetTypeEnum.PATIENT_DIED_DURING_ADMISSION
    else:
        raise NotImplementedError('Value {0} of argument target_spec not supported'.format(target_spec))
    target_extraction_spec = TargetExtractionSpecDto(target_type, ids)

    logger.info('Requesting mimic-iii-explorer to extract the target values for the specified ids')
    return client.extract_target(target_extraction_spec)
