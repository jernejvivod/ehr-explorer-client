from setuptools import setup, find_packages

setup(
    name='ehr-explorer-client',
    version='0.1.0',
    packages=find_packages(),
    url='https://github.com/jernejvivod/ehr-explorer-client',
    license='MIT',
    author='Jernej Vivod',
    author_email='vivod.jernej@gmail.com',
    description='Client for the ehr-explorer',
    include_package_data=True,
    entry_points={
        'console_scripts': [
            'ehr_explorer_client=ehr_explorer_client.__main__:main',
        ]
    },
)
