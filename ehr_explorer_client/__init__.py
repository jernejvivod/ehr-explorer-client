import logging
from enum import Enum

__version__ = "0.1.0"

# module logger

logging.basicConfig()
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


class Tasks(Enum):
    EXTRACT_CLINICAL_TEXT = 'extract-clinical-text'
    EXTRACT_TARGET_STATISTICS = 'extract-target-statistics'
    COMPUTE_WORDIFICATION = 'compute-wordification'


class TargetSpec(Enum):
    PATIENT_DIED_DURING_ADMISSION = 'patient-died-during-admission'


class TextOutputFormat(Enum):
    FAST_TEXT = 'fast-text'


CONFIG_PATH = 'config/config'  # configuration file path (relative to the top-level package root directory
CONFIG_EHR_EXPLORER_CORE_SECTION = 'ehr-explorer'
CONFIG_EHR_EXPLORER_CORE_URL_KEY = 'core-api-url'
CONFIG_EHR_EXPLORER_MIMIC_III_TARGET_EXTRACTION_URL_KEY = 'mimic-iii-target-extraction-api-url'
