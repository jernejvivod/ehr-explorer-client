from ehr_explorer_client import CONFIG_EHR_EXPLORER_MIMIC_III_TARGET_EXTRACTION_URL_KEY
from ehr_explorer_client.client.abstract_api_client import AbstractApiClient


class AbstractTargetExtractionApiClient(AbstractApiClient):
    def get_config_url_key(self):
        return CONFIG_EHR_EXPLORER_MIMIC_III_TARGET_EXTRACTION_URL_KEY
