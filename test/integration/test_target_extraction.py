import unittest

from generated_client import TargetExtractionSpec, ExtractedTarget
from mimic_iii_explorer_client.client.target_api_client import TargetApiClient
from mimic_iii_explorer_client.mimic_iii_explorer_client.model.target_extraction_spec import TargetTypeEnum


class TestTargetExtraction(unittest.TestCase):
    """Integration tests for target extraction"""

    def test_basic_target_extraction_patient_died_during_admission(self):
        id1 = 100001
        id2 = 100053

        target_extraction_spec = TargetExtractionSpec(
            target_type=TargetTypeEnum.PATIENT_DIED_DURING_ADMISSION.value,
            ids=[id1, id2]
        )

        client = TargetApiClient()

        res = client.target(target_extraction_spec)

        self.assertEqual(2, len(res))
        self.assertTrue(ExtractedTarget(int(id1), 0) in res)
        self.assertTrue(ExtractedTarget(int(id2), 1) in res)

    def test_target_extraction_with_invalid_target_spec(self):
        target_extraction_spec = TargetExtractionSpec(
            target_type=TargetTypeEnum.PATIENT_DIED_DURING_ADMISSION.value,
            ids=[-1]
        )

        client = TargetApiClient()

        self.assertEqual(0, len(client.target(target_extraction_spec)))
