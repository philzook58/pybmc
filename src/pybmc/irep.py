from dataclasses import dataclass, field
from typing import Dict, List
import json

# Assuming `IrepId` is just a string alias
IrepId = str


@dataclass
class Irep:
    """Represents the CBMC serialization format for goto-programs."""

    id: IrepId
    sub: List["Irep"] = field(default_factory=list)
    named_sub: Dict[IrepId, "Irep"] = field(default_factory=dict)

    def to_json(self) -> str:
        """Serializes the Irep structure to a JSON string."""
        return json.dumps(self.to_dict())

    def to_dict(self) -> Dict:
        """Converts Irep into a dictionary for serialization."""
        return {
            "id": self.id,
            "sub": [s.to_dict() for s in self.sub],
            "named_sub": {k: v.to_dict() for k, v in self.named_sub.items()},
        }

    @classmethod
    def from_json(cls, json_str: str) -> "Irep":
        """Deserializes an Irep structure from a JSON string."""
        return cls.from_dict(json.loads(json_str))

    @classmethod
    def from_dict(cls, data: Dict) -> "Irep":
        """Converts a dictionary into an Irep object."""
        return cls(
            id=data["id"],
            sub=[cls.from_dict(s) for s in data["sub"]],
            named_sub={k: cls.from_dict(v) for k, v in data["named_sub"].items()},
        )


# https://github.com/model-checking/kani/blob/main/cprover_bindings/src/irep/to_irep.rs
def to_irep(x):
    raise NotImplementedError
