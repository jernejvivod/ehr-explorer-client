import os
import sys

# NOTE: this line should be before any imports from the 'generated_client' package
sys.path.append(os.path.join(os.path.dirname(__file__), "../../client/gen"))

import collections  # noqa: E402
import glob  # noqa: E402
import os  # noqa: E402
import unittest  # noqa: E402
from datetime import datetime  # noqa: E402

from generated_client import ClinicalTextResult, ExtractedTarget, WordificationResult  # noqa: E402
from mimic_iii_explorer_client.data_saving import save  # noqa: E402


class TestSave(unittest.TestCase):
    """Unit tests for data saving"""

    def test_save_clinical_text_empty(self):
        save.save_clinical_text(
            [],
            [],
            'fast-text',
            '',
            None
        )

        # test saved file contents correct
        files = glob.glob('data*.txt')
        self.assertEqual(len(files), 1)
        saved_file_path = files[0]
        with open(saved_file_path, 'r') as f:
            self.assertEqual(len(f.readlines()), 0)

        os.remove(saved_file_path)

    def test_save_clinical_text_simple(self):
        clinical_text_result = ClinicalTextResult(1, 'this is a test')
        extracted_target = ExtractedTarget(
            root_entity_id=1,
            target_entity_id=2,
            target_value=0
        )

        save.save_clinical_text(
            [clinical_text_result],
            [extracted_target],
            'fast-text',
            '',
            None
        )

        # test saved file contents correct
        files = glob.glob('data*.txt')
        self.assertEqual(len(files), 1)
        saved_file_path = files[0]
        with open(saved_file_path, 'r') as f:
            lines = f.readlines()
            self.assertEqual(len(lines), 1)
            self.assertEqual('test __label__0\n', lines[0])

        os.remove(saved_file_path)

    def test_save_target_statistics_empty(self):
        target_value_counts = collections.Counter([1, 1, 1, 2, 3, 3, 3, 3, 3])
        save.save_target_statistics(
            target_value_counts,
            ''
        )

        # test saved file contents correct
        files = glob.glob('stats*.txt')
        self.assertEqual(len(files), 1)
        saved_file_path = files[0]
        with open(saved_file_path, 'r') as f:
            lines = f.readlines()
            self.assertEqual(len(lines), 3)
            lines_striped = [s.strip() for s in lines]
            self.assertTrue('1: 3' in lines_striped)
            self.assertTrue('2: 1' in lines_striped)
            self.assertTrue('3: 5' in lines_striped)

        os.remove(saved_file_path)

    def test_save_target_statistics_simple(self):
        wordification_results = [
            WordificationResult(
                root_entity_id=1,
                time_lim=datetime(2023, 1, 1, 12, 0, 0),
                words=['a', 'b', 'c']
            ),
            WordificationResult(
                root_entity_id=1,
                time_lim=datetime(2023, 2, 1, 13, 30, 30),
                words=['d', 'e', 'f']
            ),
            WordificationResult(
                root_entity_id=2,
                time_lim=datetime(2023, 3, 3, 17, 21, 45),
                words=['g', 'h', 'i', 'j']
            ),
        ]

        extracted_target = [
            ExtractedTarget(
                root_entity_id=1,
                target_entity_id=11,
                target_value=0,
                date_time_limit=datetime(2023, 1, 1, 12, 0, 0)
            ),
            ExtractedTarget(
                root_entity_id=1,
                target_entity_id=12,
                target_value=1,
                date_time_limit=datetime(2023, 2, 1, 13, 30, 30)
            ),
            ExtractedTarget(
                root_entity_id=2,
                target_entity_id=22,
                target_value=2,
                date_time_limit=datetime(2023, 3, 3, 17, 21, 45)
            ),
        ]

        save.save_wordification_results(
            wordification_results,
            extracted_target,
            'fast-text',
            '',
            None
        )

        # test saved file contents correct
        files = glob.glob('data*.txt')
        self.assertEqual(len(files), 1)
        saved_file_path = files[0]
        with open(saved_file_path, 'r') as f:
            lines = f.readlines()
            self.assertEqual(len(lines), 3)

            lines_striped = [s.strip() for s in lines]
            self.assertTrue('a b c __label__0' in lines_striped)
            self.assertTrue('d e f __label__1' in lines_striped)
            self.assertTrue('g h i j __label__2' in lines_striped)

        os.remove(saved_file_path)
