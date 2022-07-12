import configparser
import os
from typing import List
from urllib.parse import urljoin

import requests

from mimic_iii_explorer_client import (
    CONFIG_PATH,
    CONFIG_MEXPLORER_CORE_SECTION,
    CONFIG_MEXPLORER_CORE_URL_KEY,
    CONFIG_MEXPLORER_CORE_ID_RETRIEVAL_PATH_KEY,
    CONFIG_MEXPLORER_CORE_CLINICAL_TEXT_EXTRACTION_PATH_KEY,
    CONFIG_MEXPLORER_CORE_TARGET_EXTRACTION_PATH_KEY
)
from mimic_iii_explorer_client.errors.client_errors import ClientException
from mimic_iii_explorer_client.mimic_iii_explorer_client import logger
from mimic_iii_explorer_client.mimic_iii_explorer_client.model.clinical_text_config import ClinicalTextConfig
from mimic_iii_explorer_client.mimic_iii_explorer_client.model.clinical_text_result import ClinicalTextResultDto
from mimic_iii_explorer_client.mimic_iii_explorer_client.model.id_retrieval_spec import IdRetrievalSpec
from mimic_iii_explorer_client.mimic_iii_explorer_client.model.target_extraction_result import ExtractedTargetDto
from mimic_iii_explorer_client.mimic_iii_explorer_client.model.target_extraction_spec import TargetExtractionSpecDto


class Client:
    """
    Client for interacting with MIMIC-III-Explorer (https://github.com/jernejvivod/mimic-iii-explorer).
    """

    def __init__(self, config_path: str = None):
        """Initialize client with API paths from configuration file.

        :param config_path: path to configuration file (use default path if None)
        """

        # parse server paths
        config = configparser.ConfigParser()
        config.read(os.path.join(os.path.dirname(__file__), '../..', CONFIG_PATH if config_path is None else config_path))

        # base API path
        self.core_url = config[CONFIG_MEXPLORER_CORE_SECTION][CONFIG_MEXPLORER_CORE_URL_KEY]

        # paths
        self._id_retrieval_path = config[CONFIG_MEXPLORER_CORE_SECTION][CONFIG_MEXPLORER_CORE_ID_RETRIEVAL_PATH_KEY]
        self._clinical_text_extraction_path = config[CONFIG_MEXPLORER_CORE_SECTION][CONFIG_MEXPLORER_CORE_CLINICAL_TEXT_EXTRACTION_PATH_KEY]
        self._target_extraction_path = config[CONFIG_MEXPLORER_CORE_SECTION][CONFIG_MEXPLORER_CORE_TARGET_EXTRACTION_PATH_KEY]

        # urls for making calls
        self.id_retrieval_url = urljoin(self.core_url, self._id_retrieval_path)
        self.clinical_text_extraction_url = urljoin(self.core_url, self._clinical_text_extraction_path)
        self.target_extraction_url = urljoin(self.core_url, self._target_extraction_path)

    def retrieve_ids(self, id_retrieval_spec: IdRetrievalSpec) -> List['str']:
        """Retrieve root entity ids.

        :param id_retrieval_spec: request body (id retrieval parameters)
        :return: retrieved ids
        """

        logger.info('Retrieving ids')
        res = requests.post(url=self.id_retrieval_url, data=id_retrieval_spec.to_json(), headers={"Content-Type": "application/json"})
        if res.ok:
            return res.json()
        else:
            raise ClientException(res.status_code, res.reason, self.id_retrieval_url)

    def extract_clinical_text(self, clinical_text_config: ClinicalTextConfig, batch_size: int = -1) -> List[ClinicalTextResultDto]:
        """Retrieve extracted clinical texts.

        :param clinical_text_config: request body (text extraction retrieval parameters)
        :param batch_size: batch size for IDs. Use single batch if batch_size equal to -1.
        :return: root entity ids and extracted clinical texts (DTO)
        """
        logger.info('Extracting clinical texts')
        return self._batched_clinical_text_extraction(clinical_text_config, batch_size if batch_size > 0 else len(clinical_text_config.root_entities_spec.ids))

    def extract_target(self, target_extraction_spec: TargetExtractionSpecDto) -> List[ExtractedTargetDto]:
        """Retrieve target values.

        :param target_extraction_spec: request body (target extraction retrieval parameters)
        :return: root entity ids and extracted targets (DTO)
        """

        logger.info('Extracting target values')
        res = requests.post(url=self.target_extraction_url, data=target_extraction_spec.to_json(), headers={"Content-Type": "application/json"})
        if res.ok:
            return [ExtractedTargetDto.from_dict(r) for r in res.json()]
        else:
            raise ClientException(res.status_code, res.reason, self.target_extraction_url)

    def _batched_clinical_text_extraction(self, clinical_text_config: ClinicalTextConfig, batch_size: int):
        """Retrieve extracted clinical texts in batches (auxiliary method).

        :param clinical_text_config: request body (text extraction retrieval parameters)
        :param batch_size: batch size for IDs. Use single batch if batch_size equal to -1.
        :return: root entity ids and extracted clinical texts (DTO)
        """

        ids_all = clinical_text_config.root_entities_spec.ids.copy()
        results = []
        for idx_start in range(0, len(ids_all), batch_size):
            batch_nxt = ids_all[idx_start:idx_start + batch_size]
            clinical_text_config.root_entities_spec.ids = batch_nxt  # set next batch IDs
            res = requests.post(url=self.clinical_text_extraction_url, data=clinical_text_config.to_json(), headers={"Content-Type": "application/json"})
            if res.ok:
                results += [ClinicalTextResultDto.from_dict(r) for r in res.json()]
            else:
                raise ClientException(res.status_code, res.reason, self.clinical_text_extraction_url)
        return results
