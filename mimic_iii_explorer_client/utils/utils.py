import random
from typing import List, Union

from mimic_iii_explorer_client.utils import logger


def limit_ids(ids: List[str], keep: Union[float, int] = 1.0):
    """Get a random sample of the elements in the specified list. The size of the sample is either the specified number of elements to keep
    or the specified decimal fraction of the elements in the original list.

    :param ids: list of elements from which to sample
    :param keep: how many elements to sample (either the number or a decimal fraction)
    :return: random sample of specified size
    """
    try:
        keep = float(keep)
    except ValueError:
        raise ValueError('Invalid type for argument \'portion_keep\' (can be either int or float)')

    if keep.is_integer():
        keep = int(keep)
        if keep < 0:
            raise ValueError('Value of argument \'portion_keep\' must be positive')
        if keep > len(ids):
            raise ValueError('Value of argument \'portion_keep\' must be less than {0}'.format(len(ids)))
        logger.info('Limiting ids to a random sample of {0} ids'.format(keep))
        return random.sample(ids, keep)
    else:
        if keep < 0.0 or keep > 1.0:
            raise ValueError('Value of argument \'portion_keep\' must be between 0.0 and 1.0')
        lim = round(len(ids) * keep)
        logger.info('Limiting ids to a random sample of {0} ids ({1})'.format(lim, keep))
        return random.sample(ids, lim)
