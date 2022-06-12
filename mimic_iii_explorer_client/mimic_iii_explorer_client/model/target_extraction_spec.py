from dataclasses import dataclass
from enum import Enum
from typing import List

from dataclasses_json import dataclass_json


class TargetTypeEnum(Enum):
    PATIENT_DIED_DURING_ADMISSION = 'PATIENT_DIED_DURING_ADMISSION'


@dataclass_json
@dataclass
class TargetExtractionSpecDto:
    target_type: TargetTypeEnum
    ids: List[object]
