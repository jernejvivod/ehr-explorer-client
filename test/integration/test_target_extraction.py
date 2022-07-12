import http
import unittest

from mimic_iii_explorer_client.errors.client_errors import ClientException
from mimic_iii_explorer_client.mimic_iii_explorer_client.client import Client
from mimic_iii_explorer_client.mimic_iii_explorer_client.model.target_extraction_result import ExtractedTargetDto
from mimic_iii_explorer_client.mimic_iii_explorer_client.model.target_extraction_spec import TargetExtractionSpecDto, TargetTypeEnum


class TestTargetExtraction(unittest.TestCase):
    """Integration tests for target extraction"""

    def test_basic_target_extraction_patient_died_during_admission(self):
        id1 = '100001'
        id2 = '100053'

        target_extraction_spec = TargetExtractionSpecDto(
            TargetTypeEnum.PATIENT_DIED_DURING_ADMISSION,
            [id1, id2]
        )

        client = Client()
        res = client.extract_target(target_extraction_spec)
        self.assertEqual(2, len(res))
        self.assertTrue(ExtractedTargetDto(int(id1), 0) in res)
        self.assertTrue(ExtractedTargetDto(int(id2), 1) in res)

    def test_target_extraction_with_invalid_target_spec(self):
        target_extraction_spec = TargetExtractionSpecDto(
            TargetTypeEnum.PATIENT_DIED_DURING_ADMISSION,
            ['wrong']
        )

        client = Client()

        with self.assertRaises(ClientException) as context:
            client.extract_target(target_extraction_spec)

        self.assertEqual(http.HTTPStatus.BAD_REQUEST, context.exception.status)
