#!/bin/bash

# define the path to the script
script_path=$(dirname "$0")

# define paths to the configuration files
ids_spec_path="$script_path/config/ids_spec.json"
target_spec_path="$script_path/config/target_spec_patient_died_during_admission.json"

# define the output directory
output_dir="$script_path/results"

# run the command
python3 "$script_path/../../mimic_iii_explorer_client" \
    extract-target-statistics \
    --ids-spec-path "$ids_spec_path" \
    --target-spec-path "$target_spec_path" \
    --output-dir "$output_dir"
