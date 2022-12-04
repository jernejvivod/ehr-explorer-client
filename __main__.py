import argparse

from mimic_iii_explorer_client import Tasks, TargetSpec, TextOutputFormat
from mimic_iii_explorer_client import logger
from mimic_iii_explorer_client.data_saving import save
from mimic_iii_explorer_client.extraction.clinical_text_extraction.clinical_text_extraction import extract_clinical_text
from mimic_iii_explorer_client.extraction.id_retrieval.id_retrieval import retrieve_ids
from mimic_iii_explorer_client.extraction.target_extraction.target_extraction import extract_target
from mimic_iii_explorer_client.utils.cli_args_types import dir_path


def main(**kwargs):
    # CLINICAL TEXT EXTRACTION
    if kwargs['task'] == Tasks.EXTRACT_CLINICAL_TEXT.value:
        logger.info('Running clinical text extraction task')

        # extract clinical texts, extract target values, save in specified output format
        retrieved_ids = retrieve_ids(kwargs['root_entity_name'], kwargs['id_property_name'], kwargs['filter_specs'])
        extracted_texts = extract_clinical_text(
            kwargs['clinical_text_entity_name'],
            kwargs['text_property_name'],
            kwargs['clinical_text_entity_id_property_name'],
            kwargs['date_time_properties_names'],
            kwargs['root_entity_name'],
            kwargs['id_property_name'],
            retrieved_ids,
            kwargs['first_minutes'],
            kwargs['limit_ids']
        )
        extracted_target = extract_target(kwargs['target'], [e.root_entity_id for e in extracted_texts])
        save.save_clinical_text(extracted_texts, extracted_target, kwargs['output_format'], kwargs['output_dir'], preprocessing_steps=None)
    else:
        raise NotImplementedError('Task {0} not implemented'.format(kwargs['task']))


if __name__ == '__main__':
    # parse arguments
    parser = argparse.ArgumentParser(prog='mimic-iii-analysis')
    subparsers = parser.add_subparsers(required=True, dest='task', help='Data processing task to run')

    # CLINICAL TEXT EXTRACTION
    extract_clinical_text_parser = subparsers.add_parser(Tasks.EXTRACT_CLINICAL_TEXT.value)
    extract_clinical_text_parser.add_argument('--target', type=str, default=TargetSpec.PATIENT_DIED_DURING_ADMISSION.value,
                                              choices=[v.value for v in TargetSpec], help='Target extraction specification')
    extract_clinical_text_parser.add_argument('--root-entity-name', type=str, default='AdmissionsEntity', help='Root entity name')
    extract_clinical_text_parser.add_argument('--clinical-text-entity-name', type=str, default='NoteEventsEntity', help='Clinical text entity name')
    extract_clinical_text_parser.add_argument('--text-property-name', type=str, default='text', help='Clinical text entity text property name')
    extract_clinical_text_parser.add_argument('--clinical-text-entity-id-property-name', type=str, default='rowId', help='Clinical text entity ID property name')
    extract_clinical_text_parser.add_argument('--date-time-properties-names', nargs="*", type=str, default=['charttime', 'chartdate'], help='Clinical text entity ID property name')
    extract_clinical_text_parser.add_argument('--id-property-name', type=str, default='hadmId', help='Root entity id property name')
    extract_clinical_text_parser.add_argument('--filter-specs', nargs='+', help='Entity filters to apply')
    extract_clinical_text_parser.add_argument('--first-minutes', type=int, help='Limit texts to the texts no more than the specified number of minutes from the initial timestamp')
    extract_clinical_text_parser.add_argument('--limit-ids', default=1.0, help='Number or percentage of root entity idss to consider')
    extract_clinical_text_parser.add_argument('--output-format', type=str, default=TextOutputFormat.FAST_TEXT.value,
                                              choices=[v.value for v in TextOutputFormat], help='Output format')
    extract_clinical_text_parser.add_argument('--output-dir', type=dir_path, default='.', help='Directory in which to store the outputs')

    args = parser.parse_args()
    main(**vars(args))
