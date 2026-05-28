from dataclasses import dataclass, field
from typing import Any


@dataclass
class Validity:
    category: str
    message: str
    status_code: int | None = None


@dataclass
class Variant:
    canonical_url: str
    url: str
    payload: dict[Any, Any] | None
    validity: Validity


@dataclass
class Seed:
    canonical_path: str
    http_method: str
    variants: list[Variant] = field(default_factory=list)