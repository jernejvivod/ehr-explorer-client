import os
import re
import time
from typing import List, Collection

from generated_client import ClinicalTextResult, ExtractedTarget
from mimic_iii_explorer_client import TextOutputFormat
from mimic_iii_explorer_client.text_preprocessing.text_preprocessing import preprocess


def save_clinical_text(extracted_texts: List[ClinicalTextResult],
                       extracted_target: List[ExtractedTarget],
                       output_format: str,
                       output_dir: str,
                       preprocessing_steps: Collection[str] = None) -> None:
    """Save extracted clinical texts in specified format.

    :param extracted_texts: extracted clinical texts (DTOs)
    :param extracted_target: extracted target values (DTOs)
    :param output_format: output format specifier
    :param output_dir: output directory
    :param preprocessing_steps: preprocessing steps (use all if set to None)
    """
    if output_format == TextOutputFormat.FAST_TEXT.value:
        _RE_COMBINE_WHITESPACE = re.compile(r"\s+")
        with open(os.path.join(output_dir, 'data-' + time.strftime("%Y%m%d-%H%M%S") + '.txt'), 'w') as f:
            for extracted_text in extracted_texts:
                # pre-process
                text = _RE_COMBINE_WHITESPACE.sub(' ', extracted_text.text.replace('\n', ' ')).strip()
                text = preprocess(text, preprocessing_steps)

                # write to fast-text format
                target_val = [t for t in extracted_target if t.root_entity_id == extracted_text.root_entity_id]
                if len(target_val) == 0:
                    raise ValueError('Target value for root entity with id={0} not found'.format(extracted_text.root_entity_id))
                f.write(text)
                f.write(' ')
                f.write('__label__{0}\n'.format(target_val[0].target_value))
    else:
        raise ValueError('Format \'{0}\' not supported'.format(output_format))
