import os
import re
import time
from collections import Counter
from typing import List, Collection, Optional

from generated_client import ClinicalTextResult, ExtractedTarget, WordificationResult
from ehr_explorer_client import TextOutputFormat
from ehr_explorer_client.text_preprocessing.text_preprocessing import preprocess


def save_clinical_text(extracted_texts: List[ClinicalTextResult],
                       extracted_target: List[ExtractedTarget],
                       output_format: str,
                       output_dir: str,
                       output_file_suffix: Optional[str],
                       preprocessing_steps: Collection[str] = None) -> None:
    """Save extracted clinical texts in specified format.

    :param extracted_texts: extracted clinical texts (DTOs)
    :param extracted_target: extracted target values (DTOs)
    :param output_format: output format specifier
    :param output_dir: output directory
    :param output_file_suffix: suffix to add to the output filename
    :param preprocessing_steps: preprocessing steps (use all if set to None)
    """
    if output_format == TextOutputFormat.FAST_TEXT.value:
        _RE_COMBINE_WHITESPACE = re.compile(r"\s+")
        with open(os.path.join(output_dir, 'data-' + time.strftime("%Y%m%d-%H%M%S") + (output_file_suffix if output_file_suffix else "") + '.txt'), 'w') as f:
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


def save_target_statistics(target_value_counts: Counter, output_dir: str):
    """Save extracted target value conts.

    :param target_value_counts: extracted target value counts
    :param output_dir: output directory
    """
    with open(os.path.join(output_dir, 'stats-' + time.strftime("%Y%m%d-%H%M%S") + '.txt'), 'w') as f:
        for (k, v) in target_value_counts.items():
            f.write("{0}: {1}\n".format(k, v))


def save_wordification_results(wordification_result: List[WordificationResult],
                               extracted_target: List[ExtractedTarget],
                               output_format: str,
                               output_dir: str,
                               output_file_suffix: Optional[str]) -> None:
    """Save extracted Wordification results.

    :param wordification_result: computed Wordification results
    :param extracted_target: extracted target values (used for matching Wordification results to target entities)
    :param output_format: output format specifier
    :param output_dir: output directory
    :param output_file_suffix: suffix to add to the output filenaem
    """
    if output_format == TextOutputFormat.FAST_TEXT.value:
        with open(os.path.join(output_dir, 'data-' + time.strftime("%Y%m%d-%H%M%S") + (output_file_suffix if output_file_suffix else "") + '.txt'), 'w') as f:
            for res in wordification_result:
                target_val = [t for t in extracted_target if t.root_entity_id == res.root_entity_id and t.date_time_limit == res.time_lim]

                if len(target_val) == 0:
                    raise ValueError('Target value for root entity with id={0} not found'.format(res.root_entity_id))

                f.write(' '.join(res.words))
                f.write(' ')
                f.write('__label__{0}\n'.format(target_val[0].target_value))
    else:
        raise ValueError('Format \'{0}\' not supported'.format(output_format))