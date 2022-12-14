#!/bin/bash

PROJECT_DIR_PATH="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
GENERATOR_JAR_NAME="openapi-generator-cli-4.3.1.jar"

if [ ! -f "${PROJECT_DIR_PATH}/${GENERATOR_JAR_NAME}" ]; then
  wget https://repo1.maven.org/maven2/org/openapitools/openapi-generator-cli/4.3.1/"${GENERATOR_JAR_NAME}"
fi

chmod +x "${PROJECT_DIR_PATH}"/"${GENERATOR_JAR_NAME}"

"${PROJECT_DIR_PATH}"/"${GENERATOR_JAR_NAME}" generate -g python -i \
"${PROJECT_DIR_PATH}"/mimic_iii_explorer_client/client/mimic-iii-explorer-api/doc/rest-spec/v1/mexplorer-openapi.yaml -o \
"${PROJECT_DIR_PATH}"/mimic_iii_explorer_client/client/gen \
--additional-properties=generateSourceCodeOnly=true,packageName=generated_client

touch "${PROJECT_DIR_PATH}"/mimic_iii_explorer_client/client/gen/__init__.py