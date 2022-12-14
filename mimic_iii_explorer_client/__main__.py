import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), "client/gen"))

import argparse  # noqa: E402

from mimic_iii_explorer_client import Tasks, TargetSpec, TextOutputFormat  # noqa: E402
from mimic_iii_explorer_client import logger  # noqa: E402
from mimic_iii_explorer_client.data_saving import save  # noqa: E402
from mimic_iii_explorer_client.extraction.clinical_text_extraction.clinical_text_extraction import extract_clinical_text  # noqa: E402
from mimic_iii_explorer_client.extraction.id_retrieval.id_retrieval import retrieve_ids  # noqa: E402
from mimic_iii_explorer_client.extraction.target_extraction.target_extraction import extract_target  # noqa: E402
from mimic_iii_explorer_client.request_spec_parsing.parsing import parse_request_spec_clinical_text, parse_request_spec_ids, parse_request_spec_target  # noqa: E402
from mimic_iii_explorer_client.utils.cli_args_types import dir_path  # noqa: E402
from mimic_iii_explorer_client.utils.utils import limit_ids  # noqa: E402


def main():
    # parse arguments
    parser = argparse.ArgumentParser(prog='mimic-iii-analysis')
    subparsers = parser.add_subparsers(required=True, dest='task', help='Data processing task to run')

    # CLINICAL TEXT EXTRACTION
    clinical_text_extraction_spec_parser = subparsers.add_parser(Tasks.EXTRACT_CLINICAL_TEXT.value)
    clinical_text_extraction_spec_parser.add_argument('--spec-path', type=str, required=True)
    clinical_text_extraction_spec_parser.add_argument('--target', type=str, default=TargetSpec.PATIENT_DIED_DURING_ADMISSION.value,
                                                      choices=[v.value for v in TargetSpec], help='Target extraction specification')
    clinical_text_extraction_spec_parser.add_argument('--limit-ids', default=1.0, help='Number or percentage of root entity idss to consider')
    clinical_text_extraction_spec_parser.add_argument('--output-format', type=str, default=TextOutputFormat.FAST_TEXT.value,
                                                      choices=[v.value for v in TextOutputFormat], help='Output format')
    clinical_text_extraction_spec_parser.add_argument('--output-dir', type=dir_path, default='.', help='Directory in which to store the outputs')

    args = vars(parser.parse_args())

    # CLINICAL TEXT EXTRACTION
    if args['task'] == Tasks.EXTRACT_CLINICAL_TEXT.value:
        logger.info('Running clinical text extraction task')

        # extract ids
        id_retrieval_spec = parse_request_spec_ids(args['ids_spec_path'])
        retrieved_ids = retrieve_ids(id_retrieval_spec)

        # limit ids
        ids_limitd = limit_ids(retrieved_ids, args['limit_ids'])

        # extract clinical text
        clinical_text_config = parse_request_spec_clinical_text(args['clinical_text_spec_path'], ids_limitd)
        extracted_texts = extract_clinical_text(clinical_text_config)

        # extract target values
        target_extraction_spec = parse_request_spec_target(args['target_spec_path'], ids_limitd)
        extracted_target = extract_target(target_extraction_spec)

        # pre-process and save clinical text
        save.save_clinical_text(extracted_texts, extracted_target, args['output_format'], args['output_dir'], preprocessing_steps=None)
    else:
        raise NotImplementedError('Task {0} not implemented'.format(args['task']))


if __name__ == '__main__':
    main()