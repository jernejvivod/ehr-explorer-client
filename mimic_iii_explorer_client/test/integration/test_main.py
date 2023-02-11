import os
import sys

# NOTE: this line should be before any imports from the 'generated_client' package
sys.path.append(os.path.join(os.path.dirname(__file__), "../../client/gen"))

import glob  # noqa: E402
import os  # noqa: E402
import unittest  # noqa: E402

from mimic_iii_explorer_client.__main__ import main  # noqa: E402


class MyTestCase(unittest.TestCase):

    @staticmethod
    def __get_rel_path(rel_path):
        return os.path.join(os.path.dirname(__file__), rel_path)

    def test_main_extract_clinical_text(self):
        args = [
            'extract-clinical-text',
            '--ids-spec-path', self.__get_rel_path('test-spec/ids_spec.json'),
            '--limit-ids', '0.01',
            '--clinical-text-spec-path', self.__get_rel_path('test-spec/clinical_text_spec.json'),
            '--target-spec-path', self.__get_rel_path('test-spec/target_spec.json'),
            '--output-dir', os.path.dirname(__file__)
        ]
        main(args)

        file_path = glob.glob(self.__get_rel_path('*.txt'))[0]
        with open(file_path, 'r') as f:
            lines = f.readlines()

        self.assertGreater(len(lines), 0)

        os.remove(file_path)

    def test_main_extract_clinical_text_tt_split(self):
        args = [
            'extract-clinical-text',
            '--ids-spec-path', self.__get_rel_path('test-spec/ids_spec.json'),
            '--limit-ids', '0.01',
            '--test-size', '0.2',
            '--clinical-text-spec-path', self.__get_rel_path('test-spec/clinical_text_spec.json'),
            '--target-spec-path', self.__get_rel_path('test-spec/target_spec.json'),
            '--output-dir', os.path.dirname(__file__)
        ]
        main(args)

        file_path_train = glob.glob(self.__get_rel_path('*-train.txt'))[0]
        file_path_test = glob.glob(self.__get_rel_path('*-test.txt'))[0]
        with open(file_path_train, 'r') as f:
            lines = f.readlines()
            self.assertGreater(len(lines), 0)

        with open(file_path_test, 'r') as f:
            lines = f.readlines()
            self.assertGreater(len(lines), 0)

        os.remove(file_path_train)
        os.remove(file_path_test)

    def test_main_extract_target_statistics(self):
        args = [
            'extract-target-statistics',
            '--ids-spec-path', self.__get_rel_path('test-spec/ids_spec.json'),
            '--target-spec-path', self.__get_rel_path('test-spec/target_spec.json'),
            '--output-dir', os.path.dirname(__file__)
        ]
        main(args)

        file_path = glob.glob(self.__get_rel_path('*.txt'))[0]
        with open(file_path, 'r') as f:
            lines = f.readlines()
            self.assertGreater(len(lines), 0)

        os.remove(file_path)

    def test_main_wordification(self):
        args = [
            'compute-wordification',
            '--ids-spec-path', self.__get_rel_path('test-spec/wordification_ids_spec.json'),
            '--wordification-config-path', self.__get_rel_path('test-spec/wordification_config.json'),
            '--target-spec-path', self.__get_rel_path('test-spec/wordification_target_spec.json'),
            '--output-dir', os.path.dirname(__file__)
        ]
        main(args)

        file_path = glob.glob(self.__get_rel_path('*.txt'))[0]
        with open(file_path, 'r') as f:
            lines = f.readlines()
            self.assertGreater(len(lines), 0)

        os.remove(file_path)
