import json
from collections import defaultdict
from typing import List

from generated_client import IdRetrievalSpec, IdRetrievalFilterSpec, TargetExtractionSpec, ClinicalTextConfig, RootEntitiesSpec, ClinicalTextExtractionDurationSpec


class SpecParsingError(Exception):
    def __init__(self, key: str):
        self.key = key


def parse_request_spec_ids(spec_file_path: str) -> IdRetrievalSpec:
    with open(spec_file_path, 'r') as f:
        json_dict = to_defaultdict(json.load(f))
    return IdRetrievalSpec(
        entity_name=json_dict['entity_name'],
        id_property=json_dict['id_property'],
        filter_specs=[IdRetrievalFilterSpec(filt['foreign_key_path'], filt['property_name'], filt['comparator'], filt['property_val'])
                      for filt in (json_dict['filter_specs'] if 'filter_specs' in json_dict else [])],
    )


def parse_request_spec_target(spec_file_path: str, ids: List[str] = None) -> TargetExtractionSpec:
    with open(spec_file_path, 'r') as f:
        json_dict = to_defaultdict(json.load(f))
    return TargetExtractionSpec(
        target_type=json_dict['target_type'],
        ids=json_dict['ids'] if ids is None else ids,
    )


def parse_request_spec_clinical_text(spec_file_path: str, ids: List[str] = None) -> ClinicalTextConfig:
    with open(spec_file_path, 'r') as f:
        json_dict = to_defaultdict(json.load(f))
    return ClinicalTextConfig(
        foreign_key_path=json_dict['foreign_key_path'],
        text_property_name=json_dict['text_property_name'],
        clinical_text_entity_id_property_name=json_dict['clinical_text_entity_id_property_name'],
        clinical_text_date_time_properties_names=json_dict['clinical_text_date_time_properties_names'],
        root_entities_spec=RootEntitiesSpec(
            root_entity=json_dict['root_entities_spec']['root_entity'],
            id_property=json_dict['root_entities_spec']['id_property'],
            ids=ids if ids is not None else json_dict['root_entities_spec']['ids'],
        ),
        clinical_text_extraction_duration_spec=ClinicalTextExtractionDurationSpec(
            first_minutes=json_dict['clinical_text_extraction_duration_spec']['first_minutes']
        )
    )


def to_defaultdict(d: dict) -> defaultdict:
    d = defaultdict(lambda: None, d)
    for key, value in d.items():
        if isinstance(value, dict):
            d[key] = to_defaultdict(value)
    return d
