import configparser
import os
from abc import ABC

import generated_client
from mimic_iii_explorer_client import CONFIG_MEXPLORER_CORE_SECTION, CONFIG_MEXPLORER_CORE_URL_KEY, CONFIG_PATH


class AbstractApiClient(ABC):
    def __init__(self, config_path: str = None):
        """Initialize client with API paths from configuration file.

        :param: config_path: path to configuration file (use default path if None)
        """

        # parse server paths
        config = configparser.ConfigParser()
        config.read(os.path.join(os.path.dirname(__file__), '../..', CONFIG_PATH if config_path is None else config_path))

        # base API path
        self.client_config = generated_client.Configuration(
            host=config[CONFIG_MEXPLORER_CORE_SECTION][CONFIG_MEXPLORER_CORE_URL_KEY],
        )
