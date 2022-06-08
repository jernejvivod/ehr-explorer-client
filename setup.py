from distutils.core import setup

setup(
    name='mimic-iii-analysis',
    version='0.1.0',
    packages=['mimic_iii_analysis', 'mimic_iii_analysis.mimic_iii_explorer_client'],
    url='https://github.com/jernejvivod/mimic-iii-analysis',
    license='',
    author='Jernej Vivod',
    author_email='vivod.jernej@gmail.com',
    description='Client for mimic-iii-explorer that provides additional data preprocessing and saving data for learning tasks'
)
