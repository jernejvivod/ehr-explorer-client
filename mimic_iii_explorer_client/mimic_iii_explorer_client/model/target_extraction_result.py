from dataclasses import dataclass

from dataclasses_json import dataclass_json


@dataclass_json
@dataclass
class ExtractedTargetDto:
    root_entity_id: str
    target_value: int
