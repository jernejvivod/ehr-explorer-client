from enum import Enum
from typing import Collection, Sequence, List, Union

from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize


class PreprocessingSteps(Enum):
    LOWERCASE = 'lower-case'
    REMOVE_STOP_WORDS = 'remove-stop-words'
    LEMMATIZE = 'lemmatize'
    FILTER_LEN = 'filter-len'


_STOP_WORDS = set(stopwords.words('english'))
_LEMMATIZER = WordNetLemmatizer()


def preprocess(text: str, steps: Collection[str] = None, output_tokens=False, token_len_lim: int = 3) -> Union[str, List[str]]:
    """Preprocess text.

    :param text: text to preprocess
    :param steps: preprocessing steps (lower-case, remove-stop-words or lemmatize) to use (use all if set to None)
    :param output_tokens: output tokens if True and str otherwise
    :param token_len_lim: token length limit (if 'filter-len' preprocessing step specified)
    :return: preprocessed text as tokens or string
    """

    # if steps None, use all steps
    if steps is None:
        steps = {v.value for v in PreprocessingSteps}

    # tokenize
    tokens = list(filter(lambda x: len(x) > 0, [''.join([c for c in token if c.isalpha()]) for token in word_tokenize(text)]))

    # apply specified preprocessing steps
    if PreprocessingSteps.LOWERCASE.value in steps:
        tokens = lowercase(tokens)
    if PreprocessingSteps.REMOVE_STOP_WORDS.value in steps:
        tokens = remove_stop_words(tokens)
    if PreprocessingSteps.LEMMATIZE.value in steps:
        tokens = lemmatize(tokens)
    if PreprocessingSteps.FILTER_LEN.value in steps:
        tokens = filter_len(tokens, token_len_lim)

    if output_tokens:
        return tokens
    else:
        return ' '.join(tokens)


def lowercase(tokens: Sequence[str]) -> List[str]:
    """Transform tokenized text to lowercase.

    :param tokens: tokenized text
    :return: tokenized text in all lowercase
    """
    return [token.lower() for token in tokens]


def remove_stop_words(tokens: Sequence[str]) -> List[str]:
    """Remove stop words from tokenized text.

    :param tokens: tokenized text
    :return: tokenized text with stop words removed
    """
    return [token for token in tokens if token.lower() not in _STOP_WORDS]


def lemmatize(tokens: Sequence[str]) -> List[str]:
    """Perform lemmatization of tokenized text.

    :param tokens: tokenized text
    :return: lemmatized tokenized text
    """
    return [_LEMMATIZER.lemmatize(token.lower()) for token in tokens]


def filter_len(tokens: Sequence[str], len_lim: int) -> List[str]:
    """Keep only tokens equal or longer to specified length limit.

    :param tokens: tokenized text
    :param len_lim: token length limit
    :return: tokenized text with limited minimum token length
    """
    return [token for token in tokens if len(token) >= len_lim]
