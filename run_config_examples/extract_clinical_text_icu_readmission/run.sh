#!/bin/bash

# define the path to the script
script_path=$(dirname "$0")

# define paths to the configuration files
ids_spec_path="$script_path/config/ids_spec.json"
clinical_text_spec_path="$script_path/config/clinical_text_spec.json"
target_spec_path="$script_path/config/target_spec.json"

# define the output directory
output_dir="$script_path/results"

# run the command
python3 "$script_path/../../mimic_iii_explorer_client" \
    extract-clinical-text \
    --ids-spec-path "$ids_spec_path" \
    --clinical-text-spec-path "$clinical_text_spec_path" \
    --target-spec-path "$target_spec_path" \
    --limit-ids 0.01 \
    --output-dir "$output_dir"
