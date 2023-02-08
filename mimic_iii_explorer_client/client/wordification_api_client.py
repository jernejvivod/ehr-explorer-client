import generated_client
from generated_client import WordificationConfig
from generated_client.api import propositionalization_api
from mimic_iii_explorer_client.client.abstract_api_client import AbstractApiClient
from mimic_iii_explorer_client.propositionalization import logger


class PropositionalizationApiClient(AbstractApiClient):
    def wordification(self, wordification_config: WordificationConfig):
        """Retrieve extracted clinical texts.

        :param wordification_config: request body (Wordification computation parameters)
        :return: root entity ids, time limit for root entity and extracted words (DTO)
        """

        logger.info('Computing Wordification')

        with generated_client.ApiClient(self.client_config) as api_client:
            api_instance = propositionalization_api.PropositionalizationApi(api_client)
            return api_instance.wordification(wordification_config)
