from setuptools import setup, find_packages

setup(
    name='mimic-iii-explorer-client',
    version='0.1.0',
    packages=find_packages(),
    url='https://github.com/jernejvivod/mimic-iii-explorer-client',
    license='MIT',
    author='Jernej Vivod',
    author_email='vivod.jernej@gmail.com',
    description='Client for the mimic-iii-explorer',
    entry_points={
        'console_scripts': [
            'my-script=mimic_iii_explorer_client.__main__:main',
        ]
    },
)
