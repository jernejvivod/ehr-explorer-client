from typing import List

import generated_client
from ehr_explorer_client.client import logger
from ehr_explorer_client.client.abstract_core_api_client import AbstractCoreApiClient
from generated_client.api import ids_api
from generated_client.models.id_retrieval_spec import IdRetrievalSpec


class IdsApiClient(AbstractCoreApiClient):
    def ids(self, id_retrieval_spec: IdRetrievalSpec) -> List['str']:
        """Retrieve root entity ids.

        :param id_retrieval_spec:
        :return:
        """

        logger.info('Retrieving root entity IDs')

        with generated_client.ApiClient(self.client_config) as api_client:
            api_instance = ids_api.IdsApi(api_client)
            return api_instance.ids(id_retrieval_spec)
