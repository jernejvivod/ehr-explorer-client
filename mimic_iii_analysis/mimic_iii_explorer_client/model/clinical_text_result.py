from dataclasses import dataclass

from dataclasses_json import dataclass_json


@dataclass_json
@dataclass
class ClinicalTextResultDto:
    root_entity_id: str
    text: str
