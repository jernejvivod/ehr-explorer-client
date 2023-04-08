import generated_client
from generated_client.api import target_api
from generated_client.models.target_extraction_spec import TargetExtractionSpec
from ehr_explorer_client.client import logger
from ehr_explorer_client.client.abstract_api_client import AbstractApiClient


class TargetApiClient(AbstractApiClient):
    def target(self, target_extraction_spec: TargetExtractionSpec):
        """Retrieve target values.

        :param target_extraction_spec: request body (target extraction retrieval parameters)
        :return: root entity ids and extracted targets (DTO)
        """

        logger.info('Retrieving target values')

        with generated_client.ApiClient(self.client_config) as api_client:
            api_instance = target_api.TargetApi(api_client)
            return api_instance.target_extraction(target_extraction_spec)
