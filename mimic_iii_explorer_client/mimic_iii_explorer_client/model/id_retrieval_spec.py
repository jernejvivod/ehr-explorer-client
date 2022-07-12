from dataclasses import dataclass
from enum import Enum
from typing import List

from dataclasses_json import dataclass_json


class ComparatorEnum(Enum):
    LESS = 'LESS'
    EQUAL = 'EQUAL'
    MORE = 'MORE'


@dataclass_json
@dataclass
class IdRetrievalFilterSpec:
    entity_name: str
    property_name: str
    comparator: ComparatorEnum
    property_val: object


@dataclass_json
@dataclass
class IdRetrievalSpec:
    entity_name: str
    id_property: str
    filter_specs: List[IdRetrievalFilterSpec] or None
