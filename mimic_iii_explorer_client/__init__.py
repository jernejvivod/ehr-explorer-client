import logging
from enum import Enum

# module logger

logging.basicConfig()
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


class Tasks(Enum):
    EXTRACT_CLINICAL_TEXT = 'extract-clinical-text'


class TargetSpec(Enum):
    PATIENT_DIED_DURING_ADMISSION = 'patient-died-during-admission'


class TextOutputFormat(Enum):
    FAST_TEXT = 'fast-text'


CONFIG_PATH = 'config/config'  # configuration file path (relative to the top-level package root directory
CONFIG_MEXPLORER_CORE_SECTION = 'mimic-iii-explorer'
CONFIG_MEXPLORER_CORE_URL_KEY = 'core-api-url'
CONFIG_MEXPLORER_CORE_ID_RETRIEVAL_PATH_KEY = 'id-retrieval-path'
CONFIG_MEXPLORER_CORE_CLINICAL_TEXT_EXTRACTION_PATH_KEY = 'clinical-text-extraction-path'
CONFIG_MEXPLORER_CORE_TARGET_EXTRACTION_PATH_KEY = 'target-extraction-path'
