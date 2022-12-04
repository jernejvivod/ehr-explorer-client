import json
import os
import unittest

from mimic_iii_explorer_client.request_spec_parsing.parsing import parse_request_spec_ids, parse_request_spec_target, parse_request_spec_clinical_text


class TestRequestSpecParsing(unittest.TestCase):
    def test_parse_request_spec_ids(self):
        spec_file_path = './spec.json'
        expected_entity_name = 'AdmisionsEntity'
        expected_id_property = 'hadmId'
        expected_filter_specs = [
            {
                'entity_name': 'A',
                'property_name': 'a',
                'comparator': 'EQUAL',
                'property_val': 'test_val'
            },
            {
                'entity_name': 'B',
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
        expected_clinical_text_entity_name = 'MY_ENTITY'
        expected_text_property_name = 'text'
        expected_clinical_text_entity_id_property_name = 'id'
        expected_date_time_properties_names = ['timestamp']
        expected_root_entities_spec = {
            'root_entity': 'AdmissionsEntity',
            'id_property': 'hadmId',
            'ids': [1, 2, 3]
        }
        expected_data_range_spec = {
            'first_minutes': 10
        }

        with open(spec_file_path, 'w') as f:
            json.dump({
                'clinical_text_entity_name': expected_clinical_text_entity_name,
                'text_property_name': expected_text_property_name,
                'clinical_text_entity_id_property_name': expected_clinical_text_entity_id_property_name,
                'date_time_properties_names': expected_date_time_properties_names,
                'root_entities_spec': expected_root_entities_spec,
                'data_range_spec': expected_data_range_spec
            }, f)

        spec = parse_request_spec_clinical_text(spec_file_path)
        assert spec.clinical_text_entity_name == expected_clinical_text_entity_name
        assert spec.text_property_name == expected_text_property_name
        assert spec.clinical_text_entity_id_property_name == expected_clinical_text_entity_id_property_name
        assert spec.date_time_properties_names == expected_date_time_properties_names
        assert spec.root_entities_spec.to_dict() == expected_root_entities_spec
        assert spec.data_range_spec.to_dict() == expected_data_range_spec

        os.remove(spec_file_path)
