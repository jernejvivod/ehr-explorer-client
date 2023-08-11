import json
from collections import defaultdict
from typing import List

from generated_client import (
    IdRetrievalSpec,
    IdRetrievalFilterSpec,
    TargetExtractionSpec,
    ClinicalTextConfig,
    RootEntitiesSpec,
    ClinicalTextExtractionDurationSpec,
    WordificationConfig,
    ConcatenationSpec,
    PropertySpec,
    PropertySpecEntry,
    RootEntityAndTimeLimit,
    CompositeColumnsSpec,
    CompositeColumnsSpecEntry,
    ValueTransformationSpec,
    ValueTransformationSpecEntry,
    Transform,
    CompositePropertySpecEntry
)


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
        age_lim=json_dict['age_lim'],
        max_days_interval_positive=json_dict['max_days_interval_positive'],
        max_days_death_after_last_positive=json_dict['max_days_death_after_last_positive']
    )


def parse_request_spec_clinical_text(spec_file_path: str, ids: List[str] = None) -> ClinicalTextConfig:
    with open(spec_file_path, 'r') as f:
        json_dict = to_defaultdict(json.load(f))
    return ClinicalTextConfig(
        foreign_key_path=json_dict['foreign_key_path'],
        text_property_name=json_dict['text_property_name'],
        clinical_text_entity_id_property_name=json_dict['clinical_text_entity_id_property_name'],
        clinical_text_date_time_properties_names=json_dict['clinical_text_date_time_properties_names'],
        root_entity_datetime_property_for_cutoff=json_dict['root_entity_datetime_property_for_cutoff'],
        root_entities_spec=RootEntitiesSpec(
            root_entity=json_dict['root_entities_spec']['root_entity'],
            id_property=json_dict['root_entities_spec']['id_property'],
            ids=ids if ids is not None else json_dict['root_entities_spec']['ids'],
        ),
        clinical_text_extraction_duration_spec=ClinicalTextExtractionDurationSpec(
            first_minutes=json_dict['clinical_text_extraction_duration_spec']['first_minutes']
        ) if json_dict['clinical_text_extraction_duration_spec'] is not None else None
    )


def parse_request_spec_wordification(spec_file_path: str, ids: List[str] = None) -> WordificationConfig:
    with open(spec_file_path, 'r') as f:
        json_dict = to_defaultdict(json.load(f))
    return WordificationConfig(
        concatenation_spec=ConcatenationSpec(concatenation_scheme=json_dict['concatenation_spec']['concatenation_scheme']),
        root_entities_spec=RootEntitiesSpec(
            root_entity=json_dict['root_entities_spec']['root_entity'],
            id_property=json_dict['root_entities_spec']['id_property'],
            ids=ids if ids is not None else json_dict['root_entities_spec']['ids'],
        ),
        property_spec=PropertySpec(
            entries=[PropertySpecEntry(
                entity=entry['entity'],
                properties=entry['properties'],
                property_for_limit=entry['property_for_limit'],
                composite_property_spec_entries=[
                    CompositePropertySpecEntry(
                        e['property_on_this_entity'],
                        e['property_on_other_entity'],
                        e['foreign_key_path'],
                        e['composite_property_name'],
                        e['combiner']
                    ) for e in entry['composite_property_spec_entries']
                ] if entry['composite_property_spec_entries'] is not None else None
            ) for entry in json_dict['property_spec']['entries']],
            root_entity_and_lime_limit=[
                RootEntityAndTimeLimit(e['root_entity_id'], e['time_lim']) for e in json_dict['property_spec']['root_entity_and_lime_limit']
            ] if json_dict['property_spec']['root_entity_and_lime_limit'] is not None else None
        ),
        composite_columns_spec=CompositeColumnsSpec(
            entries=[
                CompositeColumnsSpecEntry(
                    foreign_key_path1=e['foreign_key_path1'],
                    property1=e['property1'],
                    foreign_key_path2=e['foreign_key_path2'],
                    property2=e['property2'],
                    composite_name=e['composite_name'],
                    combiner='DATE_DIFF'
                ) for e in json_dict['composite_columns_spec']['entries']
            ]
        ) if json_dict['composite_columns_spec'] is not None else None,
        value_transformation_spec=ValueTransformationSpec(
            entries=[
                ValueTransformationSpecEntry(
                    entity=e['entity'],
                    _property=e['_property'],
                    transform=Transform(
                        kind=e['transform']['kind'],
                        date_diff_round_type=e['transform']['date_diff_round_type'],
                        rounding_multiple=e['transform']['rounding_multiple']
                    )
                ) for e in json_dict['value_transformation_spec']['entries']
            ]
        ) if json_dict['value_transformation_spec'] is not None else None
    )


def to_defaultdict(d: dict) -> defaultdict:
    d = defaultdict(lambda: None, d)
    for key, value in d.items():
        if isinstance(value, dict):
            d[key] = to_defaultdict(value)
        elif isinstance(value, list):
            d[key] = [to_defaultdict(e) if isinstance(e, dict) else e for e in value]
    return d
