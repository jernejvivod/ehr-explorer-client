import generated_client
from generated_client.api import clinical_text_api
from generated_client.models.clinical_text_config import ClinicalTextConfig
from ehr_explorer_client.client import logger
from ehr_explorer_client.client.abstract_api_client import AbstractApiClient


class ClinicalTextApiClient(AbstractApiClient):
    def clinical_text(self, clinical_text_config: ClinicalTextConfig):
        """Retrieve extracted clinical texts.

        :param clinical_text_config: request body (text extraction retrieval parameters)
        :return: root entity ids and extracted clinical texts (DTO)
        """

        logger.info('Retrieving clinical text')

        with generated_client.ApiClient(self.client_config) as api_client:
            api_instance = clinical_text_api.ClinicalTextApi(api_client)
            return api_instance.clinical_text(clinical_text_config)
