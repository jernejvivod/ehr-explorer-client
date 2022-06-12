import random
from typing import Sequence, Union, List

from mimic_iii_analysis.extraction import logger
from mimic_iii_analysis.mimic_iii_explorer_client.client import Client
from mimic_iii_analysis.mimic_iii_explorer_client.model.clinical_text_config import ClinicalTextConfig, RootEntitiesSpec, DataRangeSpec
from mimic_iii_analysis.mimic_iii_explorer_client.model.clinical_text_result import ClinicalTextResultDto


def extract_clinical_text(root_entity_name: str,
                          id_property: str,
                          ids: Sequence[str],
                          first_minutes: Union[int, None],
                          limit_ids: Union[float, int] = 1.0
                          ) -> List[ClinicalTextResultDto]:
    """Retrieve clinical texts from the MIMIC-III database.

    :param root_entity_name: root entity name
    :param id_property: id property of root entity
    :param ids: root entity ids
    :param first_minutes: number of texts to retrieve
    :param limit_ids: limit the number of root entities to use (either number of ratio)
    :return: root entity ids and concatenated extracted text for that root entity
    """

    # initialize client
    client = Client()

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
        RootEntitiesSpec(root_entity_name, id_property, ids_limited),
        None if first_minutes is None else DataRangeSpec(first_minutes)
    )
    logger.info('Requesting mimic-iii-explorer to extract the clinical texts')
    return client.extract_clinical_text(texts_req_body)
