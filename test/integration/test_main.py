import os
import sys

# NOTE: this line should be before any imports from the 'generated_client' package
sys.path.append(os.path.join(os.path.dirname(__file__), "../../ehr_explorer_client/client/gen"))

import glob  # noqa: E402
import os  # noqa: E402
import unittest  # noqa: E402

from ehr_explorer_client.__main__ import main  # noqa: E402


class TestMain(unittest.TestCase):

    @staticmethod
    def __get_rel_path(rel_path):
        return os.path.join(os.path.dirname(__file__), rel_path)

    def test_main_extract_clinical_text(self):
        argv = [
            __file__,
            'extract-clinical-text',
            '--ids-spec-path', self.__get_rel_path('test-spec/ids_spec.json'),
            '--limit-ids', '0.01',
            '--clinical-text-spec-path', self.__get_rel_path('test-spec/clinical_text_spec.json'),
            '--target-spec-path', self.__get_rel_path('test-spec/target_spec.json'),
            '--output-dir', os.path.dirname(__file__)
        ]
        main(argv)

        file_path = glob.glob(self.__get_rel_path('*.txt'))[0]
        with open(file_path, 'r') as f:
            lines = f.readlines()

        self.assertGreater(len(lines), 0)

        os.remove(file_path)

    def test_main_extract_clinical_text_tt_split(self):
        argv = [
            __file__,
            'extract-clinical-text',
            '--ids-spec-path', self.__get_rel_path('test-spec/ids_spec.json'),
            '--limit-ids', '0.01',
            '--test-size', '0.2',
            '--clinical-text-spec-path', self.__get_rel_path('test-spec/clinical_text_spec.json'),
            '--target-spec-path', self.__get_rel_path('test-spec/target_spec.json'),
            '--output-dir', os.path.dirname(__file__)
        ]
        main(argv)

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
        argv = [
            __file__,
            'extract-target-statistics',
            '--ids-spec-path', self.__get_rel_path('test-spec/ids_spec.json'),
            '--target-spec-path', self.__get_rel_path('test-spec/target_spec.json'),
            '--output-dir', os.path.dirname(__file__)
        ]
        main(argv)

        file_path = glob.glob(self.__get_rel_path('*.txt'))[0]
        with open(file_path, 'r') as f:
            lines = f.readlines()
            self.assertGreater(len(lines), 0)

        os.remove(file_path)

    def test_main_wordification(self):
        argv = [
            __file__,
            'compute-wordification',
            '--ids-spec-path', self.__get_rel_path('test-spec/wordification_ids_spec.json'),
            '--wordification-config-path', self.__get_rel_path('test-spec/wordification_config.json'),
            '--target-spec-path', self.__get_rel_path('test-spec/wordification_target_spec.json'),
            '--output-dir', os.path.dirname(__file__)
        ]
        main(argv)

        file_path = glob.glob(self.__get_rel_path('*.txt'))[0]
        with open(file_path, 'r') as f:
            lines = f.readlines()
            self.assertGreater(len(lines), 0)

        os.remove(file_path)

    def test_main_extract_clinical_text_tt_split_seeded(self):
        argv = [
            __file__,
            '--seed', '1',
            'extract-clinical-text',
            '--ids-spec-path', self.__get_rel_path('test-spec/ids_spec.json'),
            '--limit-ids', '0.01',
            '--test-size', '0.2',
            '--clinical-text-spec-path', self.__get_rel_path('test-spec/clinical_text_spec.json'),
            '--target-spec-path', self.__get_rel_path('test-spec/target_spec.json'),
            '--output-dir', os.path.dirname(__file__)
        ]
        main(argv)
        main(argv)

        file_paths_train = glob.glob(self.__get_rel_path('*-train.txt'))
        file_paths_test = glob.glob(self.__get_rel_path('*-test.txt'))

        self._assert_files_equal(file_paths_train[0], file_paths_train[1])
        self._assert_files_equal(file_paths_test[0], file_paths_test[1])

        for file_path in file_paths_train + file_paths_test:
            os.remove(file_path)

    def _assert_files_equal(self, file_path1: str, file_path2: str) -> None:
        with open(file_path1, 'r') as f1, open(file_path2, 'r') as f2:
            self.assertTrue(f1.readlines() == f2.readlines())
