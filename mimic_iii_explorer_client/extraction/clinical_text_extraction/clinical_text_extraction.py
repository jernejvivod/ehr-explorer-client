import random
from typing import Sequence, Union, List

from generated_client import ClinicalTextResult, ClinicalTextConfig, RootEntitiesSpec, DataRangeSpec
from mimic_iii_explorer_client.client.clinical_text_api_client import ClinicalTextApiClient
from mimic_iii_explorer_client.extraction import logger


def extract_clinical_text(
        clinical_text_entity_name: str,
        text_property_name: str,
        clinical_text_entity_id_property_name: str,
        date_time_properties_names: List[str],
        root_entity_name: str,
        id_property: str,
        ids: Sequence[str],
        first_minutes: Union[int, None],
        limit_ids: Union[float, int] = 1.0
) -> List[ClinicalTextResult]:
    """Retrieve clinical texts from the MIMIC-III database.

    :param clinical_text_entity_name: name of clinical text entity
    :param text_property_name: property name of text property of clinical text entity
    :param clinical_text_entity_id_property_name: ID property name of clinical text entity
    :param date_time_properties_names: property names of date/time columns (in the order they should be considered)
    :param root_entity_name: root entity name
    :param id_property: id property of root entity
    :param ids: root entity ids
    :param first_minutes: number of texts to retrieve
    :param limit_ids: limit the number of root entities to use (either number of ratio)
    :return: root entity ids and concatenated extracted text for that root entity
    """

    # initialize client
    client = ClinicalTextApiClient()

    # limit ids (if applicable)
    try:
        limit_ids = float(limit_ids)
    except ValueError:
        raise ValueError('Invalid type for argument \'limit_ids\' (can be either int or float)')

    if limit_ids.is_integer():
        limit_ids = int(limit_ids)
        if limit_ids < 0:
            raise ValueError('Value of argument limit_ids must be positive')
        if limit_ids > len(ids):
            raise ValueError('Value of argument limit_ids must be less than {0}'.format(len(ids)))
        logger.info('Limiting ids to a random sample of {0} ids'.format(limit_ids))
        ids_limited = random.sample(ids, limit_ids)
    else:
        if limit_ids < 0.0 or limit_ids > 1.0:
            raise ValueError('Value of argument limit_ids must be between 0.0 and 1.0')
        lim = round(len(ids) * limit_ids)
        logger.info('Limiting ids to a random sample of {0} ids ({1})'.format(lim, limit_ids))
        ids_limited = random.sample(ids, lim)

    # extract clinical texts
    texts_req_body = ClinicalTextConfig(
        clinical_text_entity_name=clinical_text_entity_name,
        text_property_name=text_property_name,
        clinical_text_entity_id_property_name=clinical_text_entity_id_property_name,
        date_time_properties_names=date_time_properties_names,
        root_entities_spec=RootEntitiesSpec(root_entity=root_entity_name, id_property=id_property, ids=ids_limited),
        data_range_spec=None if first_minutes is None else DataRangeSpec(first_minutes)
    )
    logger.info('Requesting mimic-iii-explorer to extract the clinical texts')
    return client.clinical_text(texts_req_body)
