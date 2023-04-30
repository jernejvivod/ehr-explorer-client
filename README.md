# EHR Explorer Client

EHR Explorer Client (`ehr-explorer-client`) is a tool that facilitates working with the [EHR Explorer]() API by providing a command-line
interface allowing users to easily
perform common tasks related to querying EHR datasets (primarily the MIMIC-III dataset) through the use of EHR Explorer.

### Also see [EHR Explorer](https://github.com/jernejvivod/ehr-explorer), [EHR Explorer API](https://github.com/jernejvivod/ehr-explorer-api), and [Classification With Embeddings](https://github.com/jernejvivod/classification-with-embeddings).

## Quickstart

This section explains the steps needed to install the package.

## Installing EHR Explorer Client

The EHR Explorer Client package (`ehr-explorer-client`) can be installed following the next steps.

1. Clone the repository:

```bash
git clone https://github.com/jernejvivod/ehr-explorer-client.git
```

2. Ensure that you have Python 3 installed. Install the package requirements with:

```bash
python -m pip install -r requirements.txt
```

This will install all the required dependencies.

3. Install the package with:

```bash
python -m pip install .
```

4. Verify that the package is installed correctly by running the following:

```bash
python -c "import ehr_explorer_client; print(ehr_explorer_client.__version__)"
```

If the installation was successful, this command will print the version of the package that was installed.

The `generate_client.sh` script in the root project directory can be used to generate a client for EHR Explorer using
the OpenAPI specification included in the project as a Git submodule (https://github.com/jernejvivod/ehr-explorer-api).
The generated client is included in the repository so this step is only needed if you modify the API specification.

## Commands and Tasks

EHR Explorer Client is capable of interacting with EHR Explorer to perform three main tasks: clinical text extraction,
Wordification data extraction, and target statistics extraction. It combines the functionality provided by the
EHR Explorer's API to perform the data querying in such a way as to provide data that can be used to perform
machine learning tasks and evaluations of methodologies.

### Clinical Text Extraction

We specify the clinical text extraction task by providing the `extract-clinical-text` argument.

Running `ehr_explorer_client extract-clinical-text --help` prints out the available options:

```
usage: mimic-iii-analysis extract-clinical-text [-h] --ids-spec-path IDS_SPEC_PATH --clinical-text-spec-path CLINICAL_TEXT_SPEC_PATH --target-spec-path TARGET_SPEC_PATH [--limit-ids LIMIT_IDS] [--test-size TEST_SIZE] [--output-format {fast-text}] [--output-dir OUTPUT_DIR]

options:
-h, --help            show this help message and exit
--ids-spec-path IDS_SPEC_PATH
--clinical-text-spec-path CLINICAL_TEXT_SPEC_PATH
--target-spec-path TARGET_SPEC_PATH
--limit-ids LIMIT_IDS
Number or percentage of root entity idss to consider
--test-size TEST_SIZE
Test set size (no train-test split is performed if not specified)
--output-format {fast-text}
Output format
--output-dir OUTPUT_DIR
Directory in which to store the outputs
```

The `--ids-spec-path` option is used to specify the location of a file containing JSON specifying the request body for
retrieving the IDs of the root entities (records in the root table) for which we want to extract the clinical text.

See [EHR Explorer API](https://github.com/jernejvivod/ehr-explorer-api) and 
[EHR Explorer](https://github.com/jernejvivod/ehr-explorer) for the OpenAPI specification describing the structure of
the JSON and the description of the values.

The `--clinical-text-spec-path` option is used to specify the location of a file containing JSON specifying the request
body for retrieving the clinical text. We do not need to specify the root entity IDs as the ones retrieved by the
request described above will be used.

The `--target-spec-path` option is used to specify the location of a file containing JSON specifying the request body
for retrieving the class values of target entities. We don't need to specify the root entity IDs as the ones retrieved
in the ID retrieval step will be used.

This will result in EHR Explorer Client retrieving the IDs as specified, using the IDs to extract the clinical text
as specified, extracting the class values for the target entities as specified, and finally combining the results
to obtain the clinical text for a patient up to the event represented by the target entity with the extracted class
value for the event. This can then directly be used in machine learning or data mining tasks.

The `--limit-ids` option allows us to limit the retrieved IDs to only include a specified portion or number of the IDs.
To for example include only 80% of the ids, set the associated value to 0.8. To include for example only 100 IDs,
set the associated value to 1000. Random sampling is used to choose the IDs that will be included.

The `--test-size` option allows us to specify the size of the test set. As before, the value should be a float between
0.0 and 1.0 or an int representing the absolute number of the samples to include in the test set. The train-test
split is not performed if this value is not specified.

The `--output-format` option allows u sto specify the output format. Currently, only the FastText format is supported
and is used as the default if this option is not specified.

The `--output-dir` option allows us to specify the path to the directory in which to store the results.
Defaults to the current directory if not specified.

TODO show examples of results.

### Wordification

We specify the clinical text extraction task by providing the `compute-wordification` argument.

Running `ehr_explorer_client compute-wordification --help` prints out the available options:

```
usage: mimic-iii-analysis compute-wordification [-h] --ids-spec-path IDS_SPEC_PATH --wordification-config-path WORDIFICATION_CONFIG_PATH --target-spec-path TARGET_SPEC_PATH [--limit-ids LIMIT_IDS] [--test-size TEST_SIZE] [--output-format {fast-text}] [--output-dir OUTPUT_DIR]

options:
  -h, --help            show this help message and exit
  --ids-spec-path IDS_SPEC_PATH
  --wordification-config-path WORDIFICATION_CONFIG_PATH
  --target-spec-path TARGET_SPEC_PATH
  --limit-ids LIMIT_IDS
                        Number or percentage of root entity idss to consider
  --test-size TEST_SIZE
                        Test set size (no train-test split is performed if not specified)
  --output-format {fast-text}
                        Output format
  --output-dir OUTPUT_DIR
                        Directory in which to store the outputs
```

The options already discussed in the previous section behave exactly the same when computing wordification.

The `--wordification-config-path` option is used to specify the location of a file containing JSON specifying the
request body for computing wordification. We do not need to specify the root entity IDs as the ones retrieved by the
ID retrieval step will be used.

TODO show examples of results.

### Target Statistics Extraction

We specify the target statistics extraction task by providing the `extract-target-statistics` argument.

Running `ehr_explorer_client extract-target-statistics --help` prints out the available options:

```
usage: mimic-iii-analysis extract-target-statistics [-h] --ids-spec-path IDS_SPEC_PATH --target-spec-path TARGET_SPEC_PATH [--output-dir OUTPUT_DIR]

options:
  -h, --help            show this help message and exit
  --ids-spec-path IDS_SPEC_PATH
  --target-spec-path TARGET_SPEC_PATH
  --output-dir OUTPUT_DIR
                        Directory in which to store the outputs
```

The options behave exactly the same as described in the sections for the other tasks.

TODO show examples of results.

## Using Pre-Defined Workflows

The `run_conig_examples` folder contains some pre-defined workflows that can be used to extract data. It contains
directories containing shell scripts as well as JSON files for the argument values.

Running the `run.sh` shell scripts for a particular task performs that task using the argument values specified in the
`config` directories. You can modify the scripts and the files containing JSON values to fit your needs.

The results are stored in the `results` directory in the directory of the task we are running.
