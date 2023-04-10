from ehr_explorer_client import CONFIG_EHR_EXPLORER_CORE_URL_KEY
from ehr_explorer_client.client.abstract_api_client import AbstractApiClient


class AbstractCoreApiClient(AbstractApiClient):
    def get_config_url_key(self):
        return CONFIG_EHR_EXPLORER_CORE_URL_KEY
