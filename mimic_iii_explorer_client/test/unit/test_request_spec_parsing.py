import os
import sys

# NOTE: this line should be before any imports from the 'generated_client' package
sys.path.append(os.path.join(os.path.dirname(__file__), "../../client/gen"))

import json  # noqa: E402
import os  # noqa: E402
import unittest  # noqa: E402

from mimic_iii_explorer_client.request_spec_parsing.parsing import (
    parse_request_spec_ids,
    parse_request_spec_target,
    parse_request_spec_clinical_text,
    parse_request_spec_wordification
)  # noqa: E402


class TestRequestSpecParsing(unittest.TestCase):
    def test_parse_request_spec_ids(self):
        spec_file_path = './spec.json'
        expected_entity_name = 'AdmisionsEntity'
        expected_id_property = 'hadmId'
        expected_filter_specs = [
            {
                'foreign_key_path': ['A', 'B'],
                'property_name': 'a',
                'comparator': 'EQUAL',
                'property_val': 'test_val'
            },
            {
                'foreign_key_path': ['A', 'C'],
                'property_name': 'b',
                'comparator': 'MORE',
                'property_val': 25
            },
        ]

        with open(spec_file_path, 'w') as f:
            json.dump({
                'entity_name': expected_entity_name,
                'id_property': expected_id_property,
                'filter_specs': expected_filter_specs,
            }, f)

        spec = parse_request_spec_ids(spec_file_path)
        assert spec.entity_name == expected_entity_name
        assert spec.id_property == expected_id_property
        assert list(map(lambda x: x.to_dict(), spec.filter_specs)) == expected_filter_specs

        os.remove(spec_file_path)

    def test_parse_request_spec_target(self):
        spec_file_path = './spec.json'
        expected_target_type = 'PATIENT_DIED_DURING_ADMISSION'
        expected_ids = [1, 2, 3]

        with open(spec_file_path, 'w') as f:
            json.dump({
                'target_type': expected_target_type,
                'ids': expected_ids,
            }, f)

        spec = parse_request_spec_target(spec_file_path)
        assert spec.target_type == expected_target_type
        assert spec.ids == expected_ids

        os.remove(spec_file_path)

    def test_parse_request_spec_clinical_text(self):
        spec_file_path = './spec.json'
        expected_foreign_key_path = 'MY_ENTITY'
        expected_text_property_name = 'text'
        expected_clinical_text_entity_id_property_name = 'id'
        expected_clinical_text_date_time_properties_names = ['timestamp']
        expected_root_entities_spec = {
            'root_entity': 'AdmissionsEntity',
            'id_property': 'hadmId',
            'ids': [1, 2, 3]
        }
        expected_clinical_text_extraction_duration_spec = {
            'first_minutes': 10
        }

        with open(spec_file_path, 'w') as f:
            json.dump({
                'foreign_key_path': expected_foreign_key_path,
                'text_property_name': expected_text_property_name,
                'clinical_text_entity_id_property_name': expected_clinical_text_entity_id_property_name,
                'clinical_text_date_time_properties_names': expected_clinical_text_date_time_properties_names,
                'root_entities_spec': expected_root_entities_spec,
                'clinical_text_extraction_duration_spec': expected_clinical_text_extraction_duration_spec
            }, f)

        spec = parse_request_spec_clinical_text(spec_file_path)
        assert spec.foreign_key_path == expected_foreign_key_path
        assert spec.text_property_name == expected_text_property_name
        assert spec.clinical_text_entity_id_property_name == expected_clinical_text_entity_id_property_name
        assert spec.clinical_text_date_time_properties_names == expected_clinical_text_date_time_properties_names
        assert spec.root_entities_spec.to_dict() == expected_root_entities_spec
        assert spec.clinical_text_extraction_duration_spec.to_dict() == expected_clinical_text_extraction_duration_spec

        os.remove(spec_file_path)

    def test_parse_request_spec_wordification(self):
        spec_file_path = './spec.json'

        expected_root_entities_spec = {
            'root_entity': 'PatientsEntity',
            'id_property': 'subject_id',
            'ids': [1, 2, 3]
        }

        expected_property_spec = {
            'entries': [
                {
                    'entity': 'PatientsEntity',
                    'properties': ['gender'],
                    'property_for_limit': None,
                    'composite_property_spec_entries': None
                },
                {
                    'entity': 'IcuStaysEntity',
                    'properties': ['dbSource'],
                    'property_for_limit': 'outTime',
                    'composite_property_spec_entries': [
                        {
                            'property_on_this_entity': 'inTime',
                            'property_on_other_entity': 'dob',
                            'foreign_key_path': ['IcuStaysEntity', 'PatientsEntity'],
                            'composite_property_name': 'ageAtAdmission',
                            'combiner': 'DATE_DIFF'
                        }
                    ]
                }
            ],
            'root_entity_and_lime_limit': [
                {
                    'root_entity_id': 1,
                    'time_lim': '2023-02-08T11:04:30.123386566',
                },
                {
                    'root_entity_id': 2,
                    'time_lim': '2023-02-07T11:04:30.123386566',
                },
                {
                    'root_entity_id': 3,
                    'time_lim': '2023-02-06T11:04:30.123386566',
                }
            ]
        }

        expected_composite_columns_spec = {
            'entries': [
                {
                    'foreign_key_path1': ['PatientsEntity'],
                    'property1': 'dob',
                    'foreign_key_path2': ['PatientsEntity', 'IcuStaysEntity'],
                    'property2': 'inTime',
                    'composite_name': 'name',
                    'combiner': 'DATE_DIFF'
                }
            ]
        }

        expected_value_transformation_spec = {
            'entries': [
                {
                    'entity': 'IcuStaysEntity',
                    '_property': 'inTime',
                    'transform': {
                        'kind': 'ROUNDING',
                        'date_diff_round_type': 'TEN_YEARS',
                        'rounding_multiple': None
                    }
                }
            ]
        }

        expected_concatenation_spec = {
            'concatenation_scheme': 'ONE'
        }

        with open(spec_file_path, 'w') as f:
            json.dump({
                'root_entities_spec': expected_root_entities_spec,
                'property_spec': expected_property_spec,
                'composite_columns_spec': expected_composite_columns_spec,
                'value_transformation_spec': expected_value_transformation_spec,
                'concatenation_spec': expected_concatenation_spec,
            }, f)

        spec = parse_request_spec_wordification(spec_file_path)
        assert spec.root_entities_spec.to_dict() == expected_root_entities_spec
        assert spec.property_spec.to_dict() == expected_property_spec
        assert spec.composite_columns_spec.to_dict() == expected_composite_columns_spec
        assert spec.value_transformation_spec.to_dict() == expected_value_transformation_spec
        assert spec.concatenation_spec.to_dict() == expected_concatenation_spec

        os.remove(spec_file_path)
