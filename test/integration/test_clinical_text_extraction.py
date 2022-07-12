import http
import unittest

from mimic_iii_explorer_client.errors.client_errors import ClientException
from mimic_iii_explorer_client.mimic_iii_explorer_client.client import Client
from mimic_iii_explorer_client.mimic_iii_explorer_client.model.clinical_text_config import ClinicalTextConfig, RootEntitiesSpec, DataRangeSpec


class TestClinicalTextExtraction(unittest.TestCase):
    """Integration tests for clinical text extraction"""

    def test_basic_clinical_text_extraction(self):
        root_entities_spec = RootEntitiesSpec(
            "AdmissionsEntity",
            "hadmId",
            [100001, 100006]
        )

        data_range_spec = DataRangeSpec(
            1440
        )

        clinical_text_config = ClinicalTextConfig(
            root_entities_spec,
            data_range_spec
        )

        client = Client()
        res = client.extract_clinical_text(clinical_text_config)
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
            root_entities_spec,
            None
        )

        client = Client()
        with self.assertRaises(ClientException) as context:
            client.extract_clinical_text(clinical_text_config)

        self.assertEqual(http.HTTPStatus.BAD_REQUEST, context.exception.status)

    def test_extraction_batches(self):

        root_entities_spec = RootEntitiesSpec(
            "AdmissionsEntity",
            "hadmId",
            [
                100001,
                100003,
                100006,
                100007,
                100009,
                100010,
                100011,
                100012,
                100014,
                100016,
            ]
        )

        data_range_spec = DataRangeSpec(
            1440
        )

        clinical_text_config = ClinicalTextConfig(
            root_entities_spec,
            data_range_spec
        )

        client = Client()
        res_single_batch = client.extract_clinical_text(clinical_text_config)
        res_batched = client.extract_clinical_text(clinical_text_config, 5)

        self.assertEqual(len(res_single_batch), len(res_batched))
