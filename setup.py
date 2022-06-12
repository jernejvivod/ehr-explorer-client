from setuptools import setup

setup(
    name='mimic-iii-explorer-client',
    version='0.1.0',
    packages=['tests', 'tests.unit', 'tests.integration', 'mimic_iii_explorer_client', 'mimic_iii_explorer_client.utils', 'mimic_iii_explorer_client.errors', 'mimic_iii_explorer_client.extraction', 'mimic_iii_explorer_client.extraction.id_retrieval', 'mimic_iii_explorer_client.extraction.target_extraction', 'mimic_iii_explorer_client.extraction.clinical_text_extraction', 'mimic_iii_explorer_client.data_saving', 'mimic_iii_explorer_client.text_preprocessing', 'mimic_iii_explorer_client.mimic_iii_explorer_client', 'mimic_iii_explorer_client.mimic_iii_explorer_client.model'],
    url='https://github.com/jernejvivod/mimic-iii-explorer-client',
    license='MIT',
    author='Jernej Vivod',
    author_email='vivod.jernej@gmail.com',
    description='Client for the mimic-iii-explorer'
)
