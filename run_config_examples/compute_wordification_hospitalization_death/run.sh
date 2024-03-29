#!/bin/bash

# define the path to the script
script_path=$(dirname "$0")

# define paths to the configuration files
ids_spec_path="$script_path/config/ids_spec.json"
wordification_config_path="$script_path/config/wordification_config.json"
target_spec_path="$script_path/config/target_spec.json"

# define the output directory
output_dir="$script_path/results"

# run the command
args=("$script_path/../../ehr_explorer_client"
  --seed 42
  compute-wordification
  --ids-spec-path "$ids_spec_path"
  --wordification-config-path "$wordification_config_path"
  --target-spec-path "$target_spec_path"
  --limit-ids 0.5
  --undersampling 1.0
  --test-size 0.2
  --output-dir "$output_dir"
)

echo "${args[@]}"

python3 "${args[@]}"
