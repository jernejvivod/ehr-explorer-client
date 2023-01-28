import http
import unittest

from generated_client import ApiException, ClinicalTextExtractionDurationSpec
from generated_client.models.clinical_text_config import ClinicalTextConfig
from generated_client.models.root_entities_spec import RootEntitiesSpec
from mimic_iii_explorer_client.client.clinical_text_api_client import ClinicalTextApiClient


class TestClinicalTextExtraction(unittest.TestCase):
    """Integration tests for clinical text extraction"""

    def test_basic_clinical_text_extraction(self):
        root_entities_spec = RootEntitiesSpec(
            root_entity="AdmissionsEntity",
            id_property="hadmId",
            ids=[100001, 100006]
        )

        clinical_text_extraction_duration_spec = ClinicalTextExtractionDurationSpec(
            first_minutes=1440
        )

        clinical_text_config = ClinicalTextConfig(
            foreign_key_path=["AdmissionsEntity", "NoteEventsEntity"],
            text_property_name="text",
            clinical_text_entity_id_property_name="rowId",
            clinical_text_date_time_properties_names=['chartTime', 'chartDate'],
            root_entities_spec=root_entities_spec,
            clinical_text_extraction_duration_spec=clinical_text_extraction_duration_spec
        )

        client = ClinicalTextApiClient()
        res = client.clinical_text(clinical_text_config)
        self.assertEqual(2, len(res))
        self.assertTrue(len(res[0].text) > 0)
        self.assertTrue(len(res[1].text) > 0)

    def test_extraction_non_existing_root_entity(self):
        root_entities_spec = RootEntitiesSpec(
            "AdmissionsEntity",
            "hadmId",
            [100001, 100006]
        )

        clinical_text_config = ClinicalTextConfig(
            foreign_key_path=["Wrong", "NoteEventsEntity"],
            text_property_name="text",
            clinical_text_entity_id_property_name="rowId",
            root_entities_spec=root_entities_spec
        )

        client = ClinicalTextApiClient()
        with self.assertRaises(ApiException) as context:
            client.clinical_text(clinical_text_config)

        self.assertEqual(http.HTTPStatus.BAD_REQUEST, context.exception.status)
