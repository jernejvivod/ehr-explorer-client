import random
from typing import List, Union

from mimic_iii_explorer_client.utils import logger


def limit_ids(ids: List[str], portion_keep: Union[float, int] = 1.0):
    try:
        portion_keep = float(portion_keep)
    except ValueError:
        raise ValueError('Invalid type for argument \'portion_keep\' (can be either int or float)')

    if portion_keep.is_integer():
        portion_keep = int(portion_keep)
        if portion_keep < 0:
            raise ValueError('Value of argument \'portion_keep\' must be positive')
        if portion_keep > len(ids):
            raise ValueError('Value of argument \'portion_keep\' must be less than {0}'.format(len(ids)))
        logger.info('Limiting ids to a random sample of {0} ids'.format(portion_keep))
        return random.sample(ids, portion_keep)
    else:
        if portion_keep < 0.0 or portion_keep > 1.0:
            raise ValueError('Value of argument \'portion_keep\' must be between 0.0 and 1.0')
        lim = round(len(ids) * portion_keep)
        logger.info('Limiting ids to a random sample of {0} ids ({1})'.format(lim, portion_keep))
        return random.sample(ids, lim)
