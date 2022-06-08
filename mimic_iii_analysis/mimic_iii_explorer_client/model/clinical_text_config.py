from dataclasses import dataclass
from typing import List

from dataclasses_json import dataclass_json


@dataclass_json
@dataclass
class RootEntitiesSpec:
    root_entity: str
    id_property: str
    ids: List[object]


@dataclass_json
@dataclass
class DataRangeSpec:
    n_records: int


@dataclass_json
@dataclass
class ClinicalTextConfig:
    root_entities_spec: RootEntitiesSpec
    data_range_spec: DataRangeSpec
