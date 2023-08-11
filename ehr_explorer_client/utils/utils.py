import random
from typing import List, Union

import numpy as np
from imblearn.under_sampling import RandomUnderSampler

from ehr_explorer_client.client.gen.generated_client.models.extracted_target import ExtractedTarget
from ehr_explorer_client.utils import logger


def limit_ids(ids: List[str], keep: Union[float, int] = 1.0):
    """Get a random sample of the elements in the specified list.
    The size of the sample is either the specified number of elements to keep
    or the specified decimal fraction of the elements in the original list.

    :param ids: list of elements from which to sample
    :param keep: how many elements to sample (either the number or a decimal fraction)
    :return: random sample of specified size
    """
    try:
        keep = float(keep)
    except ValueError:
        raise ValueError('Invalid type for argument \'portion_keep\' (can be either int or float)')

    if isinstance(keep, int):
        if keep < 0:
            raise ValueError('Value of argument \'portion_keep\' must be positive')
        if keep > len(ids):
            raise ValueError('Value of argument \'portion_keep\' must be less than {0}'.format(len(ids)))
        logger.info('Limiting ids to a random sample of {0} ids'.format(keep))
        return random.sample(ids, keep)
    elif isinstance(keep, float):
        if keep < 0.0 or keep > 1.0:
            raise ValueError('Value of argument \'portion_keep\' must be between 0.0 and 1.0')
        lim = round(len(ids) * keep)
        logger.info('Limiting ids to a random sample of {0} ids ({1})'.format(lim, keep))
        return random.sample(ids, lim)
    else:
        raise ValueError('Invalid type for argument \'portion_keep\' (can be either int or float)')


def undersample_extracted_target(extracted_target: List[ExtractedTarget], ratio: float):
    """Perform undersampling of examples based on target value.

    :param extracted_target: list of extracted target values
    :param ratio: target ratio of minority class to majority class
    """

    under_sampler = RandomUnderSampler(sampling_strategy=ratio, random_state=42)

    # need to provide nested indices
    idxs_resampled_nested, _ = under_sampler.fit_resample(
        [[idx] for idx in range(len(extracted_target))], [1 if e.target_value > 0 else 0 for e in extracted_target]
    )

    # unnest results, shuffle, and select results based on sampled indices
    idxs_resampled = [e[0] for e in idxs_resampled_nested]
    idxs_resampled_shuffled = [idxs_resampled[p] for p in np.random.permutation(len(idxs_resampled))]
    return [extracted_target[idx] for idx in idxs_resampled_shuffled]
