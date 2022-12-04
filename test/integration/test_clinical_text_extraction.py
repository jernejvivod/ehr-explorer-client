import http
import unittest

from generated_client import RootEntitiesSpec, DataRangeSpec, ClinicalTextConfig, ApiException
from mimic_iii_explorer_client.client.clinical_text_api_client import ClinicalTextApiClient


class TestClinicalTextExtraction(unittest.TestCase):
    """Integration tests for clinical text extraction"""

    def test_basic_clinical_text_extraction(self):
        root_entities_spec = RootEntitiesSpec(
            root_entity="AdmissionsEntity",
            id_property="hadmId",
            ids=[100001, 100006]
        )

        data_range_spec = DataRangeSpec(
            first_minutes=1440
        )

        clinical_text_config = ClinicalTextConfig(
            clinical_text_entity_name="NoteEventsEntity",
            text_property_name="text",
            clinical_text_entity_id_property_name="rowId",
            date_time_properties_names=['charttime', 'chartdate'],
            root_entities_spec=root_entities_spec,
            data_range_spec=data_range_spec
        )

        client = ClinicalTextApiClient()
        res = client.clinical_text(clinical_text_config)
        self.assertEqual(2, len(res))
        self.assertTrue(len(res[0].text) > 0)
        self.assertTrue(len(res[1].text) > 0)

    def test_extraction_non_existing_root_entity(self):
        root_entities_spec = RootEntitiesSpec(
            "Wrong",
            "hadmId",
            [100001, 100006]
        )

        clinical_text_config = ClinicalTextConfig(
            clinical_text_entity_name="NoteEventsEntity",
            text_property_name="text",
            clinical_text_entity_id_property_name="rowId",
            root_entities_spec=root_entities_spec
        )

        client = ClinicalTextApiClient()
        with self.assertRaises(ApiException) as context:
            client.clinical_text(clinical_text_config)

        self.assertEqual(http.HTTPStatus.BAD_REQUEST, context.exception.status)
