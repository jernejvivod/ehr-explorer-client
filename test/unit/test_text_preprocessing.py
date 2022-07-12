import unittest

from mimic_iii_explorer_client.text_preprocessing import text_preprocessing


class TestTextPreprocessing(unittest.TestCase):
    """Unit tests for text pre-processing"""

    def setUp(self):
        self.text = "These are Just Simple Words For the Tests"

    def test_no_steps(self):
        res = text_preprocessing.preprocess(self.text, steps=[], output_tokens=False)
        self.assertEqual(self.text, res)
        res_tokens = text_preprocessing.preprocess(self.text, steps=[], output_tokens=True)
        self.assertEqual(self.text.split(), res_tokens)

    def test_lowercase(self):
        res = text_preprocessing.preprocess(self.text, steps=['lower-case'], output_tokens=False)
        self.assertEqual(self.text.lower(), res)
        res_tokens = text_preprocessing.preprocess(self.text, steps=['lower-case'], output_tokens=True)
        self.assertEqual(self.text.lower().split(), res_tokens)

    def test_remove_stop_words(self):
        res = text_preprocessing.preprocess(self.text, steps=['remove-stop-words'], output_tokens=False)
        res_tokens = text_preprocessing.preprocess(self.text, steps=['remove-stop-words'], output_tokens=True)

        expected = "Simple Words Tests"

        self.assertEqual(expected, res)
        self.assertEqual(expected.split(), res_tokens)

    def test_lemmatize(self):
        res = text_preprocessing.preprocess(self.text, steps=['lemmatize'], output_tokens=False)
        res_tokens = text_preprocessing.preprocess(self.text, steps=['lemmatize'], output_tokens=True)

        expected = "these are just simple word for the test"

        self.assertEqual(expected, res)
        self.assertEqual(expected.split(), res_tokens)

    def test_filter_len(self):
        res = text_preprocessing.preprocess(self.text, steps=['filter-len'], output_tokens=False, token_len_lim=4)
        res_tokens = text_preprocessing.preprocess(self.text, steps=['filter-len'], output_tokens=True, token_len_lim=4)

        expected = "These Just Simple Words Tests"

        self.assertEqual(expected, res)
        self.assertEqual(expected.split(), res_tokens)

    def test_all(self):
        res = text_preprocessing.preprocess(self.text, steps=None, output_tokens=False, token_len_lim=4)
        res_with_all_specified = text_preprocessing.preprocess(self.text, steps=['lower-case', 'remove-stop-words', 'lemmatize', 'filter-len'],
                                                               output_tokens=False, token_len_lim=4)
        res_tokens = text_preprocessing.preprocess(self.text, steps=None, output_tokens=True, token_len_lim=4)

        expected = "simple word test"

        self.assertEqual(expected, res)
        self.assertEqual(expected, res_with_all_specified)
        self.assertEqual(expected.split(), res_tokens)
