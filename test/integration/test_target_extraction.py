import os
import sys

# NOTE: this line should be before any imports from the 'generated_client' package
sys.path.append(os.path.join(os.path.dirname(__file__), "../../ehr_explorer_client/client/gen"))

import unittest  # noqa: E402

from generated_client.models.extracted_target import ExtractedTarget  # noqa: E402
from generated_client.models.target_extraction_spec import TargetExtractionSpec  # noqa: E402
from ehr_explorer_client.client.target_api_client import TargetApiClient  # noqa: E402


class TestTargetExtraction(unittest.TestCase):
    """Integration tests for target extraction"""

    def test_basic_target_extraction_patient_died_during_admission(self):
        id1 = 100001
        id2 = 100053

        target_extraction_spec = TargetExtractionSpec(
            target_type="PATIENT_DIED_DURING_ADMISSION",
            ids=[id1, id2]
        )

        client = TargetApiClient()

        res = client.target(target_extraction_spec)

        self.assertEqual(2, len(res))
        self.assertTrue(ExtractedTarget(root_entity_id=int(id1), target_entity_id=int(id1), target_value=0) in res)
        self.assertTrue(ExtractedTarget(root_entity_id=int(id2), target_entity_id=int(id2), target_value=1) in res)

    def test_target_extraction_with_invalid_target_spec(self):
        target_extraction_spec = TargetExtractionSpec(
            target_type="PATIENT_DIED_DURING_ADMISSION",
            ids=[-1]
        )

        client = TargetApiClient()

        self.assertEqual(0, len(client.target(target_extraction_spec)))
