import os
import sys

from sklearn.model_selection import train_test_split

sys.path.append(os.path.join(os.path.dirname(__file__), "client/gen"))

import argparse  # noqa: E402

from mimic_iii_explorer_client import Tasks, TextOutputFormat  # noqa: E402
from mimic_iii_explorer_client import logger  # noqa: E402
from mimic_iii_explorer_client.data_saving import save  # noqa: E402
from mimic_iii_explorer_client.extraction.clinical_text_extraction.clinical_text_extraction import extract_clinical_text  # noqa: E402
from mimic_iii_explorer_client.extraction.id_retrieval.id_retrieval import retrieve_ids  # noqa: E402
from mimic_iii_explorer_client.extraction.target_extraction.target_extraction import extract_target  # noqa: E402
from mimic_iii_explorer_client.request_spec_parsing.parsing import parse_request_spec_clinical_text, parse_request_spec_ids, parse_request_spec_target  # noqa: E402
from mimic_iii_explorer_client.utils.cli_args_types import dir_path, train_size  # noqa: E402
from mimic_iii_explorer_client.utils.utils import limit_ids  # noqa: E402


def main(args):
    # parse arguments
    parser = argparse.ArgumentParser(prog='mimic-iii-analysis')
    subparsers = parser.add_subparsers(required=True, dest='task', help='Data processing task to run')

    # CLINICAL TEXT EXTRACTION
    clinical_text_extraction_spec_parser = subparsers.add_parser(Tasks.EXTRACT_CLINICAL_TEXT.value)
    clinical_text_extraction_spec_parser.add_argument('--ids-spec-path', type=str, required=True)
    clinical_text_extraction_spec_parser.add_argument('--clinical-text-spec-path', type=str, required=True)
    clinical_text_extraction_spec_parser.add_argument('--target-spec-path', type=str, required=True)
    clinical_text_extraction_spec_parser.add_argument('--limit-ids', default=1.0, help='Number or percentage of root entity idss to consider')
    clinical_text_extraction_spec_parser.add_argument('--test-size', type=train_size, help='Test set size (no train-test split is performed if not specified)')
    clinical_text_extraction_spec_parser.add_argument('--output-format', type=str, default=TextOutputFormat.FAST_TEXT.value,
                                                      choices=[v.value for v in TextOutputFormat], help='Output format')
    clinical_text_extraction_spec_parser.add_argument('--output-dir', type=dir_path, default='.', help='Directory in which to store the outputs')

    parsed_args = vars(parser.parse_args(args))

    # CLINICAL TEXT EXTRACTION
    if parsed_args['task'] == Tasks.EXTRACT_CLINICAL_TEXT.value:
        logger.info('Running clinical text extraction task')

        # extract ids
        id_retrieval_spec = parse_request_spec_ids(parsed_args['ids_spec_path'])
        retrieved_ids = retrieve_ids(id_retrieval_spec)

        # limit ids
        ids_limited = limit_ids(retrieved_ids, parsed_args['limit_ids'])

        def get_target_and_text(ids, output_file_suffix):
            # extract target values
            target_extraction_spec = parse_request_spec_target(parsed_args['target_spec_path'], ids)
            extracted_target = extract_target(target_extraction_spec)

            # extract clinical text
            clinical_text_config = parse_request_spec_clinical_text(parsed_args['clinical_text_spec_path'], list(map(lambda x: x.root_entity_id, extracted_target)))
            extracted_texts = extract_clinical_text(clinical_text_config)

            # pre-process and save clinical text
            save.save_clinical_text(extracted_texts, extracted_target, parsed_args['output_format'], parsed_args['output_dir'], output_file_suffix, preprocessing_steps=None)

        if parsed_args['test_size'] is not None:
            ids_limited_train, ids_limited_test = train_test_split(ids_limited, test_size=parsed_args['test_size'], random_state=42)
            get_target_and_text(ids_limited_train, "-train")
            get_target_and_text(ids_limited_test, "-test")
        else:
            get_target_and_text(ids_limited, None)

    else:
        raise NotImplementedError('Task {0} not implemented'.format(parsed_args['task']))


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
