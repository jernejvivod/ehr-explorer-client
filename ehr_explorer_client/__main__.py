import os
import random
import sys

# NOTE: this line should be before any imports from the 'generated_client' package
sys.path.append(os.path.join(os.path.dirname(__file__), "client/gen"))

import collections  # noqa: E402
from typing import List, Optional  # noqa: E402
from sklearn.model_selection import train_test_split  # noqa: E402
from ehr_explorer_client.propositionalization.wordification.wordification import compute_wordification  # noqa: E402
from generated_client import RootEntityAndTimeLimit  # noqa: E402
import argparse  # noqa: E402

from ehr_explorer_client import Tasks, TextOutputFormat  # noqa: E402
from ehr_explorer_client import logger  # noqa: E402
from ehr_explorer_client.data_saving import save  # noqa: E402
from ehr_explorer_client.extraction.clinical_text_extraction.clinical_text_extraction import extract_clinical_text  # noqa: E402
from ehr_explorer_client.extraction.id_retrieval.id_retrieval import retrieve_ids  # noqa: E402
from ehr_explorer_client.extraction.target_extraction.target_extraction import extract_target  # noqa: E402
from ehr_explorer_client.request_spec_parsing.parsing import parse_request_spec_clinical_text, parse_request_spec_ids, parse_request_spec_target, parse_request_spec_wordification  # noqa: E402
from ehr_explorer_client.utils.cli_args_types import dir_path, test_size  # noqa: E402
from ehr_explorer_client.utils.utils import limit_ids  # noqa: E402


def main(argv=None):
    if argv is None:
        argv = sys.argv

    # parse arguments
    parser = argparse.ArgumentParser(prog='mimic-iii-analysis')
    _add_common_parser_args(parser)
    subparsers = parser.add_subparsers(required=True, dest='task', help='Data processing task to run')

    # add subparsers for tasks
    _add_subparser_for_clinical_text_extraction(subparsers)
    _add_subparser_for_wordification(subparsers)
    _add_subparser_for_target_statistics_extraction(subparsers)

    # run task
    _run_task(vars(parser.parse_args(argv[1:])))


def _run_task(parsed_args):
    random.seed(parsed_args['seed'])

    # CLINICAL TEXT EXTRACTION
    if parsed_args['task'] == Tasks.EXTRACT_CLINICAL_TEXT.value:
        logger.info('Running clinical text extraction task.')
        _run_clinical_text_extraction_task(parsed_args)
    # WORDIFICATION
    elif parsed_args['task'] == Tasks.COMPUTE_WORDIFICATION.value:
        logger.info('Running compute Wordification task.')
        _run_compute_wordification_task(parsed_args)
    # TARGET STATISTICS EXTRACTION
    elif parsed_args['task'] == Tasks.EXTRACT_TARGET_STATISTICS.value:
        logger.info('Running target statistics extraction task.')
        _run_target_statistics_extraction_task(parsed_args)
    else:
        raise NotImplementedError('Task {0} not implemented'.format(parsed_args['task']))


def _add_common_parser_args(parser):
    parser.add_argument('--seed', type=int, default=None, help='Seed with which to initialize random number generation')


def _add_subparser_for_target_statistics_extraction(subparsers):
    clinical_text_extraction_spec_parser = subparsers.add_parser(Tasks.EXTRACT_TARGET_STATISTICS.value)
    clinical_text_extraction_spec_parser.add_argument('--ids-spec-path', type=str, required=True)
    clinical_text_extraction_spec_parser.add_argument('--target-spec-path', type=str, required=True)
    clinical_text_extraction_spec_parser.add_argument('--output-dir', type=dir_path, default='.', help='Directory in which to store the outputs')


def _add_subparser_for_wordification(subparsers):
    wordification_spec_parser = subparsers.add_parser(Tasks.COMPUTE_WORDIFICATION.value)
    wordification_spec_parser.add_argument('--ids-spec-path', type=str, required=True)
    wordification_spec_parser.add_argument('--wordification-config-path', type=str, required=True)
    wordification_spec_parser.add_argument('--target-spec-path', type=str, required=True)
    wordification_spec_parser.add_argument('--limit-ids', default=1.0, help='Number or percentage of root entity idss to consider')
    wordification_spec_parser.add_argument('--test-size', type=test_size, help='Test set size (no train-test split is performed if not specified)')
    wordification_spec_parser.add_argument('--output-format', type=str, default=TextOutputFormat.FAST_TEXT.value,
                                           choices=[v.value for v in TextOutputFormat], help='Output format')
    wordification_spec_parser.add_argument('--output-dir', type=dir_path, default='.', help='Directory in which to store the outputs')


def _add_subparser_for_clinical_text_extraction(subparsers):
    clinical_text_extraction_spec_parser = subparsers.add_parser(Tasks.EXTRACT_CLINICAL_TEXT.value)
    clinical_text_extraction_spec_parser.add_argument('--ids-spec-path', type=str, required=True)
    clinical_text_extraction_spec_parser.add_argument('--clinical-text-spec-path', type=str, required=True)
    clinical_text_extraction_spec_parser.add_argument('--target-spec-path', type=str, required=True)
    clinical_text_extraction_spec_parser.add_argument('--limit-ids', default=1.0, help='Number or percentage of root entity idss to consider')
    clinical_text_extraction_spec_parser.add_argument('--test-size', type=test_size, help='Test set size (no train-test split is performed if not specified)')
    clinical_text_extraction_spec_parser.add_argument('--output-format', type=str, default=TextOutputFormat.FAST_TEXT.value,
                                                      choices=[v.value for v in TextOutputFormat], help='Output format')
    clinical_text_extraction_spec_parser.add_argument('--output-dir', type=dir_path, default='.', help='Directory in which to store the outputs')


def _run_clinical_text_extraction_task(parsed_args: dict):
    """Run clinical text extraction task with parameters specified by the parsed arguments."""

    # extract ids
    id_retrieval_spec = parse_request_spec_ids(parsed_args['ids_spec_path'])
    retrieved_ids = retrieve_ids(id_retrieval_spec)

    # limit ids
    ids_limited = limit_ids(retrieved_ids, parsed_args['limit_ids'])

    if parsed_args['test_size'] is not None:
        ids_limited_train, ids_limited_test = train_test_split(ids_limited, test_size=parsed_args['test_size'], random_state=42)
        _get_target_and_text(parsed_args, ids_limited_train, "-train")
        _get_target_and_text(parsed_args, ids_limited_test, "-test")
    else:
        _get_target_and_text(parsed_args, ids_limited, None)


def _run_target_statistics_extraction_task(parsed_args: dict):
    """Run statistics extraction task with parameters specified by the parsed arguments."""

    # extract ids
    id_retrieval_spec = parse_request_spec_ids(parsed_args['ids_spec_path'])
    retrieved_ids = retrieve_ids(id_retrieval_spec)

    # extract target values
    target_extraction_spec = parse_request_spec_target(parsed_args['target_spec_path'], retrieved_ids)
    extracted_target = extract_target(target_extraction_spec)

    # save target value counts
    target_value_counts = collections.Counter(map(lambda x: x.target_value, extracted_target))
    save.save_target_statistics(target_value_counts, parsed_args['output_dir'])


def _run_compute_wordification_task(parsed_args: dict):
    """Run compute Wordification task with parameters specified by the parsed arguments."""

    # extract ids
    id_retrieval_spec = parse_request_spec_ids(parsed_args['ids_spec_path'])
    retrieved_ids = retrieve_ids(id_retrieval_spec)

    # limit ids
    ids_limited = limit_ids(retrieved_ids, parsed_args['limit_ids'])

    if parsed_args['test_size'] is not None:
        ids_limited_train, ids_limited_test = train_test_split(ids_limited, test_size=parsed_args['test_size'], random_state=42)
        _get_target_and_wordification_results(parsed_args, ids_limited_train, "-train")
        _get_target_and_wordification_results(parsed_args, ids_limited_test, "-test")
    else:
        _get_target_and_wordification_results(parsed_args, ids_limited, None)


def _get_target_and_text(parsed_args: dict, ids: List[str], output_file_suffix: Optional[str]):
    """Extract target values and clinical text, perform text pre-processing and save results.

    :param parsed_args: parameters for the computatations
    :param ids: entity IDs
    :param output_file_suffix: suffix to add to the resulting file name.
    """
    # extract target values
    target_extraction_spec = parse_request_spec_target(parsed_args['target_spec_path'], ids)
    extracted_target = extract_target(target_extraction_spec)

    # extract clinical text
    clinical_text_config = parse_request_spec_clinical_text(parsed_args['clinical_text_spec_path'], list(map(lambda x: x.root_entity_id, extracted_target)))
    extracted_texts = extract_clinical_text(clinical_text_config)

    # pre-process and save clinical text
    save.save_clinical_text(extracted_texts, extracted_target, parsed_args['output_format'], parsed_args['output_dir'], output_file_suffix, preprocessing_steps=None)


def _get_target_and_wordification_results(parsed_args: dict, ids: List[str], output_file_suffix: Optional[str]):
    """Extract target values, compute Wordification, and save results.

    :param parsed_args: parameters for the computatations
    :param ids: entity IDs
    :param output_file_suffix: suffix to add to the resulting file name.
    """

    # extract target values
    target_extraction_spec = parse_request_spec_target(parsed_args['target_spec_path'], ids)
    extracted_target = extract_target(target_extraction_spec)

    wordification_config = parse_request_spec_wordification(parsed_args['wordification_config_path'], ids)

    wordification_config.property_spec.root_entity_and_lime_limit = [
        RootEntityAndTimeLimit(root_entity_id=e.root_entity_id, time_lim=e.date_time_limit) for e in extracted_target
    ]

    wordification_results = compute_wordification(wordification_config)
    save.save_wordification_results(wordification_results, extracted_target, parsed_args['output_format'], parsed_args['output_dir'], output_file_suffix)


if __name__ == '__main__':
    sys.exit(main(sys.argv))
